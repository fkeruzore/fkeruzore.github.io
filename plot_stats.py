import os
import yaml
import git
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import argparse

plt.style.use("petroff10")

# ┌───────────────────────────────────────────────────────────────────────────┐
# │  USER-CONFIGURATION SECTION                                               │
# └───────────────────────────────────────────────────────────────────────────┘

# Path to your Git repository; if you run this script from the repo root, you
# can leave this as ".". Otherwise, point it to the folder containing .git/.
REPO_PATH = "."

# The exact commit message your pipeline always uses when updating
# _data/pub_stats.yml. Example: if your GH Action always does:
# `git commit -m "Update pub stats"`, then set: COMMIT_MSG = "Update pub stats"
# Make sure this matches exactly (including capitalization and spacing).
COMMIT_MSG = "Auto-update publication page"


# ┌───────────────────────────────────────────────────────────────────────────┐
# │  END OF USER-CONFIGURATION SECTION                                        │
# └───────────────────────────────────────────────────────────────────────────┘


def collect_history(repo_path, commit_msg, data_relpath="_data/pub_stats.yml"):
    """
    Walks through all commits on 'master', finds those with
    message == commit_msg, and returns a list of dicts:
    { 'date': datetime, 'stats': { ... } }.
    """
    repo = git.Repo(repo_path)

    history = []
    # Make sure we're on master (or change branch name if needed)
    # If your default branch is 'master', this works; otherwise adjust.
    commits = list(repo.iter_commits("master"))

    for commit in commits:
        # Compare the full commit message (strip off trailing newlines/spaces)
        if commit.message.strip() == commit_msg:
            # Try to find the YAML file in that commit’s tree
            try:
                blob = commit.tree / data_relpath
            except KeyError:
                # If the file doesn't exist at this commit, skip it
                continue

            content_bytes = blob.data_stream.read()
            try:
                stats_dict = yaml.safe_load(content_bytes)
            except Exception as e:
                print(f"Warning: failed to parse YAML at {commit.hexsha}: {e}")
                continue

            # Record the timestamp (use committed_datetime, a datetime object)
            dt = commit.committed_datetime
            history.append({"date": dt, "stats": stats_dict})

    # Sort by date ascending
    history.sort(key=lambda x: x["date"])
    return history


def remove_glitches(history):
    """
    Remove glitches where a metric increases on one day and decreases
    the next. This happens when a publication is counted twice on
    release day, then corrected.

    Returns a cleaned history list with glitch entries removed.
    """
    if len(history) < 3:
        return history

    # Get all stat keys from first entry
    stat_keys = list(history[0]["stats"].keys())

    # Track indices to remove
    indices_to_remove = set()

    for i in range(1, len(history) - 1):
        prev_stats = history[i - 1]["stats"]
        curr_stats = history[i]["stats"]
        next_stats = history[i + 1]["stats"]

        # Check if this looks like a glitch for any metric
        is_glitch = False
        for key in stat_keys:
            try:
                prev_val = int(prev_stats.get(key, 0))
                curr_val = int(curr_stats.get(key, 0))
                next_val = int(next_stats.get(key, 0))

                # Glitch pattern: increase followed by decrease back to
                # or below previous level
                if curr_val > prev_val and next_val < curr_val:
                    is_glitch = True
                    print(
                        "Detected glitch at"
                        f"{history[i]['date'].strftime('%Y-%m-%d')}: "
                        f"{key} jumped from {prev_val} to {curr_val},"
                        f"then dropped to {next_val}"
                    )
                    break
            except (ValueError, TypeError):
                continue

        if is_glitch:
            indices_to_remove.add(i)

    # Return filtered history
    cleaned = [
        entry for i, entry in enumerate(history) if i not in indices_to_remove
    ]
    if indices_to_remove:
        print(f"Removed {len(indices_to_remove)} glitch entries")
    return cleaned


def plot_time_series(history, deglitch=False):
    """
    Given a list of { 'date': datetime, 'stats': { ... } }, plot each key
    in stats over time.
    """
    if not history:
        print("No matching commits found. Exiting.")
        return

    # Remove glitches before plotting if requested
    if deglitch:
        history = remove_glitches(history)

    # Extract all unique stat-keys (assuming all commits have the same keys)
    sample_stats = history[0]["stats"].keys()
    stat_keys = list(sample_stats)

    # Prepare data: for each stat, make a list of (date, value)
    dates = [entry["date"] for entry in history]
    values = {
        key: [entry["stats"].get(key, None) for entry in history]
        for key in stat_keys
    }

    # Start plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    for key in stat_keys:
        # Convert values to integers (or floats) if needed
        y = []
        for v in values[key]:
            try:
                y.append(int(v))
            except (ValueError, TypeError):
                try:
                    y.append(float(v))
                except:
                    y.append(None)
        if key in ["publications", "citecount", "hindex", "fa_papers"]:
            kw = dict(alpha=1, marker="o")
        else:
            kw = dict(alpha=0.5)

        label = {
            "publications": "Total publications",
            "citecount": "Total citations",
            "hindex": "h-index",
            "fa_papers": "First author articles",
            "co_papers": "Co-author articles",
            "fa_procs": "First author proceedings",
            "co_procs": "Co-author proceedings",
        }[key]
        line = ax.plot(dates, y, label=label, **kw)[0]

        # Add final value at the end of the line
        if y and y[-1] is not None:
            ax.text(
                dates[-1],
                y[-1],
                f"  {y[-1]:.0f}",
                va="center",
                ha="left",
                color=line.get_color(),
            )

    # Format the x-axis for dates
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(
        mdates.ConciseDateFormatter(mdates.AutoDateLocator())
    )
    ax.set_yscale("log")
    ax.set_xlabel("Commit Date")
    ax.set_ylabel("Value")
    ax.set_title("Time Evolution of Publication Statistics")
    ax.legend(ncol=2)
    ax.grid(alpha=0.5)
    ax.xaxis.set_ticks_position("both")
    ax.yaxis.set_ticks_position("both")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot publication statistics over time from git history"
    )
    parser.add_argument(
        "--deglitch",
        action="store_true",
        help="Remove glitches where metrics temporarily spike then drop back",
    )
    args = parser.parse_args()

    history = collect_history(REPO_PATH, COMMIT_MSG)
    plot_time_series(history, deglitch=args.deglitch)

import os
import yaml
import git
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  USER-CONFIGURATION SECTION                                                 │
# └─────────────────────────────────────────────────────────────────────────────┘

# Path to your Git repository; if you run this script from the repo root,
# you can leave this as ".". Otherwise, point it to the folder containing .git/.
REPO_PATH = "."

# The exact commit message your pipeline always uses when updating _data/pub_stats.yml.
# Example: if your GH Action always does: `git commit -m "Update pub stats"`, then set:
#    COMMIT_MSG = "Update pub stats"
#
# Make sure this matches exactly (including capitalization and spacing).
COMMIT_MSG = "Auto-update publication page"


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  END OF USER-CONFIGURATION SECTION                                          │
# └─────────────────────────────────────────────────────────────────────────────┘


def collect_history(repo_path, commit_msg, data_relpath="_data/pub_stats.yml"):
    """
    Walks through all commits on 'master', finds those with message == commit_msg,
    and returns a list of dicts: { 'date': datetime, 'stats': { ... } }.
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

            # Record the timestamp (use committed_datetime, which is a datetime object)
            dt = commit.committed_datetime
            history.append({"date": dt, "stats": stats_dict})

    # Sort by date ascending
    history.sort(key=lambda x: x["date"])
    return history


def plot_time_series(history):
    """
    Given a list of { 'date': datetime, 'stats': { ... } }, plot each key in stats over time.
    """
    if not history:
        print("No matching commits found. Exiting.")
        return

    # Extract all unique stat-keys (assuming all commits have the same keys)
    sample_stats = history[0]["stats"].keys()
    stat_keys = list(sample_stats)

    # Prepare data: for each stat, make a list of (date, value)
    dates = [entry["date"] for entry in history]
    values = {
        key: [entry["stats"].get(key, None) for entry in history] for key in stat_keys
    }

    # Start plotting
    plt.figure(figsize=(10, 6))
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
        plt.plot(dates, y, marker="o", label=key)

    # Format the x-axis for dates
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(
        mdates.ConciseDateFormatter(mdates.AutoDateLocator())
    )
    plt.xlabel("Commit Date")
    plt.ylabel("Value")
    plt.title("Time Evolution of Publication Statistics")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    history = collect_history(REPO_PATH, COMMIT_MSG)
    plot_time_series(history)

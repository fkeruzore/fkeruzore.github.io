import os
import requests
from urllib.parse import urlencode
import json

token = os.environ["ADS_DEV_KEY"]
secu_header = {"Authorization": f"Bearer {token}"}


def get_bibcodes(rows=1000):
    """Fetch a list of publications I am listed as an author on in the
    NASA ADS database, and returns a dict with the list of corresponding
    ADS bibcodes classed by publication type and authorship.

    Parameters
    ----------
    rows : int
        Number of rows to be exported.

    Returns
    -------
    dict
        bibcodes corresponding to my publications, with keys:
        'fa_papers': list of first author papers
        'co_papers': list of co-author papers
        'fa_procs': list of first author proceedings
        'co_procs': list of co-author proceedings
        'others': everything else (codes, datasets, ...)
    dict
        Publication titles, with the same categories as bibcodes.
    dict
        Publication dates, with the same categories as bibcodes.
    dict
        Publication journals, with the same categories as bibcodes.
    """
    # Get list of ADS entries I am an author of
    query = {
        "q": "author:keruzore, f",
        "fl": "bibcode, first_author, doctype, title, date, pub, abstract",
        "rows": rows,
        "sort": "date desc",
    }

    encoded_query = urlencode(query)
    results = requests.get(
        "https://api.adsabs.harvard.edu/v1/search/query?{}".format(
            encoded_query
        ),
        headers=secu_header,
    ).json()
    pubs = results["response"]["docs"]

    # Get their bibcodes sorted by pub type and first authorship
    bibcodes = {
        "fa_papers": [],
        "co_papers": [],
        "fa_procs": [],
        "co_procs": [],
        "others": [],
    }
    titles = {k: [] for k in bibcodes.keys()}
    dates = {k: [] for k in bibcodes.keys()}
    journals = {k: [] for k in bibcodes.keys()}
    abstracts = {k: [] for k in bibcodes.keys()}

    # Some entries are going to be misclassified, I'll deal with them manually
    with open("./_publications/specials.json", "r") as f:
        specials = json.load(f)

    for pub in pubs:
        bibcode = pub["bibcode"]
        title = pub["title"][0]
        date = pub["date"][:10]  # YYYY-MM-DD, the day might be wrong
        journal = pub["pub"]
        abstract = pub.get("abstract", "No abstract available.")

        if pub["bibcode"] in specials.keys():
            bibcodes[specials[bibcode]].append(bibcode)
            titles[specials[bibcode]].append(title)
            dates[specials[bibcode]].append(date)
            journals[specials[bibcode]].append(journal)
            abstracts[specials[bibcode]].append(abstract)
            continue

        fa = pub["first_author"].lower()
        fa_me = ("kéruzoré" in fa) or ("keruzore" in fa)
        k_aut = "fa" if fa_me else "co"

        if pub["doctype"] in ["article", "eprint"]:
            bibcodes[f"{k_aut}_papers"].append(bibcode)
            titles[f"{k_aut}_papers"].append(title)
            dates[f"{k_aut}_papers"].append(date)
            journals[f"{k_aut}_papers"].append(journal)
            abstracts[f"{k_aut}_papers"].append(abstract)
        elif pub["doctype"] == "inproceedings":
            bibcodes[f"{k_aut}_procs"].append(bibcode)
            titles[f"{k_aut}_procs"].append(title)
            dates[f"{k_aut}_procs"].append(date)
            journals[f"{k_aut}_procs"].append(journal)
            abstracts[f"{k_aut}_procs"].append(abstract)
        else:
            bibcodes["others"].append(bibcode)
            titles["others"].append(title)
            abstracts["others"].append(abstract)

    return bibcodes, titles, dates, journals, abstracts


def get_bibtex_entries(bibcodes):
    """Get bibtex entries from a list of ADS bibcodes.

    Parameters
    ----------
    bibcodes : list
        List of ADS bibcodes.

    Returns
    -------
    full_bibtex: str
        A full .bib file containing the bibtex entry corresponding to
        every bibcode
    bibtexs: list[str]
        List of bibtex entries for each bibcode.
    """
    # Request bibtex entry for each bibcode
    payload = {
        "bibcode": bibcodes,
        "sort": "date desc",
    }
    results = requests.post(
        "https://api.adsabs.harvard.edu/v1/export/bibtex",
        headers=secu_header,
        data=json.dumps(payload),
    )
    full_bibtex = results.json()["export"]  # That's the full .bib file
    bibtexs = [
        f"@{b}" for b in full_bibtex.split("@")[1:]
    ]  # individual bibtex entries
    return full_bibtex, bibtexs


def get_citation(bibcodes):
    """Get aastex entries from a list of ADS bibcodes.

    Parameters
    ----------
    bibcodes : list
        List of ADS bibcodes.

    Returns
    -------
    cites: list[str]
        List of citation strings for each bibcode.
    """
    payload = {
        "bibcode": bibcodes,
        "format": "%5.3l (%Y), %J, %V, %p.\n",
        "sort": "date desc",
    }
    results = requests.post(
        "https://api.adsabs.harvard.edu/v1/export/custom",
        headers=secu_header,
        data=json.dumps(payload),
    )
    cites = results.json()["export"].split("\n\n")[:-1]
    return cites


def get_citecount_hindex(bibcodes):
    """Get citation counts and h-index from a list of ADS bibcodes.

    Parameters
    ----------
    bibcodes : list
        List of ADS bibcodes.

    Returns
    -------
    citecount: int
        Total number of citations for all bibcodes.
    h: int
        h-index for bibcodes.
    """
    payload = {"bibcodes": bibcodes, "types": ["citations", "indicators"]}
    results = requests.post(
        "https://api.adsabs.harvard.edu/v1/metrics",
        headers={**secu_header, "Content-type": "application/json"},
        data=json.dumps(payload),
    )
    stats = results.json()
    citecount = stats["citation stats"]["total number of citations"]
    h = stats["indicators"]["h"]
    return citecount, h


if __name__ == "__main__":

    # Clean directory
    files = os.listdir("./_publications")
    for f in files:
        if f.endswith(".md") and (f != "phdthesis.md"):
            os.remove(f"./_publications/{f}")

    # Prepare file to store stats
    file_pub_stats = open("./_data/pub_stats.yml", "w")

    # Get bibcodes neatly organized
    all_bibcodes, all_titles, all_dates, all_journals, all_abstracts = get_bibcodes(rows=999)

    # Total publications
    all_bibcodes["all_pubs"] = (
        all_bibcodes["fa_papers"]
        + all_bibcodes["co_papers"]
        + all_bibcodes["fa_procs"]
        + all_bibcodes["co_procs"]
    )
    file_pub_stats.write(f"publications: {len(all_bibcodes['all_pubs'])}\n")

    # Citation stats
    citecount, h = get_citecount_hindex(all_bibcodes["all_pubs"])
    file_pub_stats.write(f"citecount: {citecount}\n")
    file_pub_stats.write(f"hindex: {h}\n")

    for pub_type in ["fa_papers", "co_papers", "fa_procs", "co_procs"]:
        bibcodes = all_bibcodes[pub_type]
        titles = all_titles[pub_type]
        dates = all_dates[pub_type]
        journals = all_journals[pub_type]
        abstracts = all_abstracts[pub_type]
        cites = get_citation(bibcodes)

        for bibcode, title, date, journal, abstract, cite in zip(
            bibcodes, titles, dates, journals, abstracts, cites
        ):
            bibcode_nodot = bibcode.replace(".", "")
            title_formatted = title.replace("\\", "\\\\")
            # Escape abstract: first backslashes, then quotes
            abstract_formatted = abstract.replace("\\", "\\\\").replace('"', '\\"')

            # Write .md file for each publication
            with open(f"./_publications/{bibcode_nodot}.md", "w") as file_pub:
                file_pub.write("---\n")
                file_pub.write(f'title: "{title_formatted}"\n')
                file_pub.write('collection: "publications"\n')
                file_pub.write(f'category: "{pub_type}"\n')
                file_pub.write(f"permalink: /publications/{bibcode_nodot}\n")
                file_pub.write(
                    "link: https://ui.adsabs.harvard.edu/abs/"
                    + f"{bibcode}/abstract\n"
                )
                file_pub.write(f"date: {date}\n")
                file_pub.write(f'venue: "{journal}"\n')
                file_pub.write(f'citation: "{cite}"\n')
                file_pub.write(f'abstract: "{abstract_formatted}"\n')
                file_pub.write("---")

        # Append stats of publication type to stats file
        file_pub_stats.write(f"{pub_type}: {len(bibcodes)}\n")

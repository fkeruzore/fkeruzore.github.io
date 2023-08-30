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
        "fl": "bibcode, first_author, doctype, title, date, pub",
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

    # Some entries are going to be misclassified, I'll deal with them manually
    specials = {
        "2022arXiv220414052A": "co_procs",
    }
    for pub in pubs:
        bibcode = pub["bibcode"]
        title = pub["title"][0]
        date = pub["date"][:10]  # YYYY-MM-DD, the day might be wrong
        journal = pub["pub"]

        if pub["bibcode"] in specials.keys():
            bibcodes[specials[bibcode]].append(bibcode)
            titles[specials[bibcode]].append(title)
            dates[specials[bibcode]].append(date)
            journals[specials[bibcode]].append(journal)
            continue

        fa = pub["first_author"].lower()
        fa_me = ("kéruzoré" in fa) or ("keruzore" in fa)
        k_aut = "fa" if fa_me else "co"

        if pub["doctype"] in ["article", "eprint"]:
            bibcodes[f"{k_aut}_papers"].append(bibcode)
            titles[f"{k_aut}_papers"].append(title)
            dates[f"{k_aut}_papers"].append(date)
            journals[f"{k_aut}_papers"].append(journal)
        elif pub["doctype"] == "inproceedings":
            bibcodes[f"{k_aut}_procs"].append(bibcode)
            titles[f"{k_aut}_procs"].append(title)
            dates[f"{k_aut}_procs"].append(date)
            journals[f"{k_aut}_procs"].append(journal)
        else:
            bibcodes["others"].append(bibcode)
            titles["others"].append(title)

    return bibcodes, titles, dates, journals


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


if __name__ == "__main__":
    all_bibcodes, all_titles, all_dates, all_journals = get_bibcodes(rows=100)

    for pub_type in ["fa_papers", "co_papers", "fa_procs", "co_procs"]:
        bibcodes = all_bibcodes[pub_type]
        titles = all_titles[pub_type]
        dates = all_dates[pub_type]
        journals = all_journals[pub_type]
        cites = get_citation(bibcodes)

        for bibcode, title, date, journal, cite in zip(
            bibcodes, titles, dates, journals, cites
        ):
            bibcode_nodot = bibcode.replace(".", "")
            md = f"""---
    title: "{title}"
    collection: "publications"
    category: "{pub_type}"
    permalink: /publications/{bibcode_nodot}
    date: {date}
    venue: "{journal}"
    citation: "{cite}"
    ---"""
            with open(f"./_publications/{bibcode_nodot}.md", "w") as f:
                f.write(md)

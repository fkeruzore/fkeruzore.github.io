import adsync

all_bibcodes, all_titles, all_dates, all_journals = adsync.get_bibcodes(
    rows=100
)

for pub_type in ["fa_papers", "co_papers", "fa_procs", "co_procs"]:
    bibcodes = all_bibcodes[pub_type]
    titles = all_titles[pub_type]
    dates = all_dates[pub_type]
    journals = all_journals[pub_type]
    cites = adsync.get_citation(bibcodes)

    for bibcode, title, date, journal, cite in zip(
        bibcodes, titles, dates, journals, cites
    ):
        md = f"""---
title: "{title}"
collection: "{pub_type}"
permalink: /publications/{bibcode}
date: {date}
venue: "{journal}"
citation: "{cite}"
---"""
        with open(f"./{bibcode}.md", "w") as f:
            f.write(md)

---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<strong>{{ site.data.pub_stats.publications }}</strong> publications; <strong>{{ site.data.pub_stats.citecount }}</strong> citations; h-index: <strong>{{ site.data.pub_stats.hindex }}</strong> (*Source*: [NASA ADS](https://ui.adsabs.harvard.edu/search/filter_doctype_facet_hier_fq_doctype=AND&filter_doctype_facet_hier_fq_doctype=doctype_facet_hier%3A%220%2FArticle%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq_doctype=(doctype_facet_hier%3A%220%2FArticle%22)&q=%20author%3A%22keruzore%2C%20florian%22&sort=date%20desc%2C%20bibcode%20desc&p_=0))

<div class="publications-compact" markdown="1">

# Journal Articles

## ✍️ As first author

{% for post in site.publications reversed %}
  {% if post.category == "fa_papers" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

## 👥 As co-author

{% for post in site.publications reversed %}
  {% if post.category == "co_papers" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

# Conference Proceedings

## ✍️ As first author

{% for post in site.publications reversed %}
  {% if post.category == "fa_procs" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

## 👥 As co-author

{% for post in site.publications reversed %}
  {% if post.category == "co_procs" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

# 🎓 PhD Thesis

{% for post in site.publications reversed %}
  {% if post.category == "thesis" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

</div>

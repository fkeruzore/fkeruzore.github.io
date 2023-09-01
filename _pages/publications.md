---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

Total number of publications: <strong>{{ site.data.pub_stats.publications }}</strong> (<strong>{{ site.data.pub_stats.citecount }}</strong> citations, h-index: <strong>{{ site.data.pub_stats.hindex }}</strong>)

# Journal Articles

## As first author

{% for post in site.publications reversed %}
  {% if post.category == "fa_papers" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

## As co-author

{% for post in site.publications reversed %}
  {% if post.category == "co_papers" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

# Conference Proceedings

## As first author

{% for post in site.publications reversed %}
  {% if post.category == "fa_procs" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

## As co-author

{% for post in site.publications reversed %}
  {% if post.category == "co_procs" %}
    {% include publication-publication.html %}
  {% endif %}
{% endfor %}

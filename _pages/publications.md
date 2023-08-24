---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

# Journal Articles

## As primary author

{% for post in site.publications reversed %}
  {% if post.category == "fa_papers" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

## As co-author

{% for post in site.publications reversed %}
  {% if post.category == "co_papers" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

# Conference Proceedings

## As primary author

{% for post in site.publications reversed %}
  {% if post.category == "fa_procs" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

## As co-author

{% for post in site.publications reversed %}
  {% if post.category == "co_procs" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

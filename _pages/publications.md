---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

Journal Articles
======

{% for post in site.publications reversed %}
  {% if post.collection == "fa_papers" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
  {% if post.collection == "co_papers" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

Conference Proceedings
======

{% for post in site.publications reversed %}
  {% if post.collection == "fa_procs" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
  {% if post.collection == "co_procs" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

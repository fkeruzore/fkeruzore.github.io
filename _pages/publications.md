---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

Journal Articles
======

{% for post in site.fa_papers reversed %}
  {% include archive-single.html %}
{% endfor %}

{% for post in site.co_papers reversed %}
  {% include archive-single.html %}
{% endfor %}

Conference Proceedings
======

{% for post in site.fa_procs reversed %}
  {% include archive-single.html %}
{% endfor %}

{% for post in site.co_procs reversed %}
  {% include archive-single.html %}
{% endfor %}

---
layout: "base.njk"
title: "Blog"
permalink: "blog.html"
---
<section id="blog">
    <h2>Blog</h2>
    {%- if collections.post.length -%} {# Check if there are any posts #}
        <ul>
            {%- for post in collections.post | reverse -%}
                <li>
                    <a href="{{ post.url }}">
                        <h3>{{ post.data.title }}</h3>
                        <p>{{ post.date | readableDate }}</p>
                    </a>
                </li>
            {%- endfor -%}
        </ul>
    {%- else -%}
        <p>No blog posts yet. Please check back soon!</p> {# Fallback message #}
    {%- endif -%}
</section>

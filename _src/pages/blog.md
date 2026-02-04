---
layout: "base.njk"
title: "Blog"
---
<section id="blog">
    <h2>Blog</h2>
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
</section>

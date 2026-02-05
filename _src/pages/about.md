---
layout: "base.njk"
title: "About"
jobs:
  - title: "Software Developer Intern"
    company: "Queensland Investment Corporation (QIC)"
    date: "Sep 2025 - Present"
    items:
      - "Maintained and validated market/derivatives data pipelines used by integration and analytics teams."
      - "Fixed a calculation defect in realised bond-volatility bilinear interpolation by refactoring state management."
      - "Improved reliability by adding CI regression checks and targeted tests to ensure performance stays within tolerance."
  - title: "Software Engineer"
    company: "UQ Racing"
    date: "Feb 2025 - Oct 2025"
    items:
      - "Authored C++ and Python code for vehicle computer vision systems, leveraging simulation and real-world test data to optimise path planning, increasing navigational accuracy."
      - "Refactored the AV cone detection algorithm, splitting C++/Python bases into modular components to reduce complexity by 40%."
      - "Collaborated with engineering teams to integrate software components ensuring compliance with Formula SAE specs."
  - title: "Secretary"
    company: "UQ Computing Society"
    date: "Oct 2025 - Present"
    items:
      - "Previously <em>General Executive Committee</em> (Aug 2025 - Oct 2025). Managed and delegated tasks among Exec Committee."
      - "Assisted with running community driven and social events."
projects:
  - name: "stochastic-density-dynamics"
    description: "A computational study and 3D visualization of probability density evolution in stochastic processes."
    url: "https://github.com/april-webm/stochastic-density-dynamics"
  - name: "SIG-Algothon-2025"
    description: "Strategy Implementation for the UNSW x SIG Algothon 2025."
    url: "https://github.com/april-webm/SIG-Algothon-2025"
  - name: "Kestrel"
    description: "A modern Python library for stochastic process modelling, parameter estimation and Monte Carlo simulation."
    url: "https://github.com/april-webm/kestrel"
  - name: "aprils-resume-template"
    description: "A parser-friendly resume template created in Typst."
    url: "https://github.com/april-webm/aprils-resume-template"
---

<section id="experience">

## Experience

{% for job in jobs %}
<div class="job">

### {{ job.title }}

**{{ job.company }}** | {{ job.date }}

{% for item in job.items %}
- {{ item | safe }}
{% endfor %}

</div>
{% endfor %}

</section>

<section id="projects">

## Projects

<div class="project-grid">
{% for project in projects %}
<div class="project">

### {{ project.name }}

{{ project.description }}

<a href="{{ project.url }}" target="_blank">View on GitHub</a>

</div>
{% endfor %}
</div>

</section>

<section id="skills">

## Technical Skills

- **Languages:** Python, Java, C++, R
- **Libraries:** pandas, NumPy, PyTorch, scikit-learn, Matplotlib, statsmodels
- **Tools:** Git, Linux/Unix Command Line, Docker, JUnit, pytest

</section>

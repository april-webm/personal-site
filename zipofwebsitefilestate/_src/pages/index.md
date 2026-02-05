---
layout: "base.njk"
title: "Home"
script: |
    // Function to update the monster counter
    function updateMonsterCounter() {
        const lastMonsterDateStr = localStorage.getItem('lastMonsterDate');
        let lastMonsterDate;

        if (!lastMonsterDateStr) {
            // If no date is stored, set it to now and use 0 days
            lastMonsterDate = new Date();
            localStorage.setItem('lastMonsterDate', lastMonsterDate.toISOString());
            document.getElementById('monster-days').textContent = 0;
        } else {
            lastMonsterDate = new Date(lastMonsterDateStr);
            const now = new Date();
            const diffTime = Math.abs(now.getTime() - lastMonsterDate.getTime());
            const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            document.getElementById('monster-days').textContent = diffDays;
        }
    }

    // Run on page load
    updateMonsterCounter();
---
<section id="intro">
    <h2>Welcome!</h2>
    <p>
        Hi there! 👋 I'm April. This is my little corner of the internet.
    </p>
    <p>
        Here you can find some information about me, my projects, and my thoughts on various topics.
    </p>
    <p>
        Use the navigation above to explore the different sections of the site.
    </p>
</section>

<div class="monster-counter">
    <h2>Days Since Last Monster: <span id="monster-days">0</span></h2>
</div>

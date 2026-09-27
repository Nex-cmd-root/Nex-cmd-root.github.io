document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Dark Mode Toggle System ---
    const themeToggleBtn = document.getElementById('theme-toggle');

    function initTheme() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark');
        }
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            document.documentElement.classList.toggle('dark');
            const isDark = document.documentElement.classList.contains('dark');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }

    initTheme();

    // --- 2. Interactive Projection Planner ---
    const actionInput = document.getElementById('monthly-action-amount');
    const proj6m = document.getElementById('proj-6m');
    const proj1y = document.getElementById('proj-1y');
    const proj2y = document.getElementById('proj-2y');

    function calculateProjections() {
        const monthlyVal = parseFloat(actionInput.value) || 0;
        
        // Simple linear projections without market variable standard compound assumptions
        proj6m.textContent = `$${(monthlyVal * 6).toLocaleString()}`;
        proj1y.textContent = `$${(monthlyVal * 12).toLocaleString()}`;
        proj2y.textContent = `$${(monthlyVal * 24).toLocaleString()}`;
    }

    if (actionInput) {
        actionInput.addEventListener('input', calculateProjections);
        calculateProjections(); // initialize
    }

    // --- 3. Accordion FAQ Feature ---
    const faqToggles = document.querySelectorAll('.faq-toggle');

    faqToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const faqItem = toggle.parentElement;
            const isActive = faqItem.classList.contains('active');

            // Close all other items
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
            });

            // Toggle clicked state
            if (!isActive) {
                faqItem.classList.add('active');
            }
        });
    });

    // --- 4. Smooth Learn More Scroll ---
    const learnMoreBtn = document.getElementById('learn-more-btn');
    if (learnMoreBtn) {
        learnMoreBtn.addEventListener('click', () => {
            const target = document.getElementById('features');
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});
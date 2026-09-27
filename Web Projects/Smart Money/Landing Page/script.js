document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Compound Interest Calculator ---
    const principalInput = document.getElementById('principal');
    const contribInput = document.getElementById('annual-contrib');
    const yearsInput = document.getElementById('years');
    const rateInput = document.getElementById('rate');
    const displayVal = document.getElementById('future-value-display');

    function calculateCompoundInterest() {
        const P = parseFloat(principalInput.value) || 0;
        const PMT = parseFloat(contribInput.value) || 0;
        const t = parseFloat(yearsInput.value) || 0;
        const r = (parseFloat(rateInput.value) || 0) / 100;

        if (t < 0 || r < 0) return;

        // Compound interest with regular annual contributions formula
        let total = P * Math.pow(1 + r, t);
        for (let i = 1; i <= t; i++) {
            total += PMT * Math.pow(1 + r, t - i);
        }

        displayVal.textContent = `$${Math.round(total).toLocaleString()}`;
    }

    [principalInput, contribInput, yearsInput, rateInput].forEach(input => {
        if (input) input.addEventListener('input', calculateCompoundInterest);
    });

    calculateCompoundInterest(); // Initial run

    // --- 2. Interactive Budget Calculator (50/30/20) ---
    const incomeInput = document.getElementById('monthly-income');
    const needsVal = document.getElementById('needs-val');
    const wantsVal = document.getElementById('wants-val');
    const savingsVal = document.getElementById('savings-val');

    function updateBudget() {
        const income = parseFloat(incomeInput.value) || 0;
        needsVal.textContent = (income * 0.50).toFixed(0);
        wantsVal.textContent = (income * 0.30).toFixed(0);
        savingsVal.textContent = (income * 0.20).toFixed(0);
    }

    if (incomeInput) {
        incomeInput.addEventListener('input', updateBudget);
    }

    // --- 3. Dynamic Filtering for Investment Types ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const investmentBoxes = document.querySelectorAll('.investment-box');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');

            investmentBoxes.forEach(box => {
                if (filter === 'all' || box.getAttribute('data-category') === filter) {
                    box.style.display = 'block';
                } else {
                    box.style.display = 'none';
                }
            });
        });
    });

    // --- 4. Smooth Scrolling & Active Link Highlight ---
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
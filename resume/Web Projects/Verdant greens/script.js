/**
 * Verdant Greens - Core UI Controller (script.js)
 * Manages FAQ accordions, smooth navigation scrolling,
 * Home page Spectacle showcase rendering, lightbox inspection,
 * and dynamic footer copyright.
 */

document.addEventListener('DOMContentLoaded', () => {

    /* ----------------------------------------------------
       FEATURE 1: Interactive FAQ Accordion
       ---------------------------------------------------- */
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            const icon = question.querySelector('.toggle-icon');

            if (answer) {
                answer.classList.toggle('active');
                if (icon) {
                    icon.textContent = answer.classList.contains('active') ? '−' : '+';
                }
            }
        });
    });

    /* ----------------------------------------------------
       FEATURE 2: Smooth Scrolling for Navigation
       ---------------------------------------------------- */
    const navLinks = document.querySelectorAll('nav a[href^="#"]');

    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#' || targetId === '') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    /* ----------------------------------------------------
       FEATURE 3: Home Page Spectacle Showcase & Filter Tabs
       ---------------------------------------------------- */
    const spectacleGrid = document.getElementById('vg-spectacle-grid');
    if (spectacleGrid && window.VG_SPECTACLES) {
        let currentFilter = 'all';

        function renderSpectacles() {
            const list = currentFilter === 'all'
                ? window.VG_SPECTACLES
                : window.VG_SPECTACLES.filter(s => s.category === currentFilter);

            spectacleGrid.innerHTML = list.map((item, idx) => `
                <div class="spectacle-card" data-id="${item.id}" data-idx="${idx}">
                    <div class="spectacle-image-wrap">
                        <img src="${item.image}" alt="${item.title}" loading="lazy">
                        <span class="spectacle-category-badge">${item.categoryLabel}</span>
                        <button class="spectacle-zoom-btn" data-action="zoom-spectacle" data-id="${item.id}" aria-label="Zoom spectacle image">
                            🔍 Inspect
                        </button>
                    </div>
                    <div class="spectacle-body">
                        <h4 class="spectacle-title">${item.title}</h4>
                        <p class="spectacle-desc">${item.description}</p>
                        <div class="spectacle-tags">
                            ${item.tags.map(t => `<span class="spectacle-tag">#${t}</span>`).join(' ')}
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // Filter pills for spectacles
        const spectaclePills = document.querySelectorAll('.spectacle-pill[data-filter]');
        spectaclePills.forEach(pill => {
            pill.addEventListener('click', () => {
                spectaclePills.forEach(p => p.classList.remove('active'));
                pill.classList.add('active');
                currentFilter = pill.dataset.filter;
                renderSpectacles();
            });
        });

        // Delegate click for Zoom / Lightbox
        spectacleGrid.addEventListener('click', (e) => {
            const card = e.target.closest('.spectacle-card');
            if (card) {
                const id = card.dataset.id;
                openSpectacleLightbox(id);
            }
        });

        renderSpectacles();
    }

    /* ----------------------------------------------------
       FEATURE 4: High-Definition Spectacle Lightbox
       ---------------------------------------------------- */
    function openSpectacleLightbox(spectacleId) {
        if (!window.VG_SPECTACLES) return;
        const item = window.VG_SPECTACLES.find(s => s.id === spectacleId);
        if (!item) return;

        let lightbox = document.getElementById('vg-spectacle-lightbox');
        if (!lightbox) {
            lightbox = document.createElement('div');
            lightbox.id = 'vg-spectacle-lightbox';
            lightbox.className = 'vg-modal-overlay active';
            document.body.appendChild(lightbox);
        } else {
            lightbox.classList.add('active');
        }

        lightbox.innerHTML = `
            <div class="vg-modal-container vg-lightbox-container">
                <button class="vg-modal-close" onclick="document.getElementById('vg-spectacle-lightbox').classList.remove('active')">&times;</button>
                <div class="lightbox-content">
                    <div class="lightbox-img-wrap">
                        <img src="${item.image}" alt="${item.title}">
                    </div>
                    <div class="lightbox-details">
                        <span class="spectacle-category-badge">${item.categoryLabel}</span>
                        <h2>${item.title}</h2>
                        <p>${item.description}</p>
                        <div class="spectacle-tags" style="margin: 15px 0;">
                            ${item.tags.map(t => `<span class="spectacle-tag">#${t}</span>`).join(' ')}
                        </div>
                        <div style="margin-top: 20px; display: flex; gap: 10px; flex-wrap: wrap;">
                            <a href="shop.html" class="btn">Browse Matching Plants in Store →</a>
                            <a href="https://wa.me/26077597103?text=Hi%20Verdant%20Greens,%20I%20love%20the%20${encodeURIComponent(item.title)}%20bundle%20from%20your%20website!%20Is%20a%20similar%20arrangement%20available?" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                                💬 WhatsApp About This Bundle
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    /* ----------------------------------------------------
       FEATURE 5: Dynamic Copyright Year
       ---------------------------------------------------- */
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});
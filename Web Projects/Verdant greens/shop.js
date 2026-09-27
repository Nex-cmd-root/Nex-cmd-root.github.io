/**
 * Verdant Greens - Store Page Controller (shop.js)
 * Implements real-time search, multi-facet filtering (categories, price tiers, care & air purifier traits),
 * sorting (defaulting to Highest Price First), URL param routing, and Quick View modals.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Only run if we are on the store page
    const productGrid = document.getElementById('vg-store-product-grid');
    if (!productGrid) return;

    // Filter & Sort State
    const state = {
        category: 'all',
        priceRange: 'all',
        careFilter: 'all',
        searchQuery: '',
        sortBy: 'price-desc' // Default to highest price first
    };

    // DOM Elements
    const searchInput = document.getElementById('vg-store-search');
    const categoryButtons = document.querySelectorAll('.filter-pill[data-category]');
    const priceButtons = document.querySelectorAll('.price-pill[data-price]');
    const careButtons = document.querySelectorAll('.care-pill[data-care]');
    const sortSelect = document.getElementById('vg-sort-select');
    const resultsCountEl = document.getElementById('vg-results-count');

    // Parse URL query parameters (e.g. shop.html?category=office or shop.html?search=Anthurium)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('category')) {
        const cat = urlParams.get('category').toLowerCase();
        state.category = cat;
        categoryButtons.forEach(btn => {
            if (btn.dataset.category.toLowerCase() === cat) {
                categoryButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            }
        });
    }

    if (urlParams.has('search')) {
        state.searchQuery = urlParams.get('search').trim();
        if (searchInput) searchInput.value = state.searchQuery;
    }

    if (urlParams.has('sort')) {
        state.sortBy = urlParams.get('sort');
        if (sortSelect) sortSelect.value = state.sortBy;
    }

    // Filter & Sort Logic
    function getFilteredProducts() {
        if (!window.VG_PRODUCTS) return [];

        return window.VG_PRODUCTS.filter(product => {
            // 1. Category Filter
            if (state.category !== 'all' && product.category.toLowerCase() !== state.category.toLowerCase()) {
                return false;
            }

            // 2. Price Range Filter (K400 - K1,200 actual on-sale prices)
            if (state.priceRange !== 'all') {
                if (state.priceRange === '400-650' && (product.price < 400 || product.price > 650)) return false;
                if (state.priceRange === '700-950' && (product.price < 700 || product.price > 950)) return false;
                if (state.priceRange === '1000-1200' && (product.price < 1000 || product.price > 1200)) return false;
            }

            // 3. Care / Trait Filter
            if (state.careFilter !== 'all') {
                if (state.careFilter === 'pet' && !product.petFriendly) return false;
                if (state.careFilter === 'low-light' && !product.light.toLowerCase().includes('low') && !product.light.toLowerCase().includes('shade')) return false;
                if (state.careFilter === 'bright' && !product.light.toLowerCase().includes('bright') && !product.light.toLowerCase().includes('sun')) return false;
                if (state.careFilter === 'purifier') {
                    const isPurifier = (product.tags && product.tags.includes('air purifier')) || 
                                       product.badge.toLowerCase().includes('purifier') ||
                                       product.description.toLowerCase().includes('purif');
                    if (!isPurifier) return false;
                }
            }

            // 4. Search Query Filter
            if (state.searchQuery) {
                const query = state.searchQuery.toLowerCase();
                const matchName = product.name.toLowerCase().includes(query);
                const matchBotanical = product.botanicalName.toLowerCase().includes(query);
                const matchDesc = product.description.toLowerCase().includes(query);
                const matchBadge = product.badge.toLowerCase().includes(query);
                const matchCat = product.category.toLowerCase().includes(query);
                const matchTags = product.tags && product.tags.some(t => t.toLowerCase().includes(query));
                if (!matchName && !matchBotanical && !matchDesc && !matchBadge && !matchCat && !matchTags) return false;
            }

            return true;
        }).sort((a, b) => {
            // Sorting Logic
            if (state.sortBy === 'price-desc') return b.price - a.price; // Most expensive at top
            if (state.sortBy === 'price-asc') return a.price - b.price;  // Budget at top
            if (state.sortBy === 'name-asc') return a.name.localeCompare(b.name);
            if (state.sortBy === 'popular') return (b.featured ? 1 : 0) - (a.featured ? 1 : 0);
            return 0;
        });
    }

    // Render Product Cards
    function renderCatalog() {
        const filtered = getFilteredProducts();

        if (resultsCountEl) {
            resultsCountEl.innerHTML = `Showing <strong>${filtered.length}</strong> of ${window.VG_PRODUCTS.length} botanical plants`;
        }

        if (filtered.length === 0) {
            productGrid.innerHTML = `
                <div class="vg-no-results">
                    <div class="no-results-icon">🔍</div>
                    <h3>No Botanical Plants Found</h3>
                    <p>We couldn't find any plants matching your current filter criteria.</p>
                    <button class="btn" id="vg-reset-filters-btn" style="margin-top: 15px;">Reset All Filters</button>
                </div>
            `;

            document.getElementById('vg-reset-filters-btn')?.addEventListener('click', resetFilters);
            return;
        }

        productGrid.innerHTML = filtered.map(product => `
            <div class="store-product-card" data-id="${product.id}">
                <div class="card-image-wrap">
                    <img src="${product.image}" alt="${product.name}" loading="lazy">
                    <span class="product-badge" style="background: ${product.badgeColor || 'var(--verdant-primary)'};">${product.badge}</span>
                    ${product.petFriendly ? '<span class="pet-friendly-tag" title="Pet Safe Foliage">🐾 Pet Safe</span>' : ''}
                    <button class="quick-view-btn" data-action="quickview" data-id="${product.id}">👁️ Quick View</button>
                </div>
                <div class="store-card-body">
                    <div class="card-care-meta">
                        <span>☀️ ${product.light.split('/')[0]}</span>
                        <span>💧 ${product.water}</span>
                    </div>
                    <h3 class="store-card-title">${product.name}</h3>
                    <p class="store-card-botanical">${product.botanicalName}</p>
                    <p class="store-card-desc">${product.description}</p>
                    
                    <div class="store-card-footer">
                        <div class="store-card-price">
                            <span class="price-val">${formatPrice(product.price)}</span>
                            <span class="price-size">${product.size}</span>
                        </div>
                        <button class="btn btn-add-cart" data-action="add-to-cart" data-id="${product.id}">
                            <span>+ Add to Cart</span>
                        </button>
                    </div>
                </div>
            </div>
        `).join('');
    }

    function resetFilters() {
        state.category = 'all';
        state.priceRange = 'all';
        state.careFilter = 'all';
        state.searchQuery = '';
        state.sortBy = 'price-desc';

        if (searchInput) searchInput.value = '';
        if (sortSelect) sortSelect.value = 'price-desc';

        categoryButtons.forEach(b => b.classList.toggle('active', b.dataset.category === 'all'));
        priceButtons.forEach(b => b.classList.toggle('active', b.dataset.price === 'all'));
        careButtons.forEach(b => b.classList.toggle('active', b.dataset.care === 'all'));

        renderCatalog();
    }

    // Quick View Modal
    function openQuickView(productId) {
        const product = getProductById(productId);
        if (!product) return;

        let modalRoot = document.getElementById('vg-quickview-root');
        if (!modalRoot) {
            modalRoot = document.createElement('div');
            modalRoot.id = 'vg-quickview-root';
            document.body.appendChild(modalRoot);
        }

        modalRoot.innerHTML = `
            <div id="vg-quickview-modal" class="vg-modal-overlay active">
                <div class="vg-modal-container vg-quickview-container">
                    <button class="vg-modal-close" onclick="document.getElementById('vg-quickview-modal').remove()">&times;</button>
                    <div class="quickview-grid">
                        <div class="quickview-img-col">
                            <img src="${product.image}" alt="${product.name}">
                            <span class="product-badge" style="background: ${product.badgeColor}; position: absolute; top: 15px; left: 15px;">${product.badge}</span>
                        </div>
                        <div class="quickview-details-col">
                            <span class="quickview-category">${product.category.toUpperCase()} COLLECTION</span>
                            <h2>${product.name}</h2>
                            <p class="quickview-botanical"><em>${product.botanicalName}</em></p>
                            
                            <div class="quickview-price-tag">
                                <strong>${formatPrice(product.price)}</strong>
                                <span class="quickview-size-badge">Potted Size: ${product.size}</span>
                            </div>

                            <p class="quickview-desc">${product.description}</p>

                            <div class="quickview-care-grid">
                                <div class="care-spec">
                                    <span class="spec-icon">☀️</span>
                                    <div>
                                        <strong>Light Requirement</strong>
                                        <p>${product.light}</p>
                                    </div>
                                </div>
                                <div class="care-spec">
                                    <span class="spec-icon">💧</span>
                                    <div>
                                        <strong>Watering Schedule</strong>
                                        <p>${product.water}</p>
                                    </div>
                                </div>
                                <div class="care-spec">
                                    <span class="spec-icon">🐾</span>
                                    <div>
                                        <strong>Pet Friendliness</strong>
                                        <p>${product.petFriendly ? 'Safe for Cats & Dogs' : 'Keep Away From Pets'}</p>
                                    </div>
                                </div>
                                <div class="care-spec">
                                    <span class="spec-icon">📍</span>
                                    <div>
                                        <strong>Acclimatization</strong>
                                        <p>100% Ndola Greenhouse Grown</p>
                                    </div>
                                </div>
                            </div>

                            ${product.tags ? `
                                <div class="quickview-tags-row">
                                    ${product.tags.map(t => `<span class="quickview-tag">#${t}</span>`).join(' ')}
                                </div>
                            ` : ''}

                            <div class="quickview-actions">
                                <button class="btn btn-full btn-add-cart" onclick="window.vgCart.addItem('${product.id}'); document.getElementById('vg-quickview-modal').remove();">
                                    🛒 Add to Cart • ${formatPrice(product.price)}
                                </button>
                                <a href="https://wa.me/26077597103?text=Hi%20Verdant%20Greens,%20I'm%20interested%20in%20ordering%20${encodeURIComponent(product.name)}%20(${formatPrice(product.price)})." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full" style="margin-top: 10px; display: flex; align-items: center; justify-content: center; gap: 8px;">
                                    💬 WhatsApp Inquire to +260 775 971 03
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    // Event Listeners
    // Search input listener with debouncing
    let searchTimeout;
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                state.searchQuery = e.target.value.trim();
                renderCatalog();
            }, 250);
        });
    }

    // Category button clicks
    categoryButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            categoryButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.category = btn.dataset.category;
            renderCatalog();
        });
    });

    // Price button clicks
    priceButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            priceButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.priceRange = btn.dataset.price;
            renderCatalog();
        });
    });

    // Care button clicks
    careButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            careButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.careFilter = btn.dataset.care;
            renderCatalog();
        });
    });

    // Sort select changes
    if (sortSelect) {
        sortSelect.addEventListener('change', (e) => {
            state.sortBy = e.target.value;
            renderCatalog();
        });
    }

    // Delegate grid clicks for Add-to-Cart and Quick View
    productGrid.addEventListener('click', (e) => {
        const addBtn = e.target.closest('[data-action="add-to-cart"]');
        if (addBtn) {
            const id = addBtn.dataset.id;
            if (window.vgCart) {
                window.vgCart.addItem(id);
            }
            return;
        }

        const quickBtn = e.target.closest('[data-action="quickview"]');
        if (quickBtn) {
            const id = quickBtn.dataset.id;
            openQuickView(id);
            return;
        }
    });

    // Initial Catalog Render
    renderCatalog();
});

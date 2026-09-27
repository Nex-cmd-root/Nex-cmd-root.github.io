/**
 * Verdant Greens - Shopping Cart & Checkout System
 * Handles localStorage persistence, Slide-out Cart Drawer,
 * Free Delivery calculations (Ndola >= K1,000), Toast Alerts,
 * and WhatsApp / Mobile Money Checkout Flows.
 */

const CART_STORAGE_KEY = 'verdant_greens_cart_v1';
const FREE_DELIVERY_THRESHOLD = 1000;
const STORE_PHONE_NUMBER = '26077597103';
const SUPPORT_PHONE_NUMBER = '260771594459';
const STORE_EMAIL = 'ash2herbal@gmail.com';

class ShoppingCart {
    constructor() {
        this.items = this.loadCart();
        this.init();
    }

    loadCart() {
        try {
            const data = localStorage.getItem(CART_STORAGE_KEY);
            return data ? JSON.parse(data) : [];
        } catch (e) {
            console.error('Failed to load cart from storage', e);
            return [];
        }
    }

    saveCart() {
        try {
            localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(this.items));
            this.updateBadge();
            this.renderDrawer();
        } catch (e) {
            console.error('Failed to save cart to storage', e);
        }
    }

    addItem(productId, qty = 1, showToastNotification = true) {
        const product = getProductById(productId);
        if (!product) return;

        const existing = this.items.find(item => item.id === productId);
        if (existing) {
            existing.qty += qty;
        } else {
            this.items.push({ id: productId, qty: qty });
        }

        this.saveCart();

        if (showToastNotification) {
            this.showToast(`🌿 Added <strong>${product.name}</strong> to your cart!`, true);
        }
    }

    removeItem(productId) {
        this.items = this.items.filter(item => item.id !== productId);
        this.saveCart();
    }

    updateQuantity(productId, newQty) {
        if (newQty <= 0) {
            this.removeItem(productId);
            return;
        }
        const item = this.items.find(i => i.id === productId);
        if (item) {
            item.qty = newQty;
            this.saveCart();
        }
    }

    clearCart() {
        this.items = [];
        this.saveCart();
    }

    getItemCount() {
        return this.items.reduce((sum, item) => sum + item.qty, 0);
    }

    getSubtotal() {
        return this.items.reduce((sum, item) => {
            const product = getProductById(item.id);
            return sum + (product ? product.price * item.qty : 0);
        }, 0);
    }

    init() {
        this.injectUIElements();
        this.updateBadge();
        this.bindEvents();
    }

    injectUIElements() {
        // Create Drawer & Modals if not already present in DOM
        if (!document.getElementById('vg-cart-drawer')) {
            const drawerHTML = `
                <!-- Cart Overlay -->
                <div id="vg-cart-overlay" class="vg-overlay"></div>
                
                <!-- Cart Drawer -->
                <div id="vg-cart-drawer" class="vg-cart-drawer" aria-hidden="true">
                    <div class="vg-cart-header">
                        <div class="vg-cart-title">
                            <h3>🌿 Your Botanical Cart</h3>
                            <span class="vg-cart-subtitle"><span id="vg-drawer-item-count">0</span> items selected</span>
                        </div>
                        <button id="vg-close-cart-btn" class="vg-close-btn" aria-label="Close cart">&times;</button>
                    </div>

                    <!-- Free Delivery Progress Tracker -->
                    <div class="vg-delivery-tracker" id="vg-delivery-tracker">
                        <div class="vg-tracker-text" id="vg-tracker-text">
                            <span>Add K1,000 for Free Delivery in Ndola</span>
                        </div>
                        <div class="vg-tracker-bar">
                            <div class="vg-tracker-progress" id="vg-tracker-progress" style="width: 0%;"></div>
                        </div>
                    </div>

                    <!-- Cart Item List -->
                    <div class="vg-cart-items" id="vg-cart-items">
                        <!-- Populated by JS -->
                    </div>

                    <!-- Cart Footer -->
                    <div class="vg-cart-footer" id="vg-cart-footer">
                        <div class="vg-cart-summary">
                            <div class="vg-summary-row">
                                <span>Subtotal:</span>
                                <strong id="vg-cart-subtotal">K0</strong>
                            </div>
                            <div class="vg-summary-row delivery-row">
                                <span>Ndola Delivery:</span>
                                <span id="vg-delivery-status" class="vg-delivery-badge">Free over K1,000</span>
                            </div>
                        </div>

                        <div class="vg-cart-actions">
                            <button id="vg-checkout-whatsapp-btn" class="btn btn-whatsapp">
                                <span>💬 Order via WhatsApp</span>
                            </button>
                            <button id="vg-checkout-momo-btn" class="btn btn-momo">
                                <span>📱 Mobile Money / Direct Pay</span>
                            </button>
                            <button id="vg-continue-shopping-btn" class="btn btn-secondary btn-full">
                                Continue Browsing Catalog
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Checkout & Mobile Money Modal -->
                <div id="vg-checkout-modal" class="vg-modal-overlay">
                    <div class="vg-modal-container">
                        <button id="vg-close-modal-btn" class="vg-modal-close">&times;</button>
                        <div class="vg-modal-content" id="vg-modal-body">
                            <!-- Populated on open -->
                        </div>
                    </div>
                </div>

                <!-- Toast Notification Container -->
                <div id="vg-toast-container" class="vg-toast-container"></div>
            `;

            const container = document.createElement('div');
            container.id = 'vg-cart-root';
            container.innerHTML = drawerHTML;
            document.body.appendChild(container);
        }
    }

    bindEvents() {
        // Toggle cart drawer on any element with [data-action="open-cart"] or .cart-trigger
        document.addEventListener('click', (e) => {
            const trigger = e.target.closest('[data-action="open-cart"], .cart-trigger');
            if (trigger) {
                e.preventDefault();
                this.openDrawer();
            }

            // Close drawer buttons
            if (e.target.closest('#vg-close-cart-btn') || e.target.closest('#vg-cart-overlay') || e.target.closest('#vg-continue-shopping-btn')) {
                this.closeDrawer();
            }

            // Quantity stepper buttons inside drawer
            const qtyBtn = e.target.closest('.vg-qty-btn');
            if (qtyBtn) {
                const id = qtyBtn.dataset.id;
                const change = parseInt(qtyBtn.dataset.change, 10);
                const currentItem = this.items.find(i => i.id === id);
                if (currentItem) {
                    this.updateQuantity(id, currentItem.qty + change);
                }
            }

            // Remove button
            const removeBtn = e.target.closest('.vg-remove-item-btn');
            if (removeBtn) {
                const id = removeBtn.dataset.id;
                this.removeItem(id);
            }

            // WhatsApp Checkout
            if (e.target.closest('#vg-checkout-whatsapp-btn')) {
                this.openCheckoutModal('whatsapp');
            }

            // Mobile Money Checkout
            if (e.target.closest('#vg-checkout-momo-btn')) {
                this.openCheckoutModal('momo');
            }

            // Modal Close
            if (e.target.closest('#vg-close-modal-btn') || e.target.id === 'vg-checkout-modal') {
                this.closeCheckoutModal();
            }
        });

        // Listen for ESC key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeDrawer();
                this.closeCheckoutModal();
            }
        });
    }

    updateBadge() {
        const count = this.getItemCount();
        const badges = document.querySelectorAll('.cart-count-badge');
        badges.forEach(b => {
            b.textContent = count;
            b.style.display = count > 0 ? 'inline-flex' : 'none';
        });

        const drawerCount = document.getElementById('vg-drawer-item-count');
        if (drawerCount) drawerCount.textContent = count;
    }

    renderDrawer() {
        const itemsContainer = document.getElementById('vg-cart-items');
        const subtotalEl = document.getElementById('vg-cart-subtotal');
        const trackerText = document.getElementById('vg-tracker-text');
        const trackerProgress = document.getElementById('vg-tracker-progress');
        const deliveryStatus = document.getElementById('vg-delivery-status');
        const cartFooter = document.getElementById('vg-cart-footer');

        if (!itemsContainer) return;

        const subtotal = this.getSubtotal();
        const count = this.getItemCount();

        // Update Subtotal
        if (subtotalEl) subtotalEl.textContent = formatPrice(subtotal);

        // Update Free Delivery Tracker
        if (trackerText && trackerProgress) {
            if (subtotal >= FREE_DELIVERY_THRESHOLD) {
                trackerText.innerHTML = `🎉 <strong>Free Delivery Unlocked</strong> for Ndola!`;
                trackerProgress.style.width = '100%';
                trackerProgress.style.backgroundColor = 'var(--verdant-accent)';
                if (deliveryStatus) {
                    deliveryStatus.textContent = 'FREE 🎉';
                    deliveryStatus.classList.add('free');
                }
            } else {
                const needed = FREE_DELIVERY_THRESHOLD - subtotal;
                const pct = Math.min(100, Math.round((subtotal / FREE_DELIVERY_THRESHOLD) * 100));
                trackerText.innerHTML = `Add <strong>K${needed.toLocaleString()}</strong> more to get <strong>Free Ndola Delivery</strong>`;
                trackerProgress.style.width = `${pct}%`;
                trackerProgress.style.backgroundColor = 'var(--cerulean-accent)';
                if (deliveryStatus) {
                    deliveryStatus.textContent = 'Free over K1,000';
                    deliveryStatus.classList.remove('free');
                }
            }
        }

        // Empty Cart State
        if (this.items.length === 0) {
            itemsContainer.innerHTML = `
                <div class="vg-cart-empty">
                    <div class="vg-empty-icon">🪴</div>
                    <h4>Your Botanical Cart is Empty</h4>
                    <p>Discover healthy, greenhouse-acclimatized plants to bring life to your home.</p>
                    <a href="shop.html" class="btn" style="margin-top: 15px;">Explore Store & Prices →</a>
                </div>
            `;
            if (cartFooter) cartFooter.style.display = 'none';
            return;
        }

        if (cartFooter) cartFooter.style.display = 'block';

        // Render Item rows
        itemsContainer.innerHTML = this.items.map(item => {
            const product = getProductById(item.id);
            if (!product) return '';

            const itemTotal = product.price * item.qty;

            return `
                <div class="vg-cart-item" data-id="${product.id}">
                    <img src="${product.image}" alt="${product.name}" class="vg-cart-item-img">
                    <div class="vg-cart-item-info">
                        <div class="vg-cart-item-top">
                            <h4 class="vg-cart-item-name">${product.name}</h4>
                            <button class="vg-remove-item-btn" data-id="${product.id}" title="Remove plant">&times;</button>
                        </div>
                        <span class="vg-cart-item-category">${product.botanicalName}</span>
                        <div class="vg-cart-item-price-row">
                            <div class="vg-qty-stepper">
                                <button class="vg-qty-btn" data-id="${product.id}" data-change="-1" aria-label="Decrease quantity">−</button>
                                <span class="vg-qty-val">${item.qty}</span>
                                <button class="vg-qty-btn" data-id="${product.id}" data-change="1" aria-label="Increase quantity">+</button>
                            </div>
                            <strong class="vg-cart-item-total">${formatPrice(itemTotal)}</strong>
                        </div>
                    </div>
                </div>
            `;
        }).join('');
    }

    openDrawer() {
        this.renderDrawer();
        const drawer = document.getElementById('vg-cart-drawer');
        const overlay = document.getElementById('vg-cart-overlay');
        if (drawer) {
            drawer.classList.add('active');
            drawer.setAttribute('aria-hidden', 'false');
        }
        if (overlay) overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    closeDrawer() {
        const drawer = document.getElementById('vg-cart-drawer');
        const overlay = document.getElementById('vg-cart-overlay');
        if (drawer) {
            drawer.classList.remove('active');
            drawer.setAttribute('aria-hidden', 'true');
        }
        if (overlay) overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    openCheckoutModal(flow = 'whatsapp') {
        const modal = document.getElementById('vg-checkout-modal');
        const body = document.getElementById('vg-modal-body');
        if (!modal || !body) return;

        const subtotal = this.getSubtotal();
        const isFreeDelivery = subtotal >= FREE_DELIVERY_THRESHOLD;

        body.innerHTML = `
            <div class="vg-checkout-container">
                <div class="vg-checkout-header">
                    <h2>🌿 Complete Your Plant Order</h2>
                    <p>Fast delivery direct from our Ndola greenhouse across Zambia.</p>
                </div>

                <div class="vg-checkout-tabs">
                    <button class="vg-tab-btn ${flow === 'whatsapp' ? 'active' : ''}" onclick="window.vgCart.switchTab('whatsapp')">💬 WhatsApp 1-Click</button>
                    <button class="vg-tab-btn ${flow === 'momo' ? 'active' : ''}" onclick="window.vgCart.switchTab('momo')">📱 Mobile Money & Bank</button>
                </div>

                <!-- WhatsApp Order Tab -->
                <div id="vg-tab-whatsapp" class="vg-tab-content ${flow === 'whatsapp' ? 'active' : ''}">
                    <p class="vg-tab-desc">Submit your order directly to our team via WhatsApp. We will confirm your delivery address and dispatch schedule immediately.</p>
                    
                    <form id="vg-whatsapp-form" onsubmit="window.vgCart.submitWhatsAppOrder(event)">
                        <div class="form-group">
                            <label for="cust-name">Your Full Name *</label>
                            <input type="text" id="cust-name" required placeholder="e.g., Mwamba Chanda" class="vg-input">
                        </div>
                        <div class="form-group">
                            <label for="cust-phone">WhatsApp / Phone Number *</label>
                            <input type="tel" id="cust-phone" required placeholder="e.g., 0977 123 456" class="vg-input">
                        </div>
                        <div class="form-group">
                            <label for="cust-address">Delivery Address / Town in Zambia *</label>
                            <input type="text" id="cust-address" required placeholder="e.g., Kansenshi, Ndola or Kitwe / Lusaka" class="vg-input">
                        </div>
                        <div class="form-group">
                            <label for="cust-payment">Preferred Payment Method</label>
                            <select id="cust-payment" class="vg-input">
                                <option value="Airtel Money">Airtel Money</option>
                                <option value="MTN Mobile Money">MTN MoMo</option>
                                <option value="Zamtel Kwacha">Zamtel Kwacha</option>
                                <option value="Cash on Delivery (Ndola only)">Cash on Delivery (Ndola only)</option>
                                <option value="Bank Transfer">Bank Transfer (FNB / Stanbic)</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="cust-notes">Order Notes / Pot Preferences (Optional)</label>
                            <textarea id="cust-notes" rows="2" placeholder="Any special requests or delivery instructions..." class="vg-input"></textarea>
                        </div>

                        <div class="vg-order-review-box">
                            <div class="review-line"><span>Order Total:</span> <strong>${formatPrice(subtotal)}</strong></div>
                            <div class="review-line"><span>Delivery:</span> <span>${isFreeDelivery ? 'FREE (Ndola Promo)' : 'Standard Regional Rate'}</span></div>
                        </div>

                        <button type="submit" class="btn btn-whatsapp btn-full" style="padding: 14px; font-size: 1.05rem; margin-top: 15px;">
                            🚀 Send Order to +260 775 971 03 via WhatsApp
                        </button>
                    </form>
                </div>

                <!-- Mobile Money Tab -->
                <div id="vg-tab-momo" class="vg-tab-content ${flow === 'momo' ? 'active' : ''}">
                    <div class="vg-momo-instructions">
                        <h4>📱 Pay via Airtel Money / MTN MoMo</h4>
                        <p>Follow the simple steps below to transfer your payment directly to Verdant Greens (Strict Transaction Line):</p>

                        <div class="momo-steps-card">
                            <div class="momo-line">
                                <span>1. Recipient Number:</span>
                                <strong class="highlight-number">+260 775 971 03 / 0977597103</strong>
                            </div>
                            <div class="momo-line">
                                <span>2. Account Name:</span>
                                <strong>Verdant Greens / Botanical Care</strong>
                            </div>
                            <div class="momo-line">
                                <span>3. Exact Amount:</span>
                                <strong class="highlight-amount">${formatPrice(subtotal)}</strong>
                            </div>
                            <div class="momo-line">
                                <span>4. Reference / Reason:</span>
                                <strong>VG-PLANTS</strong>
                            </div>
                        </div>

                        <h4 style="margin-top: 20px;">Confirm Payment & Email Receipt</h4>
                        <p class="small-text">Once sent, enter your transaction reference below. We will email an official receipt and arrange delivery dispatch.</p>

                        <form id="vg-momo-form" onsubmit="window.vgCart.submitMomoConfirmation(event)">
                            <div class="form-group">
                                <label for="momo-name">Your Full Name *</label>
                                <input type="text" id="momo-name" required placeholder="e.g., Mwamba Chanda" class="vg-input">
                            </div>
                            <div class="form-group">
                                <label for="momo-email">Your Email Address *</label>
                                <input type="email" id="momo-email" required placeholder="name@example.com" class="vg-input">
                            </div>
                            <div class="form-group">
                                <label for="momo-ref">Mobile Money Transaction ID / Reference *</label>
                                <input type="text" id="momo-ref" required placeholder="e.g., MP260830.1234.A0012" class="vg-input">
                            </div>
                            <div class="form-group">
                                <label for="momo-address">Delivery Location in Ndola / Zambia *</label>
                                <input type="text" id="momo-address" required placeholder="e.g., Itawa, Ndola" class="vg-input">
                            </div>

                            <button type="submit" class="btn btn-momo btn-full" style="padding: 14px; font-size: 1.05rem; margin-top: 15px;">
                                ✉️ Confirm Payment & Notify Greenhouse Team
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        `;

        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    switchTab(tab) {
        document.querySelectorAll('.vg-tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.vg-tab-content').forEach(c => c.classList.remove('active'));

        if (tab === 'whatsapp') {
            document.querySelector('.vg-tab-btn:nth-child(1)').classList.add('active');
            document.getElementById('vg-tab-whatsapp').classList.add('active');
        } else {
            document.querySelector('.vg-tab-btn:nth-child(2)').classList.add('active');
            document.getElementById('vg-tab-momo').classList.add('active');
        }
    }

    closeCheckoutModal() {
        const modal = document.getElementById('vg-checkout-modal');
        if (modal) modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    submitWhatsAppOrder(e) {
        e.preventDefault();
        const name = document.getElementById('cust-name').value;
        const phone = document.getElementById('cust-phone').value;
        const address = document.getElementById('cust-address').value;
        const payment = document.getElementById('cust-payment').value;
        const notes = document.getElementById('cust-notes').value;

        const subtotal = this.getSubtotal();
        const deliveryNote = subtotal >= FREE_DELIVERY_THRESHOLD ? 'FREE Ndola Delivery' : 'Standard Delivery Rate applies';

        let message = `*🌿 NEW ORDER - VERDANT GREENS*\n`;
        message += `---------------------------------\n`;
        message += `*Customer:* ${name}\n`;
        message += `*Phone:* ${phone}\n`;
        message += `*Delivery Address:* ${address}\n`;
        message += `*Payment Preference:* ${payment}\n`;
        if (notes) message += `*Notes:* ${notes}\n`;
        message += `---------------------------------\n`;
        message += `*ORDERED PLANTS:*\n`;

        this.items.forEach((item, index) => {
            const product = getProductById(item.id);
            if (product) {
                message += `${index + 1}. ${product.name} (x${item.qty}) - ${formatPrice(product.price * item.qty)}\n`;
            }
        });

        message += `---------------------------------\n`;
        message += `*Subtotal:* ${formatPrice(subtotal)}\n`;
        message += `*Delivery:* ${deliveryNote}\n`;
        message += `---------------------------------\n`;
        message += `Please confirm my order and send payment/delivery details. Thank you!`;

        const encoded = encodeURIComponent(message);
        const waUrl = `https://wa.me/${STORE_PHONE_NUMBER}?text=${encoded}`;

        // Clear cart or keep until verified? Keep or clear on success
        this.showToast('🌿 Redirecting to WhatsApp with your order summary...', true);
        
        setTimeout(() => {
            window.open(waUrl, '_blank');
            this.closeCheckoutModal();
            this.closeDrawer();
        }, 800);
    }

    submitMomoConfirmation(e) {
        e.preventDefault();
        const name = document.getElementById('momo-name').value;
        const email = document.getElementById('momo-email').value;
        const ref = document.getElementById('momo-ref').value;
        const address = document.getElementById('momo-address').value;

        const subtotal = this.getSubtotal();

        // Prepare email mailto fallback or mail log notification
        let emailSubject = encodeURIComponent(`Verdant Greens Order Confirmation - Ref: ${ref} (${name})`);
        let emailBody = encodeURIComponent(
            `Hi Verdant Greens Team,\n\n` +
            `I have submitted a Mobile Money payment for my plant order.\n\n` +
            `Transaction Reference: ${ref}\n` +
            `Customer Name: ${name}\n` +
            `Contact Email: ${email}\n` +
            `Delivery Address: ${address}\n` +
            `Amount Paid: ${formatPrice(subtotal)}\n\n` +
            `Ordered Items:\n` +
            this.items.map(i => {
                const p = getProductById(i.id);
                return `- ${p ? p.name : i.id} x ${i.qty}`;
            }).join('\n') +
            `\n\nPlease verify and schedule dispatch.\n`
        );

        const mailtoUrl = `mailto:${STORE_EMAIL}?cc=${encodeURIComponent(email)}&subject=${emailSubject}&body=${emailBody}`;

        const body = document.getElementById('vg-modal-body');
        if (body) {
            body.innerHTML = `
                <div class="vg-success-box">
                    <div class="success-icon">✅</div>
                    <h3>Payment Logged Successfully!</h3>
                    <p>Thank you, <strong>${name}</strong>! Your Mobile Money reference <code>${ref}</code> has been recorded.</p>
                    <p class="small-text">A dispatch notification is being prepared for <strong>${STORE_EMAIL}</strong>.</p>
                    <div style="margin: 20px 0;">
                        <a href="${mailtoUrl}" class="btn btn-momo btn-full">📧 Open Email Client to Send Receipt Copy</a>
                    </div>
                    <button class="btn btn-secondary btn-full" onclick="window.vgCart.closeCheckoutModal(); window.vgCart.clearCart();">
                        Done & Clear Cart
                    </button>
                </div>
            `;
        }
    }

    showToast(message, isHTML = false) {
        const container = document.getElementById('vg-toast-container');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = 'vg-toast';
        if (isHTML) {
            toast.innerHTML = `
                <div class="toast-content">${message}</div>
                <button class="toast-action-btn" onclick="window.vgCart.openDrawer()">View Cart</button>
            `;
        } else {
            toast.textContent = message;
        }

        container.appendChild(toast);

        // Animate in
        setTimeout(() => toast.classList.add('visible'), 10);

        // Auto remove
        setTimeout(() => {
            toast.classList.remove('visible');
            setTimeout(() => toast.remove(), 400);
        }, 4000);
    }
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    window.vgCart = new ShoppingCart();
});


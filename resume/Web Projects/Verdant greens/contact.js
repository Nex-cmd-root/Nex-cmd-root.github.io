/**
 * Verdant Greens - Contact & Customer Email Logger Controller (contact.js)
 * Manages form submissions, local lead & email persistence,
 * CSV/JSON export for nursery management, and direct WhatsApp routing.
 */

const INQUIRIES_STORAGE_KEY = 'verdant_greens_inquiries_v1';
const TRANSACTION_PHONE = '26077597103';
const SUPPORT_PHONE = '260771594459';
const STORE_EMAIL = 'ash2herbal@gmail.com';

class ContactManager {
    constructor() {
        this.inquiries = this.loadInquiries();
        this.init();
    }

    loadInquiries() {
        try {
            const data = localStorage.getItem(INQUIRIES_STORAGE_KEY);
            return data ? JSON.parse(data) : [];
        } catch (e) {
            console.error('Failed to load inquiries from storage', e);
            return [];
        }
    }

    saveInquiries() {
        try {
            localStorage.setItem(INQUIRIES_STORAGE_KEY, JSON.stringify(this.inquiries));
            this.updateAdminLeadBadge();
        } catch (e) {
            console.error('Failed to save inquiry to storage', e);
        }
    }

    addInquiry(data) {
        const entry = {
            id: 'inq_' + Date.now(),
            date: new Date().toISOString(),
            dateFormatted: new Date().toLocaleString('en-GB', {
                day: 'numeric',
                month: 'short',
                year: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            }),
            name: data.name.trim(),
            email: data.email.trim(),
            phone: (data.phone || '').trim(),
            topic: data.topic || 'General Inquiry',
            plantInterest: data.plantInterest || 'Not Specified',
            message: data.message.trim(),
            newsletter: Boolean(data.newsletter)
        };

        this.inquiries.unshift(entry);
        this.saveInquiries();
        return entry;
    }

    deleteInquiry(id) {
        this.inquiries = this.inquiries.filter(inq => inq.id !== id);
        this.saveInquiries();
        this.renderAdminModal();
    }

    clearAllInquiries() {
        if (confirm('Are you sure you want to clear all stored customer leads? This cannot be undone.')) {
            this.inquiries = [];
            this.saveInquiries();
            this.renderAdminModal();
        }
    }

    exportToCSV() {
        if (this.inquiries.length === 0) {
            alert('No customer inquiries logged yet to export.');
            return;
        }

        const headers = ['ID', 'Date', 'Full Name', 'Email Address', 'Phone / WhatsApp', 'Inquiry Topic', 'Plant Interest', 'Message', 'Subscribed to Tips'];
        const rows = this.inquiries.map(inq => [
            inq.id,
            `"${inq.dateFormatted}"`,
            `"${(inq.name || '').replace(/"/g, '""')}"`,
            `"${(inq.email || '').replace(/"/g, '""')}"`,
            `"${(inq.phone || '').replace(/"/g, '""')}"`,
            `"${(inq.topic || '').replace(/"/g, '""')}"`,
            `"${(inq.plantInterest || '').replace(/"/g, '""')}"`,
            `"${(inq.message || '').replace(/"/g, '""')}"`,
            inq.newsletter ? 'YES' : 'NO'
        ]);

        const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\r\n');
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', `verdant-greens-leads-${new Date().toISOString().slice(0, 10)}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    exportToJSON() {
        if (this.inquiries.length === 0) {
            alert('No customer inquiries logged yet to export.');
            return;
        }
        const jsonContent = JSON.stringify(this.inquiries, null, 2);
        const blob = new Blob([jsonContent], { type: 'application/json;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', `verdant-greens-leads-${new Date().toISOString().slice(0, 10)}.json`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    updateAdminLeadBadge() {
        const badges = document.querySelectorAll('.vg-admin-leads-count');
        badges.forEach(b => {
            b.textContent = this.inquiries.length;
            b.style.display = this.inquiries.length > 0 ? 'inline-flex' : 'none';
        });
    }

    init() {
        this.bindForm();
        this.bindAdminModal();
        this.updateAdminLeadBadge();
    }

    bindForm() {
        const form = document.getElementById('vg-contact-form');
        if (!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = form.querySelector('#vg-name')?.value || '';
            const email = form.querySelector('#vg-email')?.value || '';
            const phone = form.querySelector('#vg-phone')?.value || '';
            const topic = form.querySelector('#vg-topic')?.value || '';
            const plantInterest = form.querySelector('#vg-plant-interest')?.value || '';
            const message = form.querySelector('#vg-message')?.value || '';
            const newsletter = form.querySelector('#vg-newsletter')?.checked || false;

            if (!name.trim() || !email.trim() || !message.trim()) {
                alert('Please fill in your name, email address, and message.');
                return;
            }

            // Save inquiry
            const savedInquiry = this.addInquiry({
                name, email, phone, topic, plantInterest, message, newsletter
            });

            // Show confirmation UI
            const formContainer = document.getElementById('vg-contact-form-container');
            if (formContainer) {
                const isOrder = topic.toLowerCase().includes('order') || topic.toLowerCase().includes('price');
                const targetPhone = isOrder ? TRANSACTION_PHONE : SUPPORT_PHONE;
                const phoneLabel = isOrder ? '+260 775 971 03 (Transactions)' : '+260 771 594 459 (Support)';
                const waText = encodeURIComponent(`Hi Verdant Greens,\nMy Name: ${name}\nEmail: ${email}\nTopic: ${topic}\nMessage: ${message}`);
                const waUrl = `https://wa.me/${targetPhone}?text=${waText}`;

                formContainer.innerHTML = `
                    <div class="contact-success-card">
                        <div class="success-icon-badge">🌿</div>
                        <h3>Message Successfully Received!</h3>
                        <p>Thank you <strong>${name}</strong>! Your inquiry and email (<em>${email}</em>) have been logged with our Ndola botanical nursery team.</p>
                        
                        <div class="success-actions-box">
                            <p>Need an instant response right now?</p>
                            <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="display:inline-flex; align-items:center; gap:8px;">
                                <span>💬 Continue via WhatsApp to ${phoneLabel}</span>
                            </a>
                        </div>

                        <div style="margin-top: 25px;">
                            <button class="btn btn-secondary" onclick="window.location.reload()">Send Another Message</button>
                        </div>
                    </div>
                `;
            }
        });
    }

    bindAdminModal() {
        const triggers = document.querySelectorAll('[data-action="open-leads-admin"]');
        triggers.forEach(t => {
            t.addEventListener('click', (e) => {
                e.preventDefault();
                this.openAdminModal();
            });
        });
    }

    openAdminModal() {
        let modal = document.getElementById('vg-leads-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'vg-leads-modal';
            modal.className = 'vg-modal-overlay';
            document.body.appendChild(modal);
        }

        modal.classList.add('active');
        this.renderAdminModal();
    }

    closeAdminModal() {
        const modal = document.getElementById('vg-leads-modal');
        if (modal) modal.classList.remove('active');
    }

    renderAdminModal() {
        const modal = document.getElementById('vg-leads-modal');
        if (!modal) return;

        modal.innerHTML = `
            <div class="vg-modal-container vg-leads-container">
                <button class="vg-modal-close" onclick="window.vgContact.closeAdminModal()">&times;</button>
                <div class="leads-modal-header">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-size:1.8rem;">📋</span>
                        <div>
                            <h2>Customer Inquiries & Email Logger</h2>
                            <p style="color:var(--text-muted); font-size:0.88rem;">Logged customer leads saved in this browser for nursery management.</p>
                        </div>
                    </div>
                    <div class="leads-header-actions">
                        <button class="btn btn-sm" onclick="window.vgContact.exportToCSV()">📥 Export CSV</button>
                        <button class="btn btn-sm btn-secondary" onclick="window.vgContact.exportToJSON()">📥 Export JSON</button>
                        ${this.inquiries.length > 0 ? '<button class="btn btn-sm btn-danger" onclick="window.vgContact.clearAllInquiries()">🗑️ Clear All</button>' : ''}
                    </div>
                </div>

                <div class="leads-modal-body">
                    ${this.inquiries.length === 0 ? `
                        <div class="vg-empty-leads">
                            <span>🌱</span>
                            <h4>No customer inquiries recorded yet</h4>
                            <p>When visitors submit the contact form, their contact details and emails will appear here.</p>
                        </div>
                    ` : `
                        <div class="leads-table-wrapper">
                            <table class="leads-table">
                                <thead>
                                    <tr>
                                        <th>Date</th>
                                        <th>Customer</th>
                                        <th>Phone / WhatsApp</th>
                                        <th>Topic</th>
                                        <th>Message</th>
                                        <th>Tips Subscribed</th>
                                        <th>Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    ${this.inquiries.map(inq => `
                                        <tr>
                                            <td style="white-space:nowrap; font-size:0.82rem; color:var(--text-muted);">${inq.dateFormatted}</td>
                                            <td>
                                                <strong>${inq.name}</strong><br>
                                                <a href="mailto:${inq.email}" style="color:var(--verdant-primary); font-size:0.85rem;">${inq.email}</a>
                                            </td>
                                            <td style="white-space:nowrap; font-size:0.88rem;">${inq.phone || '<em style="color:var(--text-muted)">None</em>'}</td>
                                            <td><span class="lead-topic-tag">${inq.topic}</span></td>
                                            <td class="lead-msg-cell" title="${inq.message}">${inq.message}</td>
                                            <td style="text-align:center;">${inq.newsletter ? '✅ Yes' : '—'}</td>
                                            <td>
                                                <button class="lead-del-btn" onclick="window.vgContact.deleteInquiry('${inq.id}')" title="Delete lead">&times;</button>
                                            </td>
                                        </tr>
                                    `).join('')}
                                </tbody>
                            </table>
                        </div>
                    `}
                </div>
                <div class="leads-modal-footer">
                    <span>Total Recorded Leads: <strong>${this.inquiries.length}</strong></span>
                    <span style="color:var(--text-muted); font-size:0.82rem;">Verdant Greens Ndola • ash2herbal@gmail.com</span>
                </div>
            </div>
        `;
    }
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    window.vgContact = new ContactManager();
});

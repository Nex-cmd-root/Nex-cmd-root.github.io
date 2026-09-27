document.addEventListener('DOMContentLoaded', () => {

    // 1. Dark / Light Theme Switching
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');

    if (localStorage.getItem('portfolio-theme') === 'light') {
        document.body.classList.add('light-mode');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }

    themeToggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');

        if (document.body.classList.contains('light-mode')) {
            themeIcon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('portfolio-theme', 'light');
        } else {
            themeIcon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('portfolio-theme', 'dark');
        }
    });

    // 2. Interactive Skills Filtering
    const filterButtons = document.querySelectorAll('.filter-btn');
    const skillCards = document.querySelectorAll('.skill-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Update active state on filter buttons
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            });
            button.classList.add('active');
            button.setAttribute('aria-pressed', 'true');

            const filterValue = button.getAttribute('data-filter');

            skillCards.forEach(card => {
                if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // 3. Accordion Interaction for Domain Experience
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach((header, index) => {
        const content = header.nextElementSibling;
        const contentId = `capability-${index + 1}`;

        header.type = 'button';
        header.setAttribute('aria-controls', contentId);
        header.setAttribute('aria-expanded', 'false');
        content.id = contentId;
        content.setAttribute('aria-hidden', 'true');

        header.addEventListener('click', () => {
            const accordionItem = header.parentElement;
            const isActive = accordionItem.classList.contains('active');

            // Close all active accordion items
            document.querySelectorAll('.accordion-item').forEach(item => {
                item.classList.remove('active');
                item.querySelector('.accordion-header').setAttribute('aria-expanded', 'false');
                item.querySelector('.accordion-content').setAttribute('aria-hidden', 'true');
            });

            // Toggle selected item
            if (!isActive) {
                accordionItem.classList.add('active');
                header.setAttribute('aria-expanded', 'true');
                content.setAttribute('aria-hidden', 'false');
            }
        });
    });

    // Expand the first domain by default
    if (accordionHeaders.length > 0) {
        accordionHeaders[0].parentElement.classList.add('active');
        accordionHeaders[0].setAttribute('aria-expanded', 'true');
        accordionHeaders[0].nextElementSibling.setAttribute('aria-hidden', 'false');
    }

    const proposalForm = document.getElementById('proposal-form');
    if (proposalForm) {
        const proposalType = document.getElementById('proposal-type');
        const proposalDetails = document.getElementById('proposal-details');
        const proposalStatus = document.getElementById('proposal-status');

        document.getElementById('proposal-template').addEventListener('click', () => {
            const selectedType = proposalType.options[proposalType.selectedIndex].text;
            proposalDetails.value = `Hello,\n\nI'd like to discuss ${selectedType.toLowerCase()}.\n\nProject goal:\n\nKey requirements:\n\nPreferred next step:`;
            proposalDetails.focus();
        });

        const buildProposal = () => {
            const subject = `Project proposal: ${proposalType.options[proposalType.selectedIndex].text}`;
            const message = [
                `Name: ${document.getElementById('proposal-name').value}`,
                `Email: ${document.getElementById('proposal-email').value}`,
                `Project type: ${proposalType.options[proposalType.selectedIndex].text}`,
                `Timeline: ${document.getElementById('proposal-timeline').value || 'To be discussed'}`,
                '',
                'Project details:',
                proposalDetails.value
            ].join('\n');

            return { subject, message };
        };

        proposalForm.addEventListener('submit', event => {
            event.preventDefault();
            const proposal = buildProposal();
            const mailto = `mailto:nayt.bus@gmail.com?subject=${encodeURIComponent(proposal.subject)}&body=${encodeURIComponent(proposal.message)}`;
            window.location.href = mailto;
            proposalStatus.textContent = 'Your email app should open with the proposal draft. The message has not been sent yet.';
        });

        document.getElementById('copy-proposal').addEventListener('click', async () => {
            const proposal = buildProposal();
            try {
                await navigator.clipboard.writeText(`${proposal.subject}\n\n${proposal.message}`);
                proposalStatus.textContent = 'Proposal copied to clipboard.';
            } catch {
                proposalStatus.textContent = 'Clipboard access is unavailable here. Use Prepare Email to open the draft in your email app.';
            }
        });
    }
});
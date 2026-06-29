document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function() {
            const expanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !expanded);
        });

        document.addEventListener('click', function(e) {
            if (!mainNav.contains(e.target) && !menuToggle.contains(e.target)) {
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    const affiliateLinks = document.querySelectorAll('[data-affiliate]');
    affiliateLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            if (typeof gtag === 'function') {
                gtag('event', 'affiliate_click', {
                    'event_category': 'affiliate',
                    'event_label': this.getAttribute('data-affiliate'),
                    'value': 1
                });
            }
        });
    });

    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(function(item) {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        if (question && answer) {
            answer.style.display = 'none';
            question.style.cursor = 'pointer';
            question.addEventListener('click', function() {
                const isVisible = answer.style.display === 'block';
                answer.style.display = isVisible ? 'none' : 'block';
            });
        }
    });
});

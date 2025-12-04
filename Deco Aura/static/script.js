document.addEventListener('DOMContentLoaded', () => {
    // Add subtle animation to cards on load
    const cards = document.querySelectorAll('.option-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.4s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 50); // Faster stagger
    });

    // Save button interaction (mock)
    const saveBtns = document.querySelectorAll('.save-btn');
    saveBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fas fa-check"></i> Saved';
            btn.style.background = '#333';
            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.style.background = '#e60023';
            }, 2000);
        });
    });
});

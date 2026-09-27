/**
 * Verdant Greens - Care Guide Controller (care.js)
 * Manages interactive Plant Symptom Checker, plant profile search,
 * and seasonal care accordion tabs.
 */

const SYMPTOMS_DATA = {
    yellow: {
        title: '🍂 Yellowing Leaves',
        icon: '🍂',
        cause: 'Overwatering or Poor Drainage (#1 cause in Zambia)',
        diagnosis: 'When roots sit in waterlogged soil without oxygen, they begin to suffocate and rot, preventing nutrients from reaching the leaves.',
        solution: 'Allow the top 2 inches of soil to completely dry before watering again. Ensure your decorative pot has drainage holes at the bottom.',
        prevention: 'Always do the finger test: if soil feels moist, wait 3-4 days before checking again.'
    },
    brown_tips: {
        title: '🥀 Brown, Crispy Leaf Tips',
        icon: '🥀',
        cause: 'Low Humidity, Underwatering, or Tap Water Mineral Build-up',
        diagnosis: 'Dry indoor air or irregular watering cycles cause the delicate leaf tips to lose moisture faster than roots can supply it.',
        solution: 'Mist foliage in the morning with a spray bottle, group plants together to create a micro-climate, or place a pebble tray filled with water under the pot.',
        prevention: 'Avoid placing plants directly next to dry air conditioning vents or direct afternoon scorching sun.'
    },
    drooping: {
        title: '🌿 Drooping or Limp Stems',
        icon: '🌿',
        cause: 'Underwatering (Thirsty) OR Severe Root Rot',
        diagnosis: 'Check the soil: if bone-dry and pulling away from the pot edge, it is thirsty. If soggy wet and drooping, roots are compromised.',
        solution: 'For dry soil: Give a thorough bottom-watering soak until saturated. For wet soil: Gently unpot, trim blackened soft roots, and repot in fresh dry well-draining soil.',
        prevention: 'Maintain a consistent watering schedule adjusted for seasonal temperature changes in Ndola.'
    },
    pests: {
        title: '🦟 White Fluff, Webbing, or Sticky Leaves',
        icon: '🦟',
        cause: 'Common Pests (Mealybugs, Spider Mites, or Scale)',
        diagnosis: 'Tiny insects feed on plant sap, leaving sticky honeydew residue or cotton-like webbing in leaf crevices and leaf joints.',
        solution: 'Dab visible bugs with a cotton swab dipped in rubbing alcohol. Wipe entire foliage with a mild solution of neem oil or insecticidal soapy water.',
        prevention: 'Inspect the undersides of leaves weekly when watering and wipe dust off foliage.'
    },
    leggy: {
        title: '☀️ Pale Leaves & Stretched, Leggy Stems',
        icon: '☀️',
        cause: 'Insufficient Light (Reaching for the Sun)',
        diagnosis: 'When light is too dim, the plant expends energy growing long, weak stems towards the nearest light source rather than producing lush foliage.',
        solution: 'Move the plant 2 to 3 feet closer to an east- or south-facing window with bright indirect sunlight.',
        prevention: 'Rotate pots a quarter turn every week so all sides receive balanced light.'
    },
    mold: {
        title: '🪨 White Mold on Soil Surface',
        icon: '🪨',
        cause: 'Stagnant Air & Continuously Damp Soil Surface',
        diagnosis: 'Harmless saprophytic fungi thrive when the topsoil remains damp in rooms with low air circulation.',
        solution: 'Scrape off the top layer of mold, sprinkle a light dust of ground cinnamon (natural organic fungicide), and improve room ventilation.',
        prevention: 'Bottom-water your plants or ensure topsoil dries out between waterings.'
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // 1. Symptom Checker Interactivity
    const symptomButtons = document.querySelectorAll('.symptom-btn');
    const symptomCard = document.getElementById('vg-symptom-card');

    function displaySymptom(key) {
        const data = SYMPTOMS_DATA[key];
        if (!data || !symptomCard) return;

        symptomButtons.forEach(btn => btn.classList.toggle('active', btn.dataset.symptom === key));

        symptomCard.innerHTML = `
            <div class="symptom-result-header">
                <div class="symptom-badge-icon">${data.icon}</div>
                <div>
                    <h3>${data.title}</h3>
                    <span class="symptom-cause-tag">Probable Cause: ${data.cause}</span>
                </div>
            </div>
            
            <div class="symptom-analysis-grid">
                <div class="analysis-box">
                    <span class="analysis-label">🔍 What Is Happening</span>
                    <p>${data.diagnosis}</p>
                </div>
                <div class="analysis-box highlight-solution">
                    <span class="analysis-label">🛠️ Step-by-Step Fix</span>
                    <p>${data.solution}</p>
                </div>
            </div>

            <div class="prevention-tip-bar">
                <span>💡 <strong>Greenhouse Pro Tip:</strong> ${data.prevention}</span>
            </div>

            <div class="symptom-actions-bar">
                <a href="https://wa.me/260771594459?text=Hi%20Verdant%20Greens%20Plant%20Doctor,%20my%20plant%20is%20showing%20symptoms%20of%20${encodeURIComponent(data.title)}.%20Can%20you%20help?" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">
                    💬 Send Plant Photo to Our Botanist (+260 771 594 459)
                </a>
            </div>
        `;
    }

    symptomButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            displaySymptom(btn.dataset.symptom);
        });
    });

    // Default to yellow leaves
    if (symptomButtons.length > 0) {
        displaySymptom('yellow');
    }

    // 2. Care Guide Plant Search Filter
    const careSearchInput = document.getElementById('vg-care-search');
    const plantCards = document.querySelectorAll('.care-plant-card');

    if (careSearchInput) {
        careSearchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            let visibleCount = 0;

            plantCards.forEach(card => {
                const text = card.textContent.toLowerCase();
                const match = text.includes(query);
                card.style.display = match ? 'flex' : 'none';
                if (match) visibleCount++;
            });

            const countEl = document.getElementById('vg-care-results-count');
            if (countEl) {
                countEl.textContent = `Showing ${visibleCount} botanical care guides`;
            }
        });
    }

    // 3. Dynamic footer year
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});


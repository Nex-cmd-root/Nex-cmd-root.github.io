/**
 * Verdant Greens - Theme Controller (theme.js)
 * Manages Light / Dark mode toggling, system preferences,
 * smooth color transitions, and state persistence in localStorage.
 */

(function () {
    const THEME_STORAGE_KEY = 'verdant_greens_theme';
    const THEME_DARK = 'dark';
    const THEME_LIGHT = 'light';

    // 1. Immediate theme application before DOM loads to prevent white flash
    function getStoredTheme() {
        try {
            const saved = localStorage.getItem(THEME_STORAGE_KEY);
            if (saved === THEME_DARK || saved === THEME_LIGHT) {
                return saved;
            }
        } catch (e) {
            console.warn('Could not read theme from storage', e);
        }
        // Default to system preference if supported, otherwise light
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return THEME_DARK;
        }
        return THEME_LIGHT;
    }

    const currentTheme = getStoredTheme();
    document.documentElement.setAttribute('data-theme', currentTheme);

    // 2. DOM Ready UI bindings
    function initThemeUI() {
        const activeTheme = document.documentElement.getAttribute('data-theme') || THEME_LIGHT;
        updateToggleButtons(activeTheme);

        // Bind all theme toggle buttons on the page
        const toggleButtons = document.querySelectorAll('.theme-toggle-btn, [data-action="toggle-theme"]');
        toggleButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                toggleTheme();
            });
        });

        // Listen for OS theme changes
        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
                if (!localStorage.getItem(THEME_STORAGE_KEY)) {
                    setTheme(e.matches ? THEME_DARK : THEME_LIGHT, false);
                }
            });
        }
    }

    function setTheme(theme, persist = true) {
        document.documentElement.setAttribute('data-theme', theme);
        if (persist) {
            try {
                localStorage.setItem(THEME_STORAGE_KEY, theme);
            } catch (e) {
                console.warn('Could not save theme to storage', e);
            }
        }
        updateToggleButtons(theme);
    }

    function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme') || THEME_LIGHT;
        const next = current === THEME_DARK ? THEME_LIGHT : THEME_DARK;
        setTheme(next, true);
    }

    function updateToggleButtons(theme) {
        const toggleButtons = document.querySelectorAll('.theme-toggle-btn, [data-action="toggle-theme"]');
        toggleButtons.forEach(btn => {
            const isDark = theme === THEME_DARK;
            btn.setAttribute('aria-label', isDark ? 'Switch to Light Theme' : 'Switch to Dark Theme');
            btn.setAttribute('title', isDark ? 'Switch to Light Theme' : 'Switch to Dark Theme');
            
            // Look for icon inside button or update text
            const iconSpan = btn.querySelector('.theme-icon');
            if (iconSpan) {
                iconSpan.textContent = isDark ? '☀️' : '🌙';
            } else {
                btn.innerHTML = `<span class="theme-icon">${isDark ? '☀️' : '🌙'}</span> <span class="theme-text">${isDark ? 'Light' : 'Dark'}</span>`;
            }
        });
    }

    // Expose API
    window.VG_THEME = {
        getTheme: () => document.documentElement.getAttribute('data-theme') || THEME_LIGHT,
        setTheme: setTheme,
        toggle: toggleTheme
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThemeUI);
    } else {
        initThemeUI();
    }
})();

const toggleBtn = document.getElementById('theme-toggle');
const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
const savedTheme = localStorage.getItem('theme');

const setTheme = (isDark) => {
    document.body.classList.toggle('dark', isDark);
    toggleBtn.textContent = isDark ? '☀️' : '🌙';
};

// Initial Theme Setup
if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    setTheme(true);
}

// Toggle Button Click
toggleBtn.addEventListener('click', () => {
    const isDark = !document.body.classList.contains('dark');
    setTheme(isDark);
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

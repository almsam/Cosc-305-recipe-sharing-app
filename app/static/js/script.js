document.addEventListener("DOMContentLoaded", () => {
  const searchBtn = document.getElementById('search-btn');
  const searchBar = document.getElementById('search-bar');
  const resultsList = document.getElementById('results-list');

  const load = async (q) => {
    const res = await fetch(`/api/recipes${q ? `?q=${encodeURIComponent(q)}` : ''}`);
    const recipes = await res.json();
    if (!resultsList) return;
    resultsList.innerHTML = '';
    recipes.forEach(r => {
      const li = document.createElement('li');
      li.innerHTML = `<a href="/recipe/${r.id}">${r.title}</a> — ${r.summary || ''}`;
      resultsList.appendChild(li);
    });
  };

  // preload from ?q=
  const paramsQ = new URLSearchParams(location.search).get('q') || '';
  if (searchBar) searchBar.value = paramsQ;
  load(paramsQ);

  if (searchBtn && searchBar) {
    searchBtn.addEventListener('click', () => load(searchBar.value.trim()));
  }
});

fetch('/api/recipes')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('recipes');
    container.innerHTML = data.map(r => `<p>${r.name}</p>`).join('');
  });

function renderRecipeCards(container, items){
  container.innerHTML = items.map(i => `
    <article class="card">
      <img src="/static/images/placeholder.png" alt="">
      <h3><a href="/recipe/${i.id}">${i.title}</a></h3>
      <p>${i.summary || ''}</p>
    </article>
  `).join('');
}
// Pesquisa na galeria
document.querySelector('.search-form-gallery').addEventListener('submit', function(e) {
    e.preventDefault();
    const searchTerm = document.querySelector('.search-form-gallery input[type="search"]').value.toLowerCase();
    const characters = document.querySelectorAll('#character-list li');

    characters.forEach(character => {
        if (character.textContent.toLowerCase().includes(searchTerm)) {
            character.style.display = 'inline-block'; // Mostra o personagem se corresponder
        } else {
            character.style.display = 'none'; // Esconde se não corresponder
        }
    });
});

// Pesquisa na barra de pesquisa principal (se necessário)
document.querySelector('.search-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const searchTerm = document.querySelector('.search-form input[type="search"]').value.toLowerCase();
    const characters = document.querySelectorAll('#character-list li');

    characters.forEach(character => {
        if (character.textContent.toLowerCase().includes(searchTerm)) {
            character.style.display = 'inline-block'; // Mostra o personagem se corresponder
        } else {
            character.style.display = 'none'; // Esconde se não corresponder
        }
    });
});

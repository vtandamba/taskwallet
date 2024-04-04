document.addEventListener("DOMContentLoaded", function () {
    // Appliquer le mode light par défaut
    document.body.classList.add('light-mode');

    // Gestion des clics sur les liens du menu
    const menuLinks = document.querySelectorAll(".menu-link");
    menuLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            menuLinks.forEach(function (link) {
                link.classList.remove("is-active");
            });
            this.classList.add("is-active");
        });
    });

    // Gestion des clics sur les liens de l'en-tête principal
    const headerLinks = document.querySelectorAll(".main-header-link");
    headerLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            headerLinks.forEach(function (link) {
                link.classList.remove("is-active");
            });
            this.classList.add("is-active");
        });
    });

    // Gestion des clics sur les éléments de type dropdown
    const dropdowns = document.querySelectorAll(".dropdown");
    dropdowns.forEach(function (dropdown) {
        dropdown.addEventListener("click", function (e) {
            e.stopPropagation();
            dropdowns.forEach(function (otherDropdown) {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove("is-active");
                }
            });
            dropdown.classList.toggle("is-active");
        });
    });

    // Gestion du focus sur la barre de recherche
    const searchBarInput = document.querySelector(".search-bar input");
    const header = document.querySelector(".header");
    searchBarInput.addEventListener("focus", function () {
        header.classList.add("wide");
    });
    searchBarInput.addEventListener("blur", function () {
        header.classList.remove("wide");
    });

    // Gestion des clics en dehors du conteneur de statut
    document.addEventListener("click", function (e) {
        const statusButton = document.querySelector(".status-button");
        const dropdown = document.querySelector(".dropdown");
        if (!statusButton.contains(e.target)) {
            dropdown.classList.remove("is-active");
        }
    });

    // Gestion des clics sur les éléments de type dropdown
    document.querySelectorAll(".dropdown").forEach(function (dropdown) {
        dropdown.addEventListener("click", function (e) {
            document.querySelector(".content-wrapper").classList.add("overlay");
            e.stopPropagation();
        });
    });

    // Gestion de la fermeture des pop-ups
    document.querySelector(".pop-up .close").addEventListener("click", function () {
        document.querySelector(".overlay-app").classList.remove("is-active");
    });

    // Gestion du clic sur le bouton toggle pour le mode sombre/lumineux
    document.querySelector('.dark-light').addEventListener('click', function () {
        document.body.classList.toggle('light-mode');
    });
});

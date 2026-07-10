// Capital Rural — interações de navegação
(function () {
  "use strict";

  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const aberto = nav.classList.toggle("aberto");
      toggle.setAttribute("aria-expanded", aberto ? "true" : "false");
    });

    // Fecha o menu ao clicar em um link (mobile)
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("aberto");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Atualiza o ano no rodapé
  const anoEl = document.querySelectorAll("[data-ano]");
  anoEl.forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();

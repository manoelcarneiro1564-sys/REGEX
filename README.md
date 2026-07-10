# Capital Rural — Site institucional

Site institucional estático da **Capital Rural**, empresa de crédito e soluções
financeiras para o agronegócio. Feito em HTML, CSS e JavaScript puro, sem
dependências ou etapa de build.

## Estrutura

```
.
├── index.html                                  # Página inicial
├── blog.html                                   # Listagem do blog
├── blog/
│   ├── plano-safra-2026-2027.html              # Matéria 1 — Crédito Rural
│   └── financas-da-propriedade-rural.html      # Matéria 2 — Gestão
└── assets/
    ├── css/styles.css                          # Estilos do site
    └── js/main.js                              # Menu mobile e utilidades
```

## Matérias do blog

1. **Plano Safra 2026/2027: o que muda para o produtor** — explica as principais
   linhas de crédito, mudanças da temporada e como se preparar para acessar o crédito.
2. **5 pilares para organizar as finanças da sua propriedade** — guia prático de
   gestão financeira rural: separação de contas, fluxo de caixa e uso consciente do crédito.

## Como visualizar localmente

Basta abrir o `index.html` no navegador, ou servir a pasta:

```bash
python -m http.server 8000
# acesse http://localhost:8000
```

## Personalização

- **Cores e tipografia:** variáveis CSS no topo de `assets/css/styles.css` (`:root`).
- **Contato:** atualize e-mail e telefone nos rodapés e na seção de contato.
- **Novas matérias:** duplique um arquivo de `blog/` e adicione o card em
  `blog.html` e na seção de destaque do `index.html`.

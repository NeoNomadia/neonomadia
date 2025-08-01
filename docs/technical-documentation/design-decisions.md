# Design Decisions

## Project Language

The primary language for communication and documentation — including code comments — is **English**.

In cases involving country-specific, ethnic, or linguistic topics, using the respective local language may be appropriate. However, whenever possible, an accompanying English translation should be provided to ensure clarity and inclusivity across the project.


## Project Management System

The selection of a project management system remains open. The tool must encourage **simplicity**, making it easy for all potential contributors to engage comfortably.

Another key factor is **role management** — the system should support well-defined contributor roles that reflect NeoNomadia’s collaborative ethos.

This decision will be revisited once the initial roadmap is finalized and the project's evolving vision offers greater clarity on long-term requirements.

## Corporate Design

NeoNomadia is visually anchored by a distinctive logo, primarily designed for use on the project website:

![NeoNomadia Logo](../assets/images/neonomadia-full-logo-225.png#only-light)
![NeoNomadia Logo](../assets/images/neonomadia-full-logo-225-dm.png#only-dark)

This logo establishes the project's core color palette:

| Color Name | RGB | HEX Code |
|------------|-----|----------|
| <span style="color: #0A2438">**Dark Blue**</span> | 10, 36, 56 | #0A2438 |
| <span style="color: #29525C">**Turquoise**</span> | 41, 82, 92 | #29525C |
| <span style="color: #2E666B">**Light Turquoise**</span> | 46, 102, 107 | #2E666B |
| <span style="color: #F69B2F">**Light Orange**</span> | 246, 155, 47 | #F69B2F |

All additional design elements must align with this visual identity to maintain a coherent and recognizable presence across media.

The preferred typeface is **Noto Sans**, chosen for its modern clarity and wide multilingual support.

It is available as:

- **Browser font** via [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans.) for web integration:
  - CSS 
    ~~~
    font-family: 'Noto Sans', sans-serif;
    ~~~
  - HTML
    ~~~
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap" rel="stylesheet">
    ~~~
- **Downloadable TTF files** for desktop or local hosting via [1001 Fonts](https://www.1001fonts.com/noto-sans-font.html)
    or [CDNFonts](https://www.cdnfonts.com/noto-sans.font)

## CSS Unit Strategy

To ensure responsive, accessible, and scalable design across NeoNomadia and future sibling projects (e.g. Embera.world), we adopt a modern CSS unit strategy:

- **Use `rem` for font sizes, spacing, and layout rhythm**  
  This ensures consistency and respects user accessibility settings.

- **Use `%` for widths and container scaling**  
  Enables fluid layouts that adapt to parent elements.

- **Use `vw` / `vh` sparingly for full-screen sections or hero blocks**  
  Ideal for immersive layouts, but should be used with care to avoid overflow issues.

- **Avoid `px` for core layout and typography**  
  Pixels are fixed and don’t scale well across devices or zoom levels. Still acceptable for borders or fine-tuned icon sizing.

This strategy will be formalized and reused in Embera.world and other NeoNomadia-aligned projects to maintain visual coherence and accessibility across platforms.

# Python Chile 2026 Theme (pycltheme2026)

Este es el tema oficial de Python Chile, diseñado para ser moderno, rápido y fácil de mantener. Utiliza **Pelican** como generador de sitio estático y **Tailwind CSS** para el diseño.

## 🚀 Tecnologías
- **Pelican** (Jinja2 Templates)
- **Tailwind CSS v3** (vía npm)
- **Plugins de Tailwind**: Typography (prose), Forms, Aspect-Ratio, Line-clamp.
- **Iconos**: FontAwesome 6.5.1
- **Fuentes**: Inter (Sans) y Fira Code (Mono) vía Google Fonts.

## 📦 Estructura del Tema
```text
pycltheme2026/
├── static/
│   ├── css/
│   │   ├── tailwind.src.css  # Archivo fuente con directivas @tailwind
│   │   ├── tailwind.css      # Archivo generado (NO EDITAR DIRECTAMENTE)
│   │   └── pygment.css       # Resaltado de sintaxis para código
│   ├── images/               # Assets estáticos del tema (logos, favicons)
│   └── js/                   # Scripts (Dark mode, Menu mobile)
├── templates/
│   ├── base.html             # Esqueleto principal
│   ├── index.html            # Portada con grilla de artículos
│   ├── article.html          # Vista de artículo individual
│   ├── page.html             # Vista de páginas estáticas
│   ├── includes/             # Componentes reutilizables
│   │   ├── header.html       # Header de 3 niveles (Nav, Hero, Social)
│   │   ├── footer.html       # Footer unificado
│   │   ├── article_card.html # Tarjeta de artículo (grillas)
│   │   ├── pagination.html   # Componente de navegación de páginas
│   │   └── communities.html  # Sección de Comunidades Amigas
│   └── headermeta.html       # Metadatos, SEO y carga de assets
├── tailwind.config.js        # Configuración de colores y fuentes de marca
└── package.json              # Dependencias de Node.js y scripts
```

## 🛠️ Desarrollo (Tailwind CSS)

Para modificar los estilos del tema, sigue estos pasos:

1. **Instalar dependencias** (solo la primera vez):
   ```bash
   cd pycltheme2026
   npm install
   ```

2. **Compilar en tiempo real** (Recomendado):
   ```bash
   npm run watch
   ```
   *Esto vigila cambios en los archivos `.html` y actualiza el CSS automáticamente.*

3. **Compilar para producción**:
   ```bash
   npm run build
   ```
   *Genera un archivo CSS minificado y optimizado (solo incluye las clases usadas).*

## 🎨 Personalización
La paleta de colores de marca está definida en `tailwind.config.js`:
- `python-blue`: `#306998`
- `python-yellow`: `#FFD43B`
- `python-dark`: `#1e293b`

Para usar estos colores en el HTML, puedes usar clases como `bg-python-blue`, `text-python-yellow`, etc.

## 🔍 Resaltado de Sintaxis
El resaltado de sintaxis utiliza **Pygments**. Se ha añadido un override CSS en `headermeta.html` para asegurar que el bloque de código conviva correctamente con el plugin `prose` de Tailwind.

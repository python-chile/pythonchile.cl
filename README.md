# pythonchile.cl

## Configuración inicial

* Crear un entorno virtual, e instalar las dependencias:
  ```
  python -m venv env
  source env/bin/activate   # macOS/Linux
  env\Scripts\activate.bat  # Windows
  pip install -r requirements.txt
  ```

## Generar sitio estático

* Para generar el sitio estático, ejecutar:
  ```
  pelican content
  ```
  Lo que generará un directorio `output/` con el sitio web.

* Para ejecutar un servidor de prueba:
  ```
  pelican -l
  ```
  Podrás revisar el contenido generado en la url  http://127.0.0.1:8000
  y con la combinación de teclas `Ctrl + c` cierras el proceso.

## Despliegue

* Se utilizarán Github Actions, para hacer un despliegue al servidor.
* De momento es una acción sencilla que obtiene la última versión, genera el
  sitio y lo copia al directory a donde apunta la URL.

## Cómo contribuir

* Para agregar un nuevo post, favor seguir el paso a paso descrito en la [documentación oficial](https://github.com/python-chile/docs/blob/master/formato-presentacion-blog.md).
* Para conocer más sobre normativa en proyectos Python Chile, favor visitar la siguiente [documentación oficial](https://github.com/python-chile/docs/blob/master/normativa-trabajo-github.md).
* Para más información sobre como escribir un contenido en Pelican, favor visitar la siguiente [documentación](https://docs.getpelican.com/en/latest/content.html).

## Información adicional

* El tema utilizado actualmente es **pycltheme2026**, una evolución moderna basada en Tailwind CSS que reemplaza la versión anterior de Bootstrap.
* El tema se encuentra en el directorio `pycltheme2026`.

### Gestión de Estilos (Tailwind CSS)

El tema utiliza Tailwind CSS con un flujo de trabajo local basado en Node.js. Para realizar cambios en el diseño:

1. Entra a la carpeta del tema: `cd pycltheme2026`
2. Instala las dependencias: `npm install`
3. Ejecuta el compilador en modo escucha: `npm run watch` (esto regenerará `static/css/tailwind.css` automáticamente).

Para más detalles técnicos, consulta el [README del tema](pycltheme2026/README.md).



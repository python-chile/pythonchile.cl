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
  Podras revisar el contenido generado en la url  http://127.0.0.1:8000
  y con la combinación de teclas `Ctrl + c` cierras el proceso.

## Despliegue

* Se utiliazarán Github Actions, para hacer un despliegue al servidor.
* De momento es una acción sencilla que obtiene la última versión, genera el
  sitio y lo copia al directory a donde apunta la URL.


## Información adicional

* El tema que se utiliza actualmente, es un tema basado en el tema oficial
  `simple`, pero utilizando componentes de bootstrap para poder mejorar el
  diseño. Más información relacionada a la configuración del tema y como
  modificarlo, en la
  [documentación oficial](https://docs.getpelican.com/en/latest/themes.html).
  El tema está ubicado en el directorio `pycltheme`.

* La contribución de posts se hará mediante Pull-Requests a este repositorio,
  donde las personas tendrán que crear un archivo nuevo (con extensión `md`)
  en el directorio `content/`. El nombre corresponderá al título del post.
  Para más información sobre como escribir el contenido, visitar la
  [documentación](https://docs.getpelican.com/en/latest/content.html).

---
layout: post
title: ¡La documentación oficial de Python necesita tu ayuda!
subtitle: Traducción oficial de la documentación de Python al Español.
author: Cristián Maureira-Fredes
image: python-docs-es-logo.png
tags: python-docs, python
category: comunidad
---

A comienzos del 2020, un grupo de personas comenzaron a notar que la
**documentación oficial de Python** contaba con traducciones oficiales en
distintos idiomas, pero no en Español. Considerando que nuestro idioma es el
[segundo en el ranking mundial con más hablantes
nativos](https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers)
se tenía que hacer algo al respecto.

Gracias al esfuerzo de la [comunidad argentina de
Python](http://www.python.org.ar/), el tutorial oficial de la documentación ya
estaba traducido, el cual corresponde a uno de los elementos de la lista
oficial de requerimientos para ser aceptado como documentación oficial, con lo
que el primer paso ya estaba hecho.

Pasó el tiempo, y en una actividad a realizarse en España, el [PyCamp
ES](https://pycamp.es/) (inspirado en la [iniciativa
argentina](https://argentinaenpython.com/eventos/)), se tenía previsto poder
aumentar la cantidad de gente involucrada, para que así se pudiera llegar a ser
aceptado lo antes posible. Debido al COVID-19, dicho evento no se pudo
realizar, pero si se comenzó a hacer llamados públicos para cualquier
interesado pudiera colaborar, ya sea traduciendo, o revisando texto que ya
estaba traducido. Para fomentar la participación, se desarrollo un sitio web,
que contiene todos los pasos para poder comenzar con las contribuciones, siendo
así el punto inicio del equipo **PythonDocsEs**.

Tomó solo **un par de meses** para tener una cantidad importante de personas
provenientes de distintos países de habla hispana, los cuales en tiempo récord
pudieron acabar con los requisitos mínimos para ser aceptados, y así mover el
repositorio dentro del proyecto Python, convirtiéndose así en la
**documentación oficial en Español**.

La última actividad donde se pudo avanzar notablemente, fueron los Sprints de
la conferencia [EuroPython](https://ep2020.europython.eu/), de los cuales
puedes ver las [estadísticas finales
acá](https://maureira.xyz/python-docs-es-sprint-final/#/).

## Detalles Técnicos

El desarrollo se basa en un repositorio **Git**, en el cual existen **Issues**
con los archivos más demandados que necesitan traducción, ésta lista va
aumentando con el tiempo, ya que no todos los archivos que aún necesitan ser
traducidos tienen un Issue correspondiente.

Al asignar un **Issue**, las personas comienzan a traducir y envían un
**Pull-Request** que es revisado por cualquier persona de la iniciativa, y una
vez todo esté en orden, se acepta y se incluye en la rama de la versión
actualmente en uso, 3.8.

Los archivos a traducir tienen la [extensión
'po'](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html),
formato diseñado para la traducción de documentación, y que afortunadamente
tiene un conjunto de herramientas que facilitan su manipulación, como `powrap`
para ajustar el archivo a la cantidad de columnas requerida, `pospell` para
poder hacer correcciones ortográficas, y `poedit` para abrir el archivo de una
manera más conveniente y poder ver cada entrada en Inglés y proceder
a traducirla al Español.

Dentro de los archivos de traducción, existen algunas sentencias provenientes
de [Python Sphinx](https://www.sphinx-doc.org/en/master/), ya que la
documentación oficial se basa en Sphinx para generar el sitio web, con lo que
es común encontrarse con texto con frases como " La clase ``:class:`UnaClase`
`` " sirve para...", "...es importante verificar que ``:data:`otro.atributo` ``
no sea ....", etc, o formatos para establecer cuando un texto utiliza énfasis
(rodeando la palabra con asteriscos dobles), cursiva (rodeando la palabra con
un asterisco a cada lado), o URLs que se escriben de la forma `` `Comunidad
Chilena de Python <https://pythonchile.cl>`_ ``, etc. Puedes encontrar más
información sobre el formato que utiliza Sphinx, que se llama
*restructuredText* (rst) en la
[documentación](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

## Flujo de trabajo

Los pasos para realizar una traducción son bastante simples, y te los describimos ahora:

 * Hacer un fork del [repositorio oficial](https://github.com/python/python-docs-es/)
 * Buscar un **Issue** sin asignar, y pedirlo a los coordinadores, por ejemplo:
   `library/ast.po`
 * Crear un entorno virtual (solo una vez) dentro del repositorio para no
   instalar las herramientas de manera global en el sistema

        :::bash
        # Pasos para crear un entorno en Unix (macOS/Linux) o Windows
        python -m venv env
        source env/bin/activate # Para Unix
        env\Scripts\activate    # Para Windows
        pip install powrap pospell poedit

 * Agregar el repositorio principal como **remote**, para poder enviar
   **Pull-requests** (solo una vez)

        :::bash
        git remote add upstream https://github.com/python/python-docs-es.git

 * Crear una rama local, con un nombre que incluya el nombre de nuestro archivo

        :::bash
        # Recordamos que en el ejemplo el archivo se llama 'library/ast.po'
        git checkout -b traduccion_library_ast

 * Abres el archivo con `poedit` y comienzas a traducir!
 * Una vez terminado, o en cualquier momento en que quieras enviar una sección
   a revisión, realizas un **commit** y creas un **Pull-request**

        :::bash
        # Pasos antes de enviar un commit al Pull-request
        powrap library/ast.po # Para asegurarnos de que las columnas estén bien
        git add library/ast.po
        git commit -m "Traducido library/ast"
        git push origin traduccion_library_ast

Luego aparecerá un mensaje con un link para crear el Pull-request, y sería
todo!

Por supuesto, al existir complicaciones como: problemas con el build, palabras
no reconocidas, o comentarios por los revisores, hay que seguir haciendo más
**commits** sobre la misma rama, e ir actualizando el **Pull-request** hasta
que pueda ser incluido.

De cualquier forma, existe una página con preguntas frecuentes, [que puedes
leer acá](https://python-docs-es.readthedocs.io/es/3.8/faq.html).


## ¿Puedo ayudar de otra forma que no sea traduciendo?

Claro! actualmente [existen varios Pull-request
abiertos](https://github.com/python/python-docs-es/pulls) que **necesitan
corrección**, para eso solo necesitas tener una cuenta de Github, y hacer
comentarios en cualquier Pull-request que te interese, ya sea editando
y proponiendo una traducción alternativa de una palabra o frase, como
comentarios generales relacionados al uso de alguna palabra.

Si lees un Pull-request y todo te parece bien, no olvides dejar un comentario
y cualquier coordinador que lo vea sabrá que el trabajo ya ha sido revisado,
y que **gracias a ti podremos aceptar la traducción**.

## ¿Cómo Participar?

El [sitio web con la información para comenzar
a contribuir](https://python-docs-es.readthedocs.io/es/3.8/CONTRIBUTING.html)
contiene un enlace al grupo de Telegram (con casi 100 personas!) donde la
comunidad discute el uso de distintas terminologías, aclara dudas, y ayuda
a todas las personas que quieran comenzar a participar.

Si te interesa tener tu primera **contribución oficial a Python**, esta
iniciativa sin lugar a duda, es tu primer paso!

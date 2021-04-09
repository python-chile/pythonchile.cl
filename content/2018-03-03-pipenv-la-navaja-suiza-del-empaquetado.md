---
layout: post
title: Pipenv La Navaja Suiza Del Empaquetado
subtitle: Flujo De Trabajo
author: Pablo Lira
image: default.jpg
tags: pip, python, virtualenv, pyenv, env
category: tutorial
---

Un flujo clásico de manejo de paquetes y de entorno de desarrollo virtual en
Python, es la utilización de `pip` en combinación con `virtualenv`, para
manejar paquetes y administrar entornos de desarrollo virtuales
respectivamente, para tener la ventaja de replicar el proyecto en otro sistema,
o de desarrollar distintos proyectos sin conflictos de librerías.

Un ejemplo de flujo de trabajo de estas herramientas seria:

```bash
virtualenv -p python3 entorno-virtual
source entorno-virtual/bin/activate
pip install django==1.11
pip freeze > requirements.txt
```

En el primer comando crea un entorno de desarrollo con una versión por defecto
de python3 y le damos un nombre al entorno: "entorno-virtual", seguimos con el
siguiente comando para activar el entorno virtual, y estar aislado del sistema,
procedemos a instalar django específicamente la versión 1.11. Una vez que
termina dicha instalación procedemos a plasmar el nuevo paquete en el archivo
`requirements.txt`.

```bash
Django==1.11
pytz==2018.3  # dependencia de instalación automática de django.
```

Es un proceso simple, pero se puede volver algo tedioso de mantener
manualmente, el archivo `requirements.txt` no se actualiza solo, teniendo que
ejecutar `pip freeze > requirements.txt` cada vez que instalamos una biblioteca
nueva y no especifica la versión especifica de Python que se utiliza.

En distintos estados de desarrollos o fases, pueden que utilicemos bibliotecas
que no sean necesarias en un sistema de producción pero si en un sistema
desarrollo. Por ejemplo, necesitamos instalar el paquete `pytest`, para hacer
test de desarrollo de una aplicación que desarrollada con django, obviamente no
necesitamos dicha biblioteca en nuestro servidor de producción.

Lo más simple que se hace es tener de dos a tres archivos con los
requerimientos específicos y llevar la administración de estos archivos de
manera manual.

Ejemplo básico: `producción.txt`:

```bash
Django==1.11
pytz==2018.3
```

y `desarrollo.txt`:

```bash
pluggy==0.6.0
py==1.5.2
pytest==3.4.1
six==1.11.0
```

El ejemplo anterior no es un estándar, los desarrolladores de Python
administran sus listas de paquetes como más les guste o le parezca correcto.

Un tema que no es menor, en ningún lado queda documentado que versión de Python
es la que se debe de usar para replicar el proyecto, esto igual queda en manos
del desarrollador.

En resumen de esta tediosa historia, es que hay que tener una filosofía de
administración de dependencias, hay que documentar en alguna parte que con que
versión funciona el proyecto. Las dependencias de las librerías pueden romperse
por alguna incompatibilidad difícil de encontrar entre la librería principal
y versiones de Python, haciendo un poco más difícil la administración
y replicación del proyecto, sin mencionar la carga de "variables de
entorno (.env)" se deben de hacer manual.

## Pipenv: Python Development Workflow for Humans

Pipenv es la herramienta, que administra este flujo de trabajo de manera
eficaz, utilizando pip como administrador de paquetes, virtualenv como creador
de entorno virtual y pyenv como administrador de versiones de python. Generando
automáticamente dos archivos, `Pipfile` y `Pipfile.lock`, encargados de
documentar automáticamente el entorno de desarrollo.

La instalación de `pipenv` la podemos de realizar con `pip`, la única
dependencia que no se cumple es `pyenv` que tendrán que realizar una
instalación manual.  (pipenv no es compatible con Windows.)

```bash
pip3 install pipenv
```

Veamos como seria un flujo de trabajo con `pipenv`.

Primero creamos un directorio en donde estará el código del proyecto
e ingresamos:

```bash
mkdir website
cd website
```

luego procedemos a ejecutar:

```bash
pipenv install django
```

Con el comando anterior se crean los archivos automáticamente de `Pipfile`
y `Pipfile.lock`, un entorno virtual y obviamente se instala el paquete Django.

Veamos el archivo `Pipfile`:

```bash
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"
[packages]
django = "*"
[dev-packages]

[requires]
python_version = "3.6"
```

En resumen, la sección de "source" contiene la información del repositorio de
los paquetes, "packages" contiene los nombre de los paquetes instalado,
"dev-packages" contiene los nombres de los paquetes necesarios en desarrollo,
y por ultimo “requires” la versión de Python a usar.

Para instalar y agregar un paquete en dev-packages.

```bash
pipenv install --dev pytest
```

En `Pipfile.lock`, contiene la información detallada sobre la biblioteca,
dependencias de la mismas, y versión de Python usada.

Para inicializar y salir del entorno de desarrollo:

```bash
# activara el entorno
pipenv shell

# saldrá del entorno de la manera correcta.
exit
```

Para desinstalar paquetes, borrara el paquete del entorno y lo eliminara de
`Pipfile`.

```bash
pipenv uninstall django
```

Para replicar el entorno virtual en otra máquina basta con ingresar al
directorio y ejecutar pipenv install ejmplo:

```bash
cd website

# Instalacion de los paquetes del proyecto en producción,
# sin los de desarrollo
pipenv install

# Instalación de paquetes de desarrollo
pipenv install --dev
```

Al encontrar los archivos `Pipfile` y `Pipfile.lock` replicará los paquetes
instalados, y creara un ambiente virtual y en el caso se usar una versión en
especifico de python la instalara automáticamente con pyenv(debe de estar
instalado).

El flujo de trabajo se automatiza, y se especifican los requerimientos
necesarios para llevar a cabo una buena replicación del entorno virtual en
otros sistemas.

`pipenv` tiene muchas mas características, como la carga automática del archivo
`.env`, y `pipenv check` que verifica que se cumplan los requisitos del [PEP
508](https://www.python.org/dev/peps/pep-0508/), etc.

Puedes leer más en la [Documentación
oficial](https://pipenv.readthedocs.io/en/latest/).

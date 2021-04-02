---
layout:	post
title:		Pipenv La Navaja Suiza Del Empaquetado
subtitle:	Flujo De Trabajo
author:	Pablo Lira
image: default.jpg
tags: pip, python,  virtualenv, pyenv, env
category:   
---
<!-- Start Writing Below in Markdown -->

Un  flujo clásico  de manejo de paquetes y de entorno de desarrollo virtual en Python, es la utilización de “pip” en combinación con “virtualenv”, para manejar  paquetes  y  administrar  entornos de desarrollo virtuales respectivamente, para tener la ventaja de replicar el proyecto en otro sistema, o de desarrollar distintos proyectos sin conflictos de librerías.  

Un ejemplo de flujo de trabajo  de estas herramientas seria.

```bash
$virtualenv -p python3 entorno-virtual
$source entorno-virtual/bin/activate
$pip install django==1.11
$pip freeze > requerimientos.txt
```
En el primer comando crea un entorno de desarrollo con una versión  por defecto de python3 y le damos un nombre al entorno: “entorno-virtual”,  seguimos con el siguiente comando para activar el entorno virtual, y estar aislado del sistema, procedemos a instalar django específicamente la versión 1.11. Una vez que termina dicha instalación procedemos a plasmar el nuevo paquete  en el archivo requerimientos.txt . 

```bash
$cat requerimientos.txt
Django==1.11
pytz==2018.3    #dependencia de instalación automática de django.
```
Es un proceso simple, pero se puede volver algo tedioso de mantener manualmente, el archivo requerimientos.txt no se actualiza solo, teniendo que ejecutar “pip freeze > requerimientos.txt” cada vez que instalamos una librería nueva y no especifica la versión especifica de Python que se utiliza.

En distintos estados de desarrollos o fases, pueden que utilicemos librerías que no sean necesarias en un sistema de producción  pero si en un sistema desarrollo. Por ejemplo, necesitamos  instalar el paquete “pytest”, para hacer test de desarrollo de una aplicación que desarrollada con django, obviamente  no necesitamos dicha librería en nuestro servidor de producción.

Lo mas simple que se hace es tener de dos a tres archivos con los requerimientos específicos y llevar la administración de estos archivos de manera manual. Ejemplo básico: producción.txt y desarrollo.txt.

```bash
$cat producción.txt
Django==1.11
pytz==2018.3
```

```bash
$cat desarrollo.txt
pluggy==0.6.0
py==1.5.2
pytest==3.4.1
six==1.11.0
```
El ejemplo anterior no es un estándar, los desarrolladores de Python  administran sus listas de paquetes como mas les guste  o le parezcan correcto. 

Un tema que no es menor, en ningún lado queda documentado que versión de Python es la que se debe de usar para replicar el proyecto, esto igual queda en manos del desarrollador.

En resumen de esta tediosa historia, es que hay que tener  una filosofía de administración de dependencias , hay que documentar en alguna parte que con que versión funciona el proyecto.  Las dependencias de las librerías pueden romperse por alguna incompatibilidad difícil de encontrar entre la librería principal y versiones de Python, haciendo un poco mas difícil la administración y replicación del proyecto, sin mencionar la carga de “variables de entorno(.env)” se deben de hacer manual. 


***Pipenv: Python Development Workflow for Humans***

Pipenv es la herramienta, que administra este flujo de trabajo de manera eficaz, utilizando pip como administrador de paquetes, virtualenv como creador de entorno virtual y pyenv como administrador de versiones de python. Generando automáticamente dos archivos, Pipfile y Pipfile.lock, encargados de documentar automáticamente el entorno de desarrollo. 


La instalación de pipenv la podemos de realizar con pip,  la única dependencia que no se cumple es pyenv que tendrán que realizar una instalación manual.
(pipenv no es compatible con Windows.)

```bash
$pip3 install pipenv
```
Veamos como seria un flujo de trabajo con pipenv.

Primero creamos un directorio o carpeta en donde estará el código del proyecto y ingresamos a el.

```bash
$mkdir website
$cd website
```
 Procedemos a ejecutar

```bash
$pipenv install django
```
Con el comando anterior se crean los archivos automáticamente de pipfile y pipfile.lock, un entorno virtual y obviamente se instala el paquete Django. Veamos el archivo pipfile:

```bash 
$cat Pipfile
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
En resumen…  la sección de “source” contiene la información del repositorio de los paquetes, “packages” contiene los nombre de los paquetes instalado, “dev-packages” contiene los nombres de los paquetes necesarios en desarrollo, y por ultimo “requires”  la versión de Python a usar.

Para instalar y agregar un paquete en dev-packages.

```bash
$pipenv install --dev pytest
```
En Pipfile.lock,  contiene la información detallada sobre la librería, dependencias de la mismas, y versión de Python usada.

Para inicializar y salir del entorno de desarrollo:

```bash
$pipenv shell #activara el entorno
$exit #saldrá del entorno de la manera correcta.
```	
Para desinstalar paquetes, borrara el paquete del entorno y  lo eliminara de Pipfile. 

```bash
$pipenv uninstall django
```

Para replicar el entorno  virtual en otra maquina basta con ingresar al directorio y ejecutar pipenv install ejmplo:

```bash
$cd website
$pipenv install #Instalacion de los paquetes del proyecto en producción, sin los de desarrollo
$pipenv install --dev # instalación de paquetes de desarrollo
```
Al encontrar los archivos pipfile y pipfile.lock replicara los paquetes instalados, y creara un ambiente virtual  y en el caso se usar una versión en especifico de python la instalara automáticamente con pyenv(debe de estar instalado).

El flujo de trabajo se automatiza, y se especifican los requerimientos necesarios para llevar a cabo una buena replicación del entorno virtual en otros sistemas.


Pipenv tiene muchas mas características, como la carga automática del archivo  “.env”, y “pipenv check” que checa que se cumplan los requisitos del PEP 508 etc etc etc.



*Documentación oficial: 
https://pipenv.readthedocs.io/en/latest/*











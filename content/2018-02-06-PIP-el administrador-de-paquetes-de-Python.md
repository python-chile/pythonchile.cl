---
layout:     post
title:      PIP el administrador de paquetes de Python
author:     Pablo Lira
image:      default.jpg
tags: 		pip, python
subtitle:  	guia rapida de uso
category:   
---
<!-- Start Writing Below in Markdown -->



<p class="text-justify">Un administrador de paquetes es un software que se dedica a  instalar, remover, actualizar paquetes de software desde un repositorio,  en este caso  es un especifico para Python.

Pip se instala automáticamente  si compilas Python, también  si lo tienes instalado Python en Windows y en MacOS de las fuentes oficiales(python.org), pero en GNU/Linux dependiendo de la distribución puedes que tengas que instalarlo, un ejemplo  de instalación de pip2 y pip3 para sus respectivas versiones de Python en Debian:</p>

```python
sudo apt-get install python-pip python3-pip
```
Pip se ejecuta en la terminal y su uso básico es:
```bash
pip install paquete # instala un paquete.
pip uninstall paquete # desinstala  un paquete.
pip install paquete --upgrade # actualiza un paquete especifico.
pip  search  palabra # busca un paquete que coincida con la palabra.
pip install paquete==x.x.x # instala una versión especifica del paquete.
pip freeze # lista todos los paquetes instalados.
pip freeze > dependencias.txt # guarda  una lista de los paquetes instalados.
pip install -r dependencias.txt # instala el listado de paquetes.
```
Pip puede instalar  instalar los paquetes en versiones especificas de Python, ejemplo:

```bash
pip install paquete # instala en la versión por default de python en el sistema.
pip2 install paquete # instala en la versión por default de python2 en el sistema.
pip2.7 install paquete # instala en la versión especifica de python2.7 en el sistema.
pip3 install paquete # instala en la versión por default de python3 en el sistema.
pip3.6 install paquete # instala en la versión especifica de python3.6 en el sistema.
```
El uso de pip  es simple, y fácil de entender.



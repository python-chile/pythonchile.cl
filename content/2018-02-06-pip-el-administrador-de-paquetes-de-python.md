---
layout: post
title: PIP el administrador de paquetes de Python
subtitle: Guía rápida de uso
author: Pablo Lira
image: default.jpg
tags: pip, python
category: tutorial
---

Un administrador de paquetes es un software que se dedica a instalar, remover,
actualizar paquetes de software desde un repositorio central, en este caso es
un especifico para Python, llamado [PyPi](https://pypi.org).

> Nota que `pip` es también capaz de instalar "wheels" (archivos .whl)
> localmente que puedes haber descargado de distintas fuentes.

`pip` se instala automáticamente si compilas Python, también si lo tienes
instalado en las plataformas principales, Windows, macOS y Linux.

En sistemas Unix, dependiendo de la distribución de Linux o el método de
instalación en macOS puede que tengas que instalarlo a mano.

Un ejemplo de instalación de `pip2` y `pip3` para sus respectivas
versiones de Python en Debian:

```bash
sudo apt-get install python-pip python3-pip
```

`pip` se ejecuta en la terminal y su uso básico es:

```bash
# instala un paquete.
pip install paquete

# desinstala un paquete.
pip uninstall paquete

# actualiza un paquete especifico.
pip install paquete --upgrade

# busca un paquete que coincida con la palabra.
pip search palabra

# instala una versión especifica del paquete.
pip install paquete==x.x.x

# lista todos los paquetes instalados.
pip freeze

# guarda una lista de los paquetes instalados.
pip freeze > requirements.txt

# instala el listado de paquetes.
pip install -r requirements.txt
```

`pip` puede instalar instalar los paquetes en versiones especificas de Python,
ejemplo:

```bash
# instala en la versión por default de python en el sistema.
pip install paquete

# instala en la versión por default de python2 en el sistema.
pip2 install paquete

# instala en la versión especifica de python2.7 en el sistema.
pip2.7 install paquete

# instala en la versión por default de python3 en el sistema.
pip3 install paquete

# instala en la versión especifica de python3.6 en el sistema.
pip3.6 install paquete
```

El uso de `pip` es simple, y recomendado tanto si están comenzando como si ya
tienes más experiencia!.

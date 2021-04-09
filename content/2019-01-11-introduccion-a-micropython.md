---
layout: post
title: Introducción a MicroPython
author: Pablo Lira
tags: pip, python, micropython
subtitle: Python para micro-controladores
image: intro_micropython-logo.png
category: tutorial
---

Micro Python es una re-implementación del lenguaje Python específicamente de la
versión 3.4 para micro-controlares, fue desarrollado por el programador
australiano [Damien P George ](http://dpgeorge.net/)y fue lanzado el 2014 en
[Kickstarter](https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers)
para obtener financiación junto a una placa de desarrollo llamada PyBoard
siendo un éxito en la recaudación de fondos.

Está implementado en el lenguaje C, para la [arquitectura de procesador
ARM](https://es.wikipedia.org/wiki/Arquitectura_ARM), se debe de portar
a versiones específicas de cada procesador ARM, sin embargo, ha sido portado
a las placas de desarrollo mas populares y también cuenta con una versión para
x86 para [sistemas operativos tipo
UNIX](https://github.com/micropython/micropython/wiki/Getting-Started).

Se podría pensar en Micro Python como un microsistema operativo que se instala
en el micro-controlador y te entrega una
[Shell](https://es.wikipedia.org/wiki/Shell_de_Unix)
([REPL](https://es.wikipedia.org/wiki/REPL)) en la cual puede ejecutar comandos
y scripts. La conexión es serial-USB a través de un cable conectado al
computador, websokets u otro método.

Debido a que Micro Python es de código libre, cada versión portada por otros,
puede variar en sus librerías causando una especie similitud a lo que pasa en
el mundo de GNU/Linux con sus cientos de distribuciones.

Hay varias placas de desarrollo compatible con Micro Python, cada una tiene su
mercado y cubre necesidades generales o especificas.

 1. **[PyBoard](https://store.micropython.org/)**: Es la placa oficial, cuenta
    con ranura sd, y algunas versiones con acelerómetro.

 2. **[ESP](https://www.espressif.com/en/products/hardware/)**: Dos modelos
    principales esp32 y esp8622, se venden en forma de módulos, Pero también
    hay disponibles placas que ya los tienen instalados, para distintos tipos
    de necesidades.

 3. **[Wipy](https://pycom.io/webshop/)**: Especializado en el internet de las
    cosas, soporta 'wpa enterprise', y una construcción de calidad superior.

 4. **[Familia Stm32](http://micropython.org/stm32/)**: Placas de desarrollos
    generales y específicos

 5. **[Espruino Pico](https://www.espruino.com/Pico)**: micro placa de
    desarrollo, que corre por defecto una implementación de
    JavaScript(espruino).

 6. **[Micro:bit](https://microbit.org/es/)**: placa de desarrollo orientada
    a la educación, cuenta con todo un ecosistema,Editor de bloques y texto,
    firmware y hardware.

 7. **[Adafruit CircuitPython](https://www.adafruit.com/category/956)**: Se
    basan en los esp y el Atmel SAMD51 y cuenta con su propia versión de
    micropython orientado al aprendizaje y principiantes.

## Pros, Contras y Algo mas.

**Pros:** Unos de los puntos fuertes, es el rápido desarrollo de prototipos
funcionales, y todos los beneficios que trae programar en Python.

**Contras:** El uso de recursos de memoria y procesamiento es alto, pero te
permite trabajar cómodamente.( esto depende de la placa de desarrollo y la
versión de MicroPython)

**Algo más:** Las diferentes placas de desarrollo compatibles en el mercado,
pueden tener bibliotecas especificas, o versiones modificas adaptadas para sus
propios propósitos, por lo cual, una solución creada puede que no funcione del
todo o directamente no funcione en otra placa o fork de MicroPython, sin
embargo, a nivel de algoritmo tendrán gran compatibilidad, y solo será
necesario cambiar parte de la sintaxis correspondiente

## Algunos Videos.

### Ponencia de Jesus Cea, MicroPython PyconES.
<iframe width="560" height="315"
src="https://www.youtube.com/embed/gMyoixCvUVI" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

### ESP8622, luces led y botom.
<iframe width="560" height="315"
src="https://www.youtube.com/embed/8rDZ-Zuc4Eo" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

### Introducción Pycom.
<iframe width="560" height="315"
src="https://www.youtube.com/embed/KwIaljvmgFg" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

### Micro:bit Tutorial.
<iframe width="560" height="315"
src="https://www.youtube.com/embed/rduVCGLvV-4" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

### STM32F405RG Clon pyboard
<iframe width="560" height="315"
src="https://www.youtube.com/embed/Deer0qFbwC0" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

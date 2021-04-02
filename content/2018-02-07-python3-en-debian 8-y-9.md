---
layout:     post
title:      Compilación e instalacion Python3 en Debian 8 y 9
author:     pablo lira
image:      default.jpg
tags: 		python3, debian 
subtitle:  	desde un sistema base

---
<!-- Start Writing Below in Markdown -->



update: metodo compatible con debian 9

Esta instalación es realizada en debían 8 net-install … una versión de debían que incluye solamente  el sistema básico y utilidades del sistema, una versión muy utilizada en servidores, de igual forma es compatible  con las versiones  con escritorio. Primero actualizamos los repositorios y el sistema.
```bash
sudo apt-get update && sudo apt-get upgrade
```
Procedemos a descargar el paquete build-essential  que cumplirá las dependencia generales para compilar Python.
```bash
sudo apt-get install build-essential 
```
Se puede compilar e instalar solo con build-essential, pero instalaremos mas dependencias para obtener una compilacion mas compatible.
```bash
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev \
libssl-dev libsqlite3-dev tk-dev  libgdbm-dev libc6-dev \
libbz2-dev libffi-dev
```
Descargamos la fuentes de Python 3.6 directamente desde la pagina de Python.org.
```bash
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
#es caso de presentar error de certificados ignorarlos con 
wget --no-check-certificate https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
```
Ahora seguimos los pasos para descomprimir,  configurar las fuentes  para luego pasar a compilar  para poder realizar un instalación de los binarios.
```bash
tar xvf Python-3.6.3.tgz
cd Python-3.6.3
./configure --prefix=/usr/local  --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make -j4   #-j4 numeros de core a usar para compilar.
```
En python 3.6 se agrego una nueva opción  “--enable-optimizations”  en ./configure, que también fue portada a python3.5 y python2.7, esta opción  optimiza  para obtener un 10% mejor de rendimiento, pero hace que la compilación tarde mucho mas.

La opción  “-j4” de make especifica  la cantidad de núcleos a ocupar de la CPU,  para realizar una compilación mas rápida, si solo tienes uno con un simple "make" funcionara.
Para proceder con la instalación hay dos formas:
```bash
sudo make install # que instalara sobre-escribiendo configuraciones de python3 anteriores
sudo make altinstall # no cambia los enlaces simbolicos, evitando romper el sistema..
```
Os aconsejo usar la segunda para evitar conflictos a futuros con instalaciones propias del sistema.

Solo basta ejecutar en un terminal python3 o python3.6 y aparecerá la  Shell interactivo de Python!. Cabe mensionar que incluye por defecto pip3.


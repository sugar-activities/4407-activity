#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,time
url = raw_input("Escribe la URL del archivo a descargar:")

off = raw_input("Deseas apagar la XO cuando termine la descarga? (si o no)")

print "Las descargas van a:"
os.system("pwd")
time.sleep(3)
if off == "si":
	os.system("wget " + url)
	os.system("poweroff")
if off == "no":
	os.system("wget " + url)
	print "Hasta luego..."


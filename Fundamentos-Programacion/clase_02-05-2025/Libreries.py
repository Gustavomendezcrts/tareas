#from **library** import **comand** 
#import = solicitar solo un comando de la libreria (con * solicitas todos los comandos)
#con from seleccionas la libreria a utilizar
import os, random, time

print("Hola, soy una libreria")
time.sleep(2) #pausa el programa por 2 segundos
os.system("cls") #limpia la pantalla de la consola

print(random.randint(1, 10))
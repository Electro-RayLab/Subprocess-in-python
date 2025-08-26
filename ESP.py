#ejercicio 1

#import subprocess
#import platform

#ip_a_verificar = "8.8.8.8"

#if platform.system().lower() == "windows":
    #comando = ['ping', '-n', '1', ip_a_verificar]
#else:
    #comando = ['ping', '-c', '1', ip_a_verificar]

#resultado = subprocess.run(
    #comando,
    #capture_output=True,
    #text=True
#)

#exito = False
#if resultado.returncode == 0 and "ttl" in resultado.stdout.lower():
    #exito = True

#if exito:
    #print(f"Éxito: La IP {ip_a_verificar} es accesible.")
#else:
    #print(f"Fallo: No se pudo contactar a la IP {ip_a_verificar}.")



#ejercicio 2

#import subprocess
#import platform

#if platform.system().lower() == "windows":
    #comando = ['date', '/t']
#else:
    #comando = ['date']

#resultado = subprocess.run(
    #comando,
    #capture_output=True,
    #text=True,
    #shell = True
#)

#if resultado.returncode == 0:
    #fecha_hora_actual = resultado.stdout.strip()
    #print(f"La fecha y hora actual es: {fecha_hora_actual}")
#else:
    #print("No se pudo obtener la fecha y hora actual.")




#ejercicio 3

#import subprocess
#import os
#import platform

#if platform.system().lower() == "windows":
    #comando = ['cmd', '/c', 'echo %MiVariable%']
#else:
    #comando = ['sh', '-c', 'echo $MiVariable']

#mi_entorno = os.environ.copy()

#mi_entorno["MiVariable"] = "ValorSecreto123"

#resultado = subprocess.run(comando, capture_output=True, text=True, env=mi_entorno)

#if resultado.returncode == 0:
    #print(f"La variable MiVariable contiene: {resultado.stdout.strip()}")
#else:
    #print("No se pudo obtener la variable MiVariable.")


#ejercicio 4

import subprocess
import platform

if platform.system().lower() == "windows":
    comando = ['ping', '-n', '5', 'google.com']
else:
    comando = ['ping', '-c', '5', 'google.com']

proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, text=True)

for linea in proceso.stdout:
    print(f"[Salida]: {linea.strip()}")

proceso.wait()

print("Monitoreo terminado.")


















#Servidor 
import socket 
import datetime
import os
import platform

host="localhost"
port=8080
format = "utf-8"
size = 1024
#crear objeto llamado server<
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#recibe una tupla del host y el puerto
server.bind((host,port))
server.listen(1)
print("servidor en espera de conexiones nuevas")
active, addr = server.accept()
#creamos la lista de palabras claves con las cuales regresaremos las peticiones
while True:
    #se recibe la peticion del cliente
    recibido = active.recv(size).decode(format)
    print("Cliente: ", recibido)
    #proceso para obtener la hora 
    ahora = datetime.datetime.now()
    ahora_str = ahora.strftime('%d/%m/%Y %H:%M:%S')
    if(recibido == "time"):
        active.send(ahora_str.encode(format))
    #proceso para obtener la información del sistema del servidor
    elif(recibido == "os"):
        enviar = str(platform.system() + " " + platform.release() + ", " + platform.processor()) 
        active.send(enviar.encode(format))
    #proceso para obtener una lista de los directorios actuales
    elif (recibido == "ls"):
       enviar = str(os.listdir())
       active.send(enviar.encode(format))
    #proceso para salir de la conexion
    elif(recibido == "salir"):
        break
    #proceso normal para mandar mensajes
    else:
        enviar=input("Server: ")
        active.send(enviar.encode(format))

active.close()

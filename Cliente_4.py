import socket
import datetime

host = "localhost"
port = 8080
format = "utf-8"
size = 1024
#crear objeto llamado socket1
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#recibe una tupla del host y el puerto 
socket1.connect((host,port))
print("inicializando cliente")
#creamos el bucle infinito para conexión
while True:
    #creamos la variable enviar y le pedimos que "espere" a que el cliente escriba 
    enviar = input("Cliente: ")
    if(enviar == "salir"):
        print("saliendo")
        break
       
    #utilizamos la primitiva send para enviar por medio del socket la información
    socket1.send(enviar.encode(format))
    #vamos a recibir la respuesta del lado del servidor
    recibido = socket1.recv(size)
    print("Servidor: ", recibido.decode(format))
    
#cerramos la conexión
socket1.close()
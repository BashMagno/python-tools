import sys
from datetime import datetime
import socket

#POSIBLE ERROR EN LONGITUD DE ARGUMENTOS INICIALES

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Numero de parametros incorrecto ")
    print("Syntax = python3 ahmScanner.py <ip>")

print("=" * 50)
print("Realizando escan de puertos a :" + target)
print("=" * 50)
print("---------------REALIZADO POR M4GNO----------------")
print("=" * 50)
print("Empieza en el: " + str(datetime.now()))
print("=" * 50)

#COMIENZO DEL SCANNER

try:
    for puertos in range(0, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        aux = s.connect_ex((target, puertos))
        if aux == 0:
            print(f"Puerto {puertos} está abierto")
            s.close()
            
#POSIBLES ERRORES USER/COMPILE

except KeyboardInterrupt:
    print("\nAbandonando el programa...")
    sys.exit()
except socket.gaierror:
    print("Nombre de host no se resolvio correctamente")
    sys.exit()
except socket.error:
    print("No se pudo conectar con el servidor")
    sys.exit()

print("=" * 50)
print("Finalizado el escan de puertos a :" + target)
print("=" * 50)
print("---------------REALIZADO POR M4GNO----------------")
print("=" * 50)
print("Acabó en el: " + str(datetime.now()))
print("=" * 50)

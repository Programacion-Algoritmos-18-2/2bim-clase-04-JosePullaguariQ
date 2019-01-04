#Importamos la clases que vamos a utilizar
from paquete_archivos.miarchivo import *
from modelado.mimodelo import *

objLeer = MiArchivo()								#Creamos un objeto tipo MiArchivo para leer el archivo
objEscribir = MiArchivoEscribir() 					#Creamos un objeto tipo MiArchivo para escribir en el archivo

lista1 = objLeer.obtener_informacion()				#Declaramos una lista para alamacenar la informacion del objeto objLeer
lista1 = [l.split("|") for l in lista1]				#Separamos con el split los datos de la lista con el caracter "|""
lista_equipo = []									#Declaramos lista_equipo como una lista vacia

for d in lista1:									#Creamos un for para recorrer la lista
    e = Equipo(d[0], d[1], d[2], d[3])      		#Creamos un objeto p tipo Equipo y definimos que dato enviamos con su posicion al constructor de la clase Equipo
    lista_equipo.append(e)

#Creamos un objeto tipo Operaciones que contiene al metodo de ordenar
operacion = Operaciones(lista_equipo)

#Creamos un menu que pida que ingrese una opcion de ordenamiento
opcion = int (input("Desea ordenar por Nombre ingrese (1) / por Campeonato ingrese (2)\n"))
if (opcion == 1):													#Si la opcion es 1 realiza ordenamiento por Nombres
	lista2 = operacion.ordenarNombres()
	print("Ordenamiento por Nombres\n")				#Presentamos el ordenamiento			
	print(operacion.ordenarNombres())

if(opcion == 2 ):													#Si la opcion es 1 realiza ordenamiento por Campeonatos
	lista2 = operacion.ordenarCampeonatos()
	print("Ordenamiento por Campeonatos\n")			#Presentamos el ordenamiento
	print(operacion.ordenarCampeonatos())

#Recorremos con un for la lista ordenada	
for d in lista2:
	objEscribir.agregar_informacion(d)									#Enviamos con el objEscribir el objeto con la lista ordenada al metodo agregar informacion

objLeer.cerrar_archivo()												#Cerramos el archivo para leer
objEscribir.cerrar_archivo()											#Cerramos el archivo para escribir
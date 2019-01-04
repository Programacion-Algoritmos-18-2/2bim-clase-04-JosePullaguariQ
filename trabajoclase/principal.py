#Importamos la clases que vamos a utilizar
from paquete_archivos.miarchivo import *
from modelado.mimodelo import *


m = MiArchivo()								#Creamos un objetos m tipo MiArchivo
m2 = MiArchivoEscribir() 					#Creamos objeto para escribir el archivo

lista = m.obtener_informacion()				#Declaramos una lista para alamacenar la informacion del objeto m 
lista = [l.split("|") for l in lista]		#Separamos con el split los datos de la lista con el caracter "|""
lista = lista[0:]  							#Inicializamos la lista en la posicion 1
lista_equipo = []							#Declaramos lista_personas como una lista vacia

for d in lista:								#Creamos un for para recorrer la lista
    e = Equipo(d[0], d[1], d[2], d[3])      #Creamos un objeto p tipo Equipo y definimos que dato enviamos con su posicion al constructor de la clase Persona
    lista_equipo.append(e)


#Creamos un objeto tipo Operaciones para llamar al metodo de ordenar
operacion = Operaciones(lista_equipo)
print("Archivo de manera ordenada\n")							
print(operacion.ordenar())

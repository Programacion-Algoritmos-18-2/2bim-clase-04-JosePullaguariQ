import codecs
import sys

class MiArchivo:#Creamos la clase Miarchivo
    """
    """
    def __init__(self):#Constructor de la clase
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r")#Direccion del archivo que vamos a utilizar y lo leemos con la letra "r"

    def obtener_informacion(self):#Metodo para leer la informacion del archivo
        return self.archivo.readlines()

    def cerrar_archivo(self):#Metodo para cerrar el archivo
        self.archivo.close()


class MiArchivoEscribir:#Creamos la clase Mi Archivo escribir
    """
    """
    def __init__(self):#Constructor de la clase
        """
        """
        self.archivo = codecs.open("data/informacion2.csv", "a") #Direccion de alrchivo que va a escribir o para crearlo si no existe, utilizamos la letra "a"

    def agregar_informacion(self, e):#Metodo para escribir informacion al archivo
        self.archivo.write("%s - %s - %d - %d\n" % (e.nombres, e.ciudad,\
                e.campeonatos, e.numJugadores))

    def cerrar_archivo(self):#Metodo para cerrar el archivo
        self.archivo.close()

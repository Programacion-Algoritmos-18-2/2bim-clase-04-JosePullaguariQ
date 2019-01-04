class Equipo:#Creamos la clase equipo
    """
    """   
    def __init__(self, n, c, camp, numJ):#Contructor de la clase estudiante que recibe 4 atributos
        """
        """
        self.nombres = n
        self.ciudad = c
        self.campeonatos = int(camp)
        self.numJugadores = int(numJ)

    #Metodos de agregar y obtener para los atributos de la clase
    def agregar_nombres(self, n):#Metodo para agregar nombre
        """
        """
        self.nombres = n

    def obtener_nombres(self):#Metodo para obtener nombre
        """
        """
        return self.nombres

    def agregar_ciudad(self, n):#Metodo para agregar ciudad
        """
        """
        self.ciudad = n

    def obtener_ciudad(self):#Metodo para obtener ciudad
        """
        """
        return self.ciudad

    def agregar_campeonatos(self, n):#Metodo para agregar campeonatos
        """
        """
        self.campeonatos = int(n)

    def obtener_campeonatos(self):#Metodo para obtener campeonatos
        """
        """
        return self.campeonatos

    def agregar_numJugadores(self, n):#Metodo para agregar numJugadores
        """
        """
        self.numJugadores = int(n)

    def obtener_numJugadores(self):#Metodo para obtener numJugadores
        """
        """
        return self.numJugadores

    #Metodo str para presentar los datos 
    def __str__(self):
        #Imprimimos los atributos
        return "%s - %s - %d - %d" % (self.obtener_nombres(), self.obtener_ciudad(),\
                self.obtener_campeonatos(), self.obtener_numJugadores())

    #Metodo repr para el metodo sorted 
    def __repr__(self):
        #Imprimimos los atributos
        return "%s - %s - %d - %d\n" % (self.obtener_nombres(), self.obtener_ciudad(),\
                self.obtener_campeonatos(), self.obtener_numJugadores())


class Operaciones(object):#Creamos el objeto Operaciones
    def __init__(self, listado):#Contructor de la clase Operaciones que recibe listado
        self.listado_equipo = listado

    #Metodo para ordenar la lista por nombres
    def ordenarNombres(self):
        return sorted(self.listado_equipo, key = lambda equipo: equipo.nombres)

    #Metodo para ordenar la lista por campeonatos
    def ordenarCampeonatos(self):
        return sorted(self.listado_equipo, key = lambda equipo: equipo.campeonatos)
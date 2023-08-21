class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo")

    def get_edad(self):
        return self.__edad

    def set_dni(self, dni):
        if len(dni) == 9:
            self.__dni = dni
        else:
            print("El DNI debe tener 9 caracteres")

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.__titular.get_nombre())
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva")

# Ejemplo de uso
persona = Persona("Mateo", 21, "12312321")
cuenta = Cuenta(persona, 100000.0)

persona.mostrar()
print("¿Es mayor de edad?", persona.es_mayor_de_edad())

cuenta.mostrar()
cuenta.ingresar(500.0)
cuenta.retirar(200.0)

cuenta.mostrar()




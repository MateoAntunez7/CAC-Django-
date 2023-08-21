class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un valor positivo")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres")

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Ejemplo de uso
persona = Persona()
persona.set_nombre("Mateo")
persona.set_edad(21)
persona.set_dni("1212373773")

persona.mostrar()
print("¿Soy mayor de edad?")
if  persona.es_mayor_de_edad():
    print("¡Sos mayor de edad!")
else:
    print("Hay olorsito a recien nacido")
    
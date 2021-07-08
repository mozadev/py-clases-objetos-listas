
class Persona:
    def __init__(self,nombre,dia, mes , anio):
        self.nombre=nombre
        self.dia=dia
        self.mes=mes
        self.anio=anio


LISTAPERSONAS=[]
fecha=[]
diccionario={}

cant=int(input("ingrese canti personas: "))
for i in range(cant):
    nombre=input("ingrese nombre: ")

    dia=int(input("ingrese dia"))
    mes=int(input("ingrese mes "))
    anio=int(input("ingrese anio"))
    objPersona=Persona(nombre,dia,mes,anio)
    LISTAPERSONAS.append(objPersona)



mes=input("ingrese el mes: ")
print("lista de personas que cumplen anios")
for k in range(len(LISTAPERSONAS)):
    if(mes==LISTAPERSONAS[k].mes):
        print(LISTAPERSONAS[k].nombre)




#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°2 de la tarea 3 

from math import pi

def calcularDiametro(radio):
    diametro = radio*2
    return diametro
    
def calcularLongitud(radio):
    longitud = (2*pi)*radio
    return longitud
    
def calcularArea(radio):
    area = pi * (radio * radio) #int not callable http://stackoverflow.com/questions/9767391/typeerror-int-object-is-not-callable
    return area
    
def main():
    radio = float(input("Escribe el radio del circulo"))
    diam = calcularDiametro(radio)
    longi = calcularLongitud(radio)
    area = calcularArea(radio)
    print("Circulo con radio:", radio)
    print("Diametro:", diam)
    print("Circunferencia:", longi)
    print("Area:", area)
main()
    
    
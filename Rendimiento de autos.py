#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°4 de la tarea 3 



def rendimientokmlit (kmRecorridos, gasUtilizado):
    rendimientokm = kmRecorridos / gasUtilizado
    return rendimientokm
    
def rendimientoMillaGal (kmRecorridos, gasUtilizado):
    milla = kmRecorridos * 1.609344
    galon = gasUtilizado * 0.264172051
    rendimientoMilga = milla / galon
    return rendimientoMilga

def main():
    kmRecorridos = int(input("Kilometros recorridos"))
    gasUtilizado = float(input("Litros de gasolina utilizados"))
    rendimiento1 = rendimientokmlit (kmRecorridos, gasUtilizado)
    rendimiento2 = rendimientoMillaGal (kmRecorridos, gasUtilizado)
    print("si recorre", kmRecorridos, "con", gasUtilizado, ",")
    print("el rendimiento en km/l es:", rendimiento1)
    print("el rendimiento en mi/galon es:", rendimiento2)
    kmParaRecorrer = int(input("¿Cuantos Kilometros vas a recorrer"))
    litrosNe = kmParaRecorrer / rendimiento1
    print("para recorrer", kmParaRecorrer, "kms., necesitas", litrosNe,"litros")
main()
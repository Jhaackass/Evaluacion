import numpy as np
import random as rd

def comprarEntradas():


    return
def validar_rut(rut):
    rut_invertido=str(rut)[::-1]
    serie_multiplicadora=[2,3,4,5,6,7]
    suma = 0
    for i, digito in enumerate(rut_invertido):
        multiplicador=serie_multiplicadora[i % len(serie_multiplicadora)]
        suma += int(digito*multiplicador)

    resto=suma % 11
    digito_verificador= 11-resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador ==10:
        digito_verificador = 'k' 

    return digito_verificador

def mostrarUbicaciones():
    return
def verListadoAsistentes():
    return
def mostrarGanancias():
    return
lista_asientos_disponibles=list(range(0,101))
sw=0
while sw==0:
    print("\nBienvenido a ventas de entradas consierto Vip de MICHEAL JAM\n")
    print("1.-Compra de entradas")
    print("2.-Mostrar ubicacines disponibles")
    print("3.-ver listado de asistentes")
    print("4.-mostrar ganancias totales")
    print("5.-salir\n")
    op=int(input("ingrese una opcion: "))

    if op==1:
        print("opcion 1")
        cant_entradas=int(input("ingrese candidad de entradas: "))
        while cant_entradas > 3 or cant_entradas < 1:
            cant_entradas=int(input("ingrese nuevamente la cantidad de entradas: "))
        for i in range(cant_entradas):
            print(f"entrada {i+1}")
            print(lista_asientos_disponibles)
            print("\nLas categorias y precios de Entradas son los siguientes :\n")
            print("1.-platinum $120.000 (asiento del 1 al 20)")
            print("2.-Gold $80.000 (asiento del 21 al 50)")
            print("3.-Silver $50.000 (asiento del 51 al 100)")
            categoria=int(input("ingrese categoria: ")) 
            asiento=int(input("ingrese numero de asiento: "))
            rut=int(input("ingrese su rut sin puntos ni guion: "))
    if op==2:
        print("opcion2")
        print(lista_asientos_disponibles)
    if op==3:
        print("opcion3")
    if op==4:
        print("opcion4")
    if op==5:
        print("adios") 
        sw+=1   
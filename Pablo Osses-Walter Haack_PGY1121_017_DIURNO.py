"""
Pablo Osses
Walter Haack
"""
import random
def buscar(lista, patente):
    """
    dentro de la lista estan los dados de cada vehiculo , 
    cada elemento de la lista es otra lista

    """
    for i in lista:
        if i[1]== patente:
            print("VEHICULO ENCONTRADO IMPRIMIENDO DATOS")
            print(f"")
            print(f"Tipo: {i[0]}")
            print(f"Patente: {i[1]}")
            print(f"Marca: {i[2]}")
            print(f"Precio: {i[3]}")
            print(f"Fecha registro {i[4]}")
            print(f"Nombre_dueno: {i[5]}")
            if i[-1]==0:
                print("NO HAY MULTAS ASOCIADAS")
            else:
                """el ultimo elemento de la lista es una lista con las multas del vehiculo"""
                for x in i[-1]:
                    print(f"Fecha multa es : {x[0]}")
                    print(f"Precio multa es : {x[1]}")
            return
    return False
def i_certi(lista, patente):
    print("Tipo certificado:\n1-Emision de contaminantes\n2-antaciones vigentes\n3-multas")
    tipo_cert=0
    while tipo_cert not in [1,2,3]:
        tipo_cert=int(input("Ingrese Tipo certificado: "))

    if tipo_cert ==1:
        nombre_cert="Emision de contaminantes"
    if tipo_cert ==2:
        nombre_cert="2-antaciones vigentes"
    if tipo_cert ==3:
        nombre_cert="multas"
    precio_certificado=random.randint(1500,3500)
    for i in lista:
        if i[1]== patente:
            print("VEHICULO ENCONTRADO IMPRIMIENDO CERTIFICADO")
            print(f"")
            print("-------------CERTIFICADO-------------")
            print(f"CERTIFICADO: {nombre_cert}         PRECIO:{precio_certificado}\n")
            print(f"Tipo: {i[0]}")
            print(f"Patente: {i[1]}")
            print(f"Marca: {i[2]}")
            print(f"Precio: {i[3]}")
            print(f"Fecha registro {i[4]}")
            print(f"Nombre_dueno: {i[5]}")
            return
    return False

vehiculos=list()
sw=0
tipo=''
patente=''
marca=''
precio=''
#multas=list()
fecha_registro=''
nombre_dueno=''
while sw ==0:
    print("             ---Bienvenido a sistema de vehiculos---\n")
    print("1-grabar")
    print("2-buscar")
    print("3-imprimir certificados")
    print("4-salir")
    try:
        op=int(input("ELIJA UNA OPCION: "))
        if op ==1:
            actual=list()
            tipo=input("Ingrese tipo de vehiculo:")
            patente=input("Ingrese PATENTE FORMATO BBBB10 (ejemplo: RTUI89) ")
            while len(patente)!=6:
                print("PATENTE NO VALIDA")
                patente=input("Ingrese PATENTE FORMATO: BBBB10 (ejemplo: RTUI89): ")

            marca=input("Ingrese MARCA de vehiculo: ")

            while len(marca)<2 or len(marca)>15:
                print("MARCA NO VALIDA")
                marca=input("Ingrese MARCA de vehiculo: ")

            precio=int(input("Ingrese PRECIO de vehiculo: "))
            while precio<5000000:
                print("PRECIO NO VALIDO")
                precio=int(input("Ingrese PRECIO de vehiculo: "))

            fecha_registro=input("Ingrese FECHA REGISTRO de vehiculo: ")
            nombre_dueno=input("Ingrese NOMBRE DUEÑO de vehiculo: ")
            actual.append(tipo)
            actual.append(patente)
            actual.append(marca)
            actual.append(precio)
            actual.append(fecha_registro)
            actual.append(nombre_dueno)
            multas=list()
            multas_cant=int(input("¿Cuantas multas tiene el vehiculo?: "))
            if multas_cant > 0:
                for i in range(multas_cant):
                    fecha_multa=input(f"Ingrese FECHA de la multa {i+1} : ")
                    monto_multa=input(f"Ingrese MONTO de la multa {i+1} : ")
                    multas.append([fecha_multa,monto_multa])
                actual.append(multas)
            else:
                actual.append(0)
                print("NO HAY MULTAS ASOCIADAS")
            vehiculos.append(actual)


        if op ==2:
            """buscar"""
            patente=input("Ingrese PATENTE a buscar: ")
            ve=buscar(vehiculos, patente)
            if ve==False:
                print("El vehiculo no existe")

        if op ==3:
            """imprimir certificados"""
            patente=input("Ingrese PATENTE para generar certificado: ")
            ve=i_certi(vehiculos, patente)
            if ve==False:
                print("El vehiculo no existe")
        if op == 4:
            """salir"""
            sw=1
    except:
        print("OPCION INVALIDA (except)")
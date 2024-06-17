import json
cargos = ['ceo','analista','desarrollador']

def registrar_trabajador(trabajadores):
    nombre = input ("Ingrese el nombre del trabajador: ")
    cargo = input ("Ingrese cargo del trabajador (CEO/ANALISTA/DESARROLLADOR): ").lower()
    while cargo not in cargos:
        print ("Ingrese un cargo valido porfavor.")
        cargo = input ("Ingrese cargo del trabajador (CEO/ANALISTA/DESARROLLADOR): ").lower()

    sueldoBruto = int (input("Ingrese sueldo del trabajador: "))
    descuentoSalud = sueldoBruto * 0.07 
    descuentoAFP = sueldoBruto * 0.12
    sueldoLiquido = sueldoBruto - descuentoAFP - descuentoSalud
    print ("Datos ingresados correctamente")
    datos = {
        'nombre': nombre,
        'cargo' : cargo,
        'sueldo bruto' : sueldoBruto,
        'descuento salud' : descuentoSalud,
        'descuento AFP' : descuentoAFP,
        'sueldo liquido' : sueldoLiquido
    }
    trabajadores.append(datos)

def cambiarDatos(trabajadores):
        for trabajador in trabajadores:
            nombreTrabajador = input ("Ingrese el nombre del trabajador: ")
            if nombreTrabajador == trabajador['nombre']:
             print (trabajador)
             datoCambiar = input ("Que datos quiere cambiar? ")
             if datoCambiar == trabajador['nombre']:
              nuevo_nombre = input ("Ingrese nuevo nombre: ")
              if 'nombre' in trabajador:
                trabajador['nombre'].append(nuevo_nombre)
                print (trabajador)
              
              #valorNuevo = input ("A que valor quiere cambiarlo? ")
            
            #trabajador.append(valorNuevo)

def lista_trabajadores (trabajadores):
    print ("LISTA TRABAJADORES")
    for trabajador in trabajadores:
        print (trabajador)
nombreArchivo = 'planilla.txt'
def planilla (trabajadores):
    cargoseleccionado = input ("Ingrese el cargo que desea imprimir: ")
    if cargoseleccionado == "":
        trabajadoresImprimir = trabajadores

        
    elif cargoseleccionado in cargos:
        trabajadoresImprimir = []
        for trabajador in trabajadores:
            if trabajador['cargo'] == cargoseleccionado:
             trabajadoresImprimir.append(trabajadores)


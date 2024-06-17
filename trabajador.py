import info_trabajadores as fn

trabajadores = []

while True:
    print ("TRABAJADORES")
    print ("1- Registrar trabajador")
    print ("2- Lista de trabajadores")
    print ("3- Imprimir planilla de sueldos")
    print ("4- Cambiar datos")
    print ("")
    try:
     opcion = int (input("Ingrese opcion: "))
     if opcion == 1:
            fn.registrar_trabajador(trabajadores)
     elif opcion == 2:
            fn.lista_trabajadores(trabajadores)
     elif opcion == 3:
            fn.planilla(trabajadores)
     elif opcion == 4:
         fn.cambiarDatos(trabajadores)
    except ValueError:
       print ("Ingrese una opcion valida porfavor.")
import funciones as fn

pedidos = []

while True:
    print ("1- Registrar pedido")
    print ("2- Listar todos los pedidos")
    print ("3- Imprimir hoja de pauta")
    print ("4- Salir del programa")

    opcion = int (input("Ingrese la opcion: "))
    if opcion == 1:
        fn.registrar_pedidos(pedidos)
    elif opcion == 2:
        fn.listar_pedidos(pedidos)
    elif opcion == 3:
        fn.ruta_pedidos(pedidos)
    elif opcion == 4:
        print ("Saliendo...")
        break
    
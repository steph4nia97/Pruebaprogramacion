
comunas = "centro","colina","industria"
cilin_5 = []
pedido = {}
cilindro_5 = 1
cilindro_15 = 1
cilindro_45 = 1
conta = 0
def registrar_pedidos(pedidos):
    opcion = input("Desea agregar un pedido? si/no: ")
        
    while opcion == "si":
     nombre = input("Ingrese nombre y apellido del cliente: ")
     comuna = input("Ingrese la comuna del reparto (centro/colina/industria): ").lower()
     comunas = "centro","colina","industria"
     if comuna is not comunas:
         print ("Ingrese una comuna dentro del rango porfavor")
         comuna = input("Ingrese la comuna del reparto (centro/colina/industria): ").lower()
     else:
            print ("Comuna agregada.")

     cilindro = int(input("Ingrese el tamaño del cilindro (5/15/45): "))
#     if cilindro == 5:
#          cilindro_5 = cilindro_5 + conta
#     elif cilindro == 10:
#          cilindro_15 = cilindro_15 + conta
#     elif cilindro == 45:
#          cilindro_45 = cilindro_45 + conta

     cantidad_cilindro = int (input("Cuantos cilindros va a querer? "))
          
          
     opcion = input("Desea agregar otro pedido? (si/no) ").lower()
     if opcion == "no":
                print ("pedido ingresado")
            

    pedidos.append({
             'nombre':nombre,
             'comuna': comuna,
             'cilindro': cilindro,
             'cantidad cilindro': cantidad_cilindro
            })



def listar_pedidos(pedidos):
    print(pedidos)

ruta_centro = []
def ruta_pedidos(pedidos):
    comuna_ruta = input("Ingrese la comuna de ruta: ")
    if comuna_ruta == "centro":
        with open ('pedidos.txt','w') as archivo:
            archivo.write(f"nombre': {pedidos['nombre']}")  
            archivo.write(f"comuna': {pedidos['comuna']}")
            archivo.write(f"cilindro': {pedidos['cilindro']}") 
            archivo.write(f"cantidad cilindro': {pedidos['cantidad cilindro']}")        
    elif comuna_ruta == "colina":
        with open ('pedidos.txt','w') as archivo:
            archivo.write(f"nombre': {pedidos['nombre']}")  
            archivo.write(f"comuna': {pedidos['comuna']}")
            archivo.write(f"cilindro': {pedidos['cilindro']}") 
            archivo.write(f"cantidad cilindro': {pedidos['cantidad cilindro']}")    
    elif comuna_ruta == "industria":
         with open ('pedidos.txt','w') as archivo:
           archivo.write(f"nombre': {pedidos['nombre']}")  
           archivo.write(f"comuna': {pedidos['comuna']}")
           archivo.write(f"cilindro': {pedidos['cilindro']}") 
           archivo.write(f"cantidad cilindro': {pedidos['cantidad cilindro']}")   
         

             
             


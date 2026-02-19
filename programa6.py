#1. Declaración o uso de variables 
    #base_mayor: int
    #base_menor: int
    #altura: int  

#2.Entrada de datos 
base_mayor = int(input("Ingrese la base_mayor del triángulo: "))
base_menor = int(input("Ingrese la base_menor del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))

#3.Proceso de cálculo
area=((base_mayor+base_menor)*altura)/2

#4.Salida de resultados 
print("BASE_MAYOR: ", base_mayor)
print("BASE_MENOR: ", base_menor)
print("ALTURA:", altura)
print("ÁREA:", area)
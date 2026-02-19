#Diseñe un algoritmo que determine el monto a pagar por la compra de cierta cantidad de unidades de un producto 


#1. DECLARACIÓN O USO DE VARIABLES
    #cantidad : int (enteros)
    #precio : float (decimales)
    #monto_pagar : float
    

#2. ENTRADA DE DATOS
cantidad = int(input("Ingrese la cantidad de productos a adquirir: "))
precio = float(input("Ingrese el precio del producto: "))

#3. PROCESO DE CÁLCULO
monto_pagar= cantidad * precio

#4. SALIDA DE RESULTADOS
print("CANTIDAD:", cantidad)
print("PRECIO:", precio)
print("MONTO A PAGAR:", monto_pagar)

print("ola")
#1. Declaración o uso de variables 
    #producto1:float
    #producto2:float
    #producto3:float
    #producto4:float
    #producto5:float
    #subtotal: float
    #igv: float
    #total_pagar: float

#2.Entrada de datos 
producto1 = float(input("Ingrese el valor en soles del primer producto: "))
producto2 = float(input("Ingrese el valor en soles del segundo producto: "))
producto3 = float(input("Ingrese el valor en soles del tercer producto: "))
producto4 = float(input("Ingrese el valor en soles del cuarto producto: "))
producto5 = float(input("Ingrese el valor en soles del quinto producto: "))

#3.Proceso de cálculo
subtotal= producto1+producto2+producto3+producto4+producto5
igv=0.18 * subtotal
total_pagar= subtotal+ igv

#4.Salida de resultados 
print("El SUBTOTAL de dicha compra es:", subtotal, "nuevos soles") 
print("El IGV de dicha compra es:", igv, "nuevos soles") 
print("EL TOTAL A PAGAR por dicha compra es:", total_pagar, "nuevos soles")
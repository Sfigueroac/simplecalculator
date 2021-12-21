def sumar():
    sum1 = int(input("Escriba el sumando uno: "))
    sum2 = int(input("Escriba el sumando dos: "))
    print ("La Suma es:", sum1=sum2)

def restar():
    minuendo = int(input("Escriba el minuendo"))
    sustraendo = int(input("Escriba el sustraendo: "))
    print ("El resultado de la resta es ", minuendo-sustraendo)

def multiplicar(): 
    multiplicando = int(input("Escriba el multiplicando: "))
    multiplicador = int(input("Escriba el multiplicador: "))
    print ("El resultado de la multiplicación es: ", multiplicando*multiplicador)

def dividir():
    try:
        dividendo = int(input("Escriba el dividendo: "))
        divisor = int(input("Escriba el divisor: "))
        print ("El resultado de la división es: ")
    except ZeroDivisionError: 
        print ("ERROR: NO SE PUEDE DIVIDIR POR CERO")
def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opción:"))
        if (opc==1):
            sumar()
        elif(opc==2):
            restar()
        elif(opc==3):
            multiplicar()
        elif(opc==4):
            dividir()
        elif(opc==5):
            fin = 1

print("""**********
Calculadora
**********
Menu
1) Suma
2) Resta
3) Multiplicación
4) División
5) Salir""")
Calculadora ()

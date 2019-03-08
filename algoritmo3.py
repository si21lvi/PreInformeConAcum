#Algoritmo que lea 5 números e imprima el mayor número leído.
print("A continuación se presenta un algoritmo que lee 5 números e imprime el mayor número leído")
n1=float(input("Ingrese el primer número"))
n2=float(input("Ingrese el segundo número"))
n3=float(input("Ingrese el tercer número"))
n4=float(input("Ingrese el cuarto número"))
n5=float(input("Ingrese el quinto número"))
if (n1>n2 and n1>n3 and n1>n4 and n1>n5):
   print('El mayor es', n1)
if (n2>n1 and n2>n3 and n2>n4 and n2>n5):
   print('El mayor es', n2)
if (n3>n1 and n3>n2 and n3>n4 and n3>n5):
   print('El mayor es', n3)
if (n4>n1 and n4>n2 and n4>n3 and n4>n5):
   print('El mayor es', n4)
if (n5>n1 and n5>n2 and n5>n3 and n5>4):
   print('El mayor es', n5)
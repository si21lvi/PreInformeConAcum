print("Algoritmo que imprime los primeros diez pares entre 1 y 30")
cont=0
num=1
while num<=30:
  if num%2==0:
    print(num)
    if num>=20:
     break
  cont=cont+1
  num=num+1


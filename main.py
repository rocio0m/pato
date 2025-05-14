numero1=3
numero2=4
suma=(numero + numero2)
print(suma)
#menor<
#mayor>
#igual

print("ingrse un numero")
numero1=int(input())
#print("ingrese otro numero")
numero2=int(input("ingrese otro numero"))
suma=(numero1 + numero2)
print("la suma de estos numeros da ",suma)
menor = numero1 < numero2
mayor = numero1 > numero2
igual = numero == numero2
#igual ==
#print("tal es mayor que tal",suma)
if mayor:
    print("numero1 es maoyr que numero2")
if igual:
    print("numero1 es igual que numero2")
if menor:
    print("numero1 es menor que numero2")
    
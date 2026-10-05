"Bucles con estructura for"

"""This is a simple excercise about the cicle FOR"""
contador = 0
suma = 0
for i in range (2,26,2):
    print(i)
    contador +=1
    suma +=i
print("la suma es ",suma)
print("El promedio es de ",suma/contador)

"""Same excersice but in  LIST COMPREHENSION"""
numeros=[o for o in range(2,26,2)]
suma1=sum(numeros)
contador1=len(numeros)

print("La suma de tus numeros es ", suma1)
print("El promedio de estos es de ", suma1/contador1)

"Second exercise"
for e in "David Corona":
    print(e,end=" ")

"now in list comprehension"
nombre=[a for a in "David Coronas"]
print(nombre)

"Now i do a excercise in wich a text is covered cheking that is an a email"
contador2=0
for u in "davidcoron4@gmail.com":
    if u=='@':
        contador2+=1

if contador2==1:
        print("\n La direccion de correo es valida")
else:
        print("\n La direccion de correo no es valida")

"The same excersise but in list comprehension"
arrobas=[t for t in "davidcoron4@gmail.com" if t=="@"]
if len(arrobas)==1:
     print("\n la direccion de correo es valida")
else:
     print("\n La direccion de correo no es valida")

"Other excersice but the same estructre"

suma3=0

for r in range (3):
     num=int(input("ingresa un numero"))
     suma3+=num
     print("la suma de tu numero es",suma3)

""""""
numeros2 =[int(input("Ingresa un numero"))for w in range (3)]
suma4 = sum(numeros2)
print ("La suma de tus numeros es",suma4)

""""""
palbras =["Python","Code","Sol","Computadora","desarrollo"]
palabras_largas=[]

for p in palbras:
     if len(p)>5:
          palabras_largas.append(p)
print(palabras_largas)

""""""
palabras2=["Python","Code","Sol","Computadora","Desarrollo"]
palabras_largas2=[l for l in palabras2 if len(p) >5]
print(palabras_largas2)


a = [[0] * 3] * 3
print("Antes:", a)

a[0][0] = 1
print("Después:", a)

# Crearmos un generador
gen = (x for x in range(3))

print("Primera iteración:")
for num in gen:
    print(num)

print("\nSegunda iteración:")
for num in gen:
    print(num)
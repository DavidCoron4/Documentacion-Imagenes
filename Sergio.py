from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect

def palabras_frecuentes(palabras,K):
    conteo =Counter(palabras)

    top_K = conteo.most_common(K)

    return[palabra for palabra, frecuencia in top_K]
lista_prueba=["manzana","pera","manzana","uva","pera","manzana","platano"]
resultado = palabras_frecuentes(lista_prueba,2)

print(f"Las 2 palabras mas frecuentes son {resultado}")

ventana = deque(maxlen=3)
datos = [10,20,30,40,50]

for dato in datos:
    ventana.append(dato)
    print(f"Llego {dato} -> ventana actual : {list(ventana)}")

def agrupar_anagramas(palabras):
    grupos = defaultdict(list)
    for palabra in palabras:
        clave = "".join(sorted(palabra))
        grupos[clave].append(palabra)
    return list(grupos.values())
palabras=["amor","roma","perro","mora","prore"]
resultado1=agrupar_anagramas(palabras)
print(f"Anagramas agrupados: {resultado1}")

def k_es_mayor(nums,k):
    return heapq.nlargest(k,nums)[-1]

numeros=[3,2,1,5,6,4]
k=2
resultado2= k_es_mayor(numeros,k)
print(f"El {k} numero mas grande es : {resultado2}")

def buscar_rango(numb, objetivo):
    inicio= bisect.bisect_left(numb, objetivo)

    if inicio == len(numb) or numb[inicio] != objetivo:
        return  [-1,-1]
    fin= bisect.bisect_right(numb,objetivo) 
    return[inicio,fin]

numeros_ordenados = [1,2,2,2,3,4]
objetivo = 2
resultado3 = buscar_rango(numeros_ordenados,objetivo)

print(f"El rango del numero {objetivo} es {resultado3}")
"""

from collections import Counter
palabras =["manzana","pera","manzana","uva","pera","manzana","platano"]

mas_frecuentes = Counter("abracadabra").most_common(1)
print(mas_frecuentes)
"""
"""
from collections import deque
fila = deque(["Ana","Carlos","Sofia"])
fila.appendleft("Elena")
atendido=fila.popleft() 

print(f"Cliente atendido adios {atendido}")
print(f"Fila restante {list(fila)}")

fila1 = deque(["Cliente1","Cliente2","Cliente3"])
fila1.append("Cliente4")
print(f"Bienvenido a la fila {list(fila1)}")
atendido1=fila1.popleft()
print(f"Que tenga un buen dia {atendido1}")
"""
"""
import heapq
notas =[20,5,10,1,15]
top_2_max = heapq.nlargest(2,notas)
print(top_2_max)
top_2_min= heapq.nsmallest(2,notas)
print(top_2_min)
"""
"""
import bisect
alturas = [150,160,170,170,170,180,190]
idx_izq=bisect.bisect_left(alturas,170)
print(f"bisect_left devuelve {idx_izq}")

idx_der=bisect.bisect_right(alturas,170)
print(f"idx_derecha devuelve {idx_der}")

notas=[60,70,80,80,80,90,100]
idx_izq1=bisect.bisect_left(notas,80)
print(f"idx_left1 devuelve {idx_izq1}")
idx_der1=bisect.bisect_right(notas,80)
print(f"idx_right1 devuelve {idx_der1}")
"""

from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print (fibonacci(50))

def suma_hasta(n):
    if n<=1:
        return n
    return n + suma_hasta(n-1)
resultado = suma_hasta(5)
print(f"La suma hasta 5 es de {resultado}")
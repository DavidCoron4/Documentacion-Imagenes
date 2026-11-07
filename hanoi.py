def hanoi(n: int, origen: str, destino: str, auxiliar: str):

    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    hanoi(n - 1, origen, auxiliar, destino)

    print(f"Mover disco {n} de {origen} a {destino}")

    hanoi(n - 1, auxiliar, destino, origen)

hanoi(3, "A", "C", "B")
import time
from functools import lru_cache


def fib_naive(n):
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

start = time.time()
print("Resultado naive (n=35):", fib_naive(35))
print(f"Tiempo sin caché: {time.time() - start:.4f} segundos\n")

start = time.time()
print("Resultado con caché (n=35):", fib_memo(35))
print(f"Tiempo con lru_cache: {time.time() - start:.6f} segundos")

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_explicit_stack(n):
    stack = []
    
    current = n
    while current > 1:
        stack.append(current)
        current -= 1
        
    result = 1
    while stack:
        val = stack.pop()
        result *= val
        
    return result
print(factorial_explicit_stack(5)) 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: TreeNode) -> list[int]:
    res = []
    
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
        
    dfs(root)
    return res


root = TreeNode(1, TreeNode(2), TreeNode(3))
print(preorderTraversal(root))
def inorderTraversal(root: TreeNode) -> list[int]:
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)         
        res.append(node.val)   
        dfs(node.right)        
    dfs(root)
    return res

def postorderTraversal(root: TreeNode) -> list[int]:
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)         
        dfs(node.right)        
        res.append(node.val)   
    dfs(root)
    return res

from collections import deque

def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])  
    
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()  
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
        
    return result

def maxDepth(root: TreeNode) -> int:

    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)
    
    return root

def isValidBST(root: TreeNode) -> bool:
    
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node:
            return True

        if not (low < node.val < high):
            return False
        
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))

    return validate(root)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs_graph(node, graph, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return
    
    print(node, end=" ")  
    visited.add(node)     
    

    for neighbor in graph[node]:
        dfs_graph(neighbor, graph, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido DFS en el grafo:")
dfs_graph('A', graph)

from collections import deque

def bfs_graph(start_node, graph):
    visited = set()
    queue = deque([start_node])
    

    visited.add(start_node)
    
    print("Recorrido BFS en el grafo:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        # Recorremos a todos sus vecinos
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs_graph('A', graph)
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0
    
    def dfs(r, c):

        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            grid[r][c] == '0' or 
            (r, c) in visited):
            return

        visited.add((r, c))
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)


    for r in range(rows):
        for c in range(cols):
            
            if grid[r][c] == '1' and (r, c) not in visited:
                island_count += 1
                dfs(r, c)  
                
    return island_count


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print("Número de islas:", numIslands(grid))  
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:

    pre_map = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        pre_map[course].append(prereq)
        
    visit_status = {}

    def dfs(course):

        if visit_status.get(course) == 1:
            return False

        if visit_status.get(course) == 2:
            return True
        
        visit_status[course] = 1
        
        for prereq in pre_map[course]:
            if not dfs(prereq):
                return False
           
        visit_status[course] = 2
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
            
    return True

print(canFinish(2, [[1, 0]])) 

print(canFinish(2, [[1, 0], [0, 1]]))  

import heapq

def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

weighted_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

print("Distancias más cortas desde el nodo 'A':")
print(dijkstra(weighted_graph, 'A'))

class UnionFind:
    def __init__(self, n):

        self.parent = list(range(n))
 
        self.rank = [1] * n

    def find(self, i):

        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  
        return self.parent[i]

    def union(self, i, j):
        
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        return True

uf = UnionFind(5)  
print(uf.union(0, 1)) 
print(uf.union(1, 2))  
print(uf.find(0) == uf.find(2))  
print(uf.union(0, 2))  

def subsets(nums: list[int]) -> list[list[int]]:
    resultado = []
    
    def backtrack(start, ruta_actual):

        resultado.append(list(ruta_actual))
        
        for i in range(start, len(nums)):
            # Elegir
            ruta_actual.append(nums[i])
            
            backtrack(i + 1, ruta_actual)
            
            ruta_actual.pop()

    backtrack(0, [])
    return resultado

print("Subconjuntos de [1, 2, 3]:")
print(subsets([1, 2, 3]))

def climbStairs(n: int) -> int:

    memo = {}
    
    def dp(i):

        if i == 1:
            return 1
        if i == 2:
            return 2
        
        if i in memo:
            return memo[i]
        
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)

print("Formas de subir 5 escalones:", climbStairs(5))  
def climbStairsBottomUp(n: int) -> int:
    if n <= 2:
        return n

    prev2 = 1 
    prev1 = 2  
    
    current = 0
    for i in range(3, n + 1):
        current = prev1 + prev2  
        prev2 = prev1            
        prev1 = current
        
    return current

print("Formas de subir 5 escalones (Bottom-Up):", climbStairsBottomUp(5))  

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len

def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged
# Patrón clásico: Invertir una Lista Enlazada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current:
        next_temp = current.next  
        current.next = prev       
        prev = current            
        current = next_temp       
        
    return prev 
def fib_iterative_stack(n):
    if n <= 1:
        return n
    
    stack = [n]
    memo = {}
    
    while stack:
        curr = stack.pop()
        if curr <= 1:
            memo[curr] = curr
        elif curr not in memo:
            if (curr - 1) in memo and (curr - 2) in memo:
                memo[curr] = memo[curr - 1] + memo[curr - 2]
            else:
                stack.append(curr)
                stack.append(curr - 1)
                stack.append(curr - 2)
                
    return memo[n]

import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_optimized(n):
    if n < 2:
        return n
    return fib_optimized(n - 1) + fib_optimized(n - 2)

start = time.time()
resultado = fib_optimized(40)
end = time.time()

print(f"Resultado: {resultado}")
print(f"Tiempo con @lru_cache: {end - start:.8f} segundos") 
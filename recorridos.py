class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def preOrderTravesal(root: TreeNode)->list:
    res=[]
    def helper(node):
        if not node:
            return
        res.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return res
def inOrderTravesal(root: TreeNode) -> list:
    res = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)
    return res
def postOrderTravesal(root: TreeNode) -> list:
    res = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)
    return res

def preOrderTravesalIterative(root: TreeNode) ->list:
    if not root:
        return []
    stack, res =[root],[]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
    
def inOrderTravesalIterative(root: TreeNode) -> list:
    res, stack = [],[]
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def postOrderTravesalInterative(root: TreeNode) -> list:
    if not root:
        return[]
    stack,res = [root],[]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]

from collections import  deque

def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(current_level)
    return res

def maxDepth(root: TreeNode) ->int:
    if not root:
        return 0
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return 1 + max(left_height,right_height)

class Codec:
    def serialize(self,root: TreeNode) -> str:
        "Codifica un arbol en una mimsa cadena"
        res =[]

        def dfs(node):
            if not node:
                res.append("None")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
    def deserialize(self,data: str) -> TreeNode:
        "decoficiacion de la cadena de texto para construir un arboñ"
        vals = deque(data.split(","))

        def dfs():
            val = vals.popleft()
            if val == "None":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
def inverTree(root: TreeNode)-> TreeNode:
    if not root:
        return None
    root.left,root.right = root.right,root.left
    inverTree(root.left)
    inverTree(root.right)
    return root
def diameterOfBinaryTree(root: TreeNode) ->int:
    diameter = [0]

    def dfs(node):
        if not node:
            return 0
        left_hight = dfs(node.left)
        right_hight = dfs(node.right)

        diameter[0] = max(diameter[0],left_hight + right_hight)
        return 1 + max(left_hight,right_hight)
    dfs(root)
    return diameter[0]
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
def isBalanced(root: TreeNode) -> bool:
    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        if left_height == -1:
            return -1
        right_height = dfs(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height,right_height)
    return dfs(root) !=1
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Arbol de pruebas")
    print("Pre-order recursivo:",preOrderTravesal(root))
    print("Pre-order iterativo:",preOrderTravesalIterative(root))
    print("Level-order (BFS):",levelOrder(root))
    print("Altura maxima",maxDepth(root))
    print("Esta balanceado",isBalanced(root))

    codec = Codec()
    serialized = codec.serialize(root)
    print("Serializado:",serialized)

    deserealized = codec.deserialize(serialized)
    print("Level-order despues de deserealizar:",levelOrder(deserealized))
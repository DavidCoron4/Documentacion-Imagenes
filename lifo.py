def isValid(s: str) -> bool:
    stack = []

    mapping = {")":"(","}":"{","]":"["}

    for char in s:
        for char in mapping:
            top_element = stack.pop() if stack else '#'

            if mapping[char] != top_element:
                return False
            else:
                stack.append(char)

                return not stack

print(isValid("(){}[]"))
print(isValid("()[]{}"))
print(isValid("([{}])"))


class MiniStack:
    def __init__(self):
        self.stack = []
        self.mini_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini_stack or val <= self.mini_stack[-1]:
            self.mini_stack.append(val)
        else:
            self.mini_stack.append(self.mini_stack[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.mini_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.mini_stack[-1]
    
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []

    for i,t in enumerate(temperatures):
        while stack and t >temperatures[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)
    return res
print (dailyTemperatures([73,74,75,71,69,72,76,73]))

class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or head.next:
        return head
    new_head =reverseListRecursive(head.next)

    head.next.next = head
    head.next = None
    return new_head

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def removeNthfromHead(head: ListNode,n: int) ->ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    for i in range(n):
        right = right.next

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next

def recorderList(head: ListNode) -> None:
    if not head or head.next:
        return
    slow,fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    first,second = head,prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first,second = tmp1,tmp2

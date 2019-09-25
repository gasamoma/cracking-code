#Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
#an additional temporary stack, but you may not copy the elements into any other data structure
#(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
# do I implement inside ot outside function that receives the stack A: outside
# only numbers? A: Yes
# il use my writen stack class it has the same methods
# if i could moddify the add method ill simply traverse the stack until i can fit the element sorted
# I could implement merge sort for stacks, tho im going to first sort it with brute force
class LList:
    value=None
    next=None
    def __init__(self):
        pass
    def print_list(self):
      if self.next is None:
        print(self.value)
        return
      print(self.value, end=' ')
      return self.next.print_list()

class NClassicStack:
  def __init__(self):
    self.head = None
  def push(self, value):#this is O(1)
    new_head = LList()
    new_head.value=value
    new_head.next = self.head
    self.head = new_head
  def pop(self): #this is O(1)
    if self.head is None:
      return None
    value = self.head.value
    self.head = self.head.next
    return value
  def peek(self): #this is O(1)
    if self.head is None:
      return None
    return self.head.value
  def is_empty(self):#this is O(1)
    if self.head is None:
      return True
    return False
  def print_stack(self):
    if self.head is None:
      return
    return self.head.print_list()

def sort_stack(stack):#this is O(n*n)
    swapper = NClassicStack()
    result = NClassicStack()
    while not stack.is_empty() or not swapper.is_empty(): #this is O(n)
        max = None
        if stack.is_empty():
            max = swapper.pop()
            while not swapper.is_empty(): #this is O(n)
                current = swapper.pop() #this is O(1)
                if current > max:
                    stack.push(max)#this is O(1)
                    max = current
                else:
                    stack.push(current) #this is O(1)
        else:
            max = stack.pop()
            while not stack.is_empty(): #this is O(n)
                current = stack.pop() #this is O(1)
                if current > max:
                    swapper.push(max)#this is O(1)
                    max = current
                else:
                    swapper.push(current) #this is O(1)
        result.push(max)
    return result

st=NClassicStack()
st.push(4)
st.push(3)
st.push(6)
st.push(7)
st.push(9)
st.push(8)
st.push(1)
st.print_stack()# 1 8 9 7 6 3 4
st=sort_stack(st)
st.print_stack() # 1 3 4 6 7 8 9
print(st.pop())#1
print(st.pop())#3
print(st.pop())#4
print(st.pop())#6
print(st.pop())#7
print(st.pop())#8
print(st.pop())#9
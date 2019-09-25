#Stack Min: How would you design a stack which, in addition to push and pop, has a function 
#min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
#Does the data type inserted in the stack is an object? i.e. string? A:No, just simple data
#only positive values? A:NO
# the entire stack is the same data type? A:yes
# do i return the min elem index or value A: value
class NClassicStack:
  def __init__(self):
    self.head = None
    self.next = None
    self.value = None
  def push(self, value):
    new_head = NClassicStack()
    new_head.value=value
    new_head.next = self.head
    self.head = new_head
  def pop(self):
    if self.head is None:
      return None
    value = self.head.value
    self.head = self.head.next
    return value
  def peek(self):
    if self.head is None:
      return None
    return self.head.value
  def is_empty(self):
    if self.head is None:
      return True
    return False
  def print_stack(self):
    if self.head is None:
      return
    if self.head.next is None:
      print(self.value, end='')
      return
    print(self.head.value, end='')
    return self.head.next.print_stack

class stack:
  def __init__(self):
     self.stack=NClassicStack()
     self.mini=NClassicStack()
  def push(self, value):#O(1)
    if self.mini.peek() is None or self.mini.peek() >= value:
      self.mini.push(value)
    self.stack.push(value)
    return True
  def pop(self):#O(1)
    if self.stack.is_empty():
      return None
    if self.mini.peek()==self.stack.peek():
      self.mini.pop()
    return self.stack.pop()
  def min(self):#O(1)
    return self.mini.peek()

st = stack()
st.push(6)
st.push(3)
st.push(3)
st.push(2)
st.push(8)
st.push(0)
st.push(-50)
st.push(-20)
print(st.pop())#-20
print(st.pop())#-50
print(st.pop())#0
print(st.pop())#8
print(st.min())#2
#when you dont know the answer use yourself in a simpler version XD
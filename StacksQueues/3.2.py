#Stack Min: How would you design a stack which, in addition to push and pop, has a function 
#min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
#Does the data type inserted in the stack is an object? i.e. string? A:No, just simple data
#only positive values? A:NO
# the entire stack is the same data type? A:yes
# do i return the min elem index or value A: value
class classic_stack:
  def __init__(self):
     self.stack=[]
  def push(self, value):#O(1)
    self.stack.insert(0,value)
    return True
  def pop(self):#O(1)
    if len(self.stack) == 0:
      return None
    return self.stack.pop(0)
  def peek(self):#O(1)
    if len(self.stack) == 0:
      return None
    return self.stack[0]
class stack:
  def __init__(self):
     self.stack=[]
     self.mini=classic_stack()
  def push(self, value):#O(1)
    if self.mini.peek() is None or self.mini.peek() >= value:
      self.mini.push(value)
    self.stack.insert(0,value)
    return True
  def pop(self):#O(1)
    if len(self.stack) == 0:
      return None
    if self.mini.peek()==self.stack[0]:
      self.mini.pop()
    return self.stack.pop(0)
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
print(st.stack) # [-20, -50, 0, 8, 2, 3, 3, 6]
print(st.mini.stack) # [-50, 0, 2, 3, 3, 6]
print(st.pop())#-20
print(st.pop())#-50
print(st.pop())#0
print(st.min())#2
print(st.stack) # [8, 2, 3, 3, 6]
#when you dont know the answer use yourself in a simpler version XD
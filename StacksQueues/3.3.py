#Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might 
#topple. Therefore, in real life, we would likely start a new stack when the previous stack 
#exceeds some threshold. Implement a data structure SetOfStacks that mimics this. 
#SetO-fStacks should be composed of several stacks and should create a new stack once the 
#previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave 
#identically to a single stack (that is, pop () should return the same values as it would 
#if there were just a single stack).
#FOLLOW UP
#Implement a function popAt ( int index) which performs a pop operation on a specific 
# sub-stack
# What u mean by plate in the code a number? or u want a plate itself, the object A:object
# by default how many plates? A: let me decide in the class
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
class SetOfStacks:
  def __init__(self,st_max):
    self.st_max=st_max
    self.stack=[classic_stack()]
    self.cur_stack=0
    self.stack_size=0
  def push(self,value):
    if  self.st_max == self.stack_size:
      self.stack.append(classic_stack())
      self.cur_stack+=1
      self.stack_size=0
    self.stack[self.cur_stack].push(value)
    self.stack_size+=1
  def pop(self):
    if self.cur_stack==0 and self.stack<0:
      return None
    ret = self.stack[self.cur_stack].pop()
    if ret is None:
      self.stack.pop(self.cur_stack)
      self.cur_stack-=1
      self.stack_size=self.st_max
      ret = self.stack[self.cur_stack].pop()
    self.stack_size-=1
    return ret
  def pop_at(self,index):
    if self.cur_stack<index:
      return None
    ret = self.stack[index].pop()
    if ret is None:
      self.stack.pop(index)
      self.cur_stack-=1
    self.stack_size-=1
    return ret

class Plate:
  def __init__(self,value):
    self.name=value
  def __repr__(self):
        return "Plate({0})".format(self.name)
  def __str__(self):
      return "Plate: {0}".format(self.name)

st=SetOfStacks(3)
st.push(Plate("1"))
st.push(Plate("2"))
st.push(Plate("3"))
st.push(Plate("4"))
st.push(Plate("5"))
st.push(Plate("6"))
st.push(Plate("7"))
st.push(Plate("8"))
st.push(Plate("9"))

for stt in st.stack:
  print(stt.stack)
  #[Plate(3), Plate(2), Plate(1)]
  #[Plate(6), Plate(5), Plate(4)]
  #[Plate(9), Plate(8), Plate(7)]
print(st.pop())#Plate: 9
print(st.pop())#Plate: 8
print(st.pop())#Plate: 7
print(st.pop())#Plate: 6
print(st.pop())#Plate: 5
print(st.pop_at(0))#Plate: 3
for stt in st.stack:
  print(stt.stack)
  #[Plate(2), Plate(1)]
  #[Plate(4)]
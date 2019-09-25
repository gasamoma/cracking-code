# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
# Lets say im inserting 1 2 3 to the queue when i remove i have to do 1 2 3
# If I add 1 then all is normal then 2 in a stack would look like 1 2 and pop would go like 2 1
# but if i have two stacks and actively swap them i would have the desired result
# st1: 1 st2:null  add(2) then i add to empty stack st2.push(2), and them empty the stack into the other one
# st2.push(st1.pop) until st1 is empty then i have 2 1 so i  pop 1 2
#then add(3) so i have to empty into st1 again st1.push(st2.pop()) until st2 is empty
# then st1 is  1 2 then i push st1.push (3) and swap back to st2 3 2 1 so i pop 1 2 3
#i always have to do the same empty st1 to st2 then push new value to st2 then empty again to st1
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

class MyQueue:
    def __init__(self):
        self.st1=NClassicStack()
        self.st2=NClassicStack()
    def add(self,value):#this is O(2n)
        while not self.st1.is_empty():#this is O(n)
            self.st2.push(self.st1.pop())#this is O(1)
        self.st2.push(value) #this is O(1)
        while not self.st2.is_empty():#this is O(n)
            self.st1.push(self.st2.pop())#this is O(1)
    def remove(self):
        if self.st1.is_empty():
            return None
        return self.st1.pop()#this is O(1)
    def peek(self):
        return self.st1.peek()#this is O(1)
    def is_empty(self):
        return self.st1.is_empty()#this is O(1)

qu=MyQueue()
qu.add(1)
qu.add(2)
qu.add(3)
print(qu.remove())#1
print(qu.remove())#2
qu.add(4)
qu.add(5)
print(qu.remove())#3
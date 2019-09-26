#Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
#out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
#or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
#that type). They cannot select which specific animal they would like. Create the data structures to
#maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
#and dequeueCat. You may use the built-in Linked list data structure.
#May I represent dogs ang cats with strings like D1 D2 C1 C2? A: Yes
#Dogs and cats are Unique? so i wont have two D2 in the queue? A: No they are not unique
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

class NClassicQueue:
    head=None
    tail=None
    def __init__(self):
        pass
    def add(self,value):#this is O(1)
        if self.head is None:
            new_head=LList()
            new_head.value=value
            self.head=new_head
            self.tail=new_head
            return new_head
        to_add = LList()
        to_add.value=value
        self.tail.next=to_add
        self.tail=to_add
        return to_add
    def remove(self):
        if self.head is None:
            return None
        value = self.head.value
        if self.head == self.tail:
            self.tail=None
        self.head=self.head.next
        return value
    def peek(self):
        return self.head.value #this is O(1)
    def is_empty(self):
        return self.head is None #this is O(1)

class Shelter:
    def __init__(self):
        self.cats=NClassicQueue()
        self.dogs=NClassicQueue()
        self.shared=NClassicQueue()
    def enqueue(self,animal):#this is O(1)
        item = self.shared.add(animal)
        if animal[0]=='D':
            self.dogs.add(item)
        else:
            self.cats.add(item)
    def dequeueAny(self):#this is O(1)
        if self.shared.is_empty():
            return None
        value = self.shared.remove()
        if value[0]=='D':
            self.dogs.remove()
        else:
            self.cats.remove()
        return value
    def dequeue_this(self,item):#this is O(n)
        value = item.value
        if item == self.shared.head:
            self.shared.remove()#this is O(1)
            return value
        headcp = self.shared.head
        while headcp.next != item:#this is O(n)
            headcp = headcp.next
        headcp.next = item.next
        if item == self.shared.tail:
            self.shared.tail = headcp
        return value
    def dequeueDog(self):
        if self.dogs.is_empty():
            return None
        item=self.dogs.remove()
        return self.dequeue_this(item)#this is O(n)
    def dequeueCat(self):
        if self.cats.is_empty():
            return None
        item=self.cats.remove()
        return self.dequeue_this(item)#this is O(n)


sh= Shelter()
sh.enqueue("D1")
sh.enqueue("C1")
sh.enqueue("C2")
sh.enqueue("C3")
sh.enqueue("C4")
sh.enqueue("D2")
print(sh.dequeueDog())#D1
print(sh.dequeueDog())#D2
print(sh.dequeueDog())#None
print(sh.dequeueCat())#C1
print(sh.dequeueCat())#C2
print(sh.dequeueCat())#C3
print(sh.dequeueCat())#C4
print(sh.dequeueCat())#None
print(sh.dequeueAny())#None
sh.enqueue("D1")
sh.enqueue("C1")
sh.enqueue("C2")
sh.enqueue("C3")
sh.enqueue("C4")
sh.enqueue("D2")
print(sh.dequeueAny())#D1
print(sh.dequeueAny())#C1
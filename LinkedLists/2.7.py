#Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
#Return the intersecting node. Note that the intersection is defined based on reference, 
#not value. That is, if the kth node of the first linked list is the exact same node (by 
#reference) as the jth node of the second linked list, then they are intersecting
#in Python i can compare objects its the same? A: yes
#Since i got classes i can pass the var by "reference" cause it will be the object
#The only way its possible is if the second linked list is at the end of the first one
# i.e 1->2->3->4->5->6 &&  4->5->6 i cannot have and intersecting linked list in the middle 
#of the other one cause then it wont point to the same next object and so on
#asuming that i could just traverse it until i find the first node
class LinkedList:
  def __init__(self,value):
    self.next=None
    self.value=value
  def add(self,value):
    head = self
    while head.next != None:
      head = head.next
    head.next= LinkedList(value)
  def push(self,value):
    new_head=LinkedList(value)
    new_head.next=self
    return new_head
  def print(self):
    head = self
    while head.next != None:
      print(head.value, end = '')
      head = head.next
    print(head.value)

def intersection(l1,l2): #O(n)
  while l1:
    if l1 == l2: # worst caseO(n)
      return l1
    l1=l1.next
  return None

l = LinkedList(2)
l.add(3)
l.add(2)
l.add(1)
l.add(2)
l.add(5)
l.add(3)
l.add(7)
l.print() # 23212537
print(intersection(l,l.next.next.next).value) #1
l2 = LinkedList(2)
l2.add(3)
l2.add(2)
l2.add(1)
l2.add(2)
l2.add(5)
l2.add(3)
l2.add(7)
print(intersection(l,l2))#None

# Since i thought it was really easy i read some hints so i have to check if either l1 
#intersects l2 or l2 intersects l1

def intersection2(l1,l2): #O(n+m)
  l1cp=l1
  while l1:
    if l1 == l2: # worst case O(n)
      return l1
    l1=l1.next
  while l2:
    if l1cp ==l2: # worst case O(m)
      return l2
    l2=l2.next
  return None

print(intersection2(l.next.next.next,l).value)#1
print(intersection2(l2,l))#None
print(intersection(l.next.next.next,l)) #None
#Loop Detection: Given a circular linked list, implement an algorithm that returns the node 
#at the beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node's next pointer points to an 
#earlier node, so as to make a loop in the linked list.
#EXAMPLE
#Input: A -> B -> C -> D -> E -> C [the same C as earlier]
#Output: C
# I already discussed this problem before but never actually did it
# I thought i could store into another list but that would be highly inefficent 
# at the end having two indices its the solution with one going faster than the other 
# to know were they intersect is the tricky part I know that there is a magic formula but
#im doing it the way i would actually come up

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

def loop(l1): # worst case is O(n*n)
  head1=l1.next
  head2=l1.next.next
  while head1!=head2:#Worst case it wont be bigger than N so it's O(n)
    head1=head1.next
    head2=head2.next.next
  while l1!=head1:#this is O(n) if we half it O(n/2) then the following
    head2=head2.next
    while head2!=head1: #if the loop is n/2 big i means O(n)
      if head2==l1:
        return l1
      head2=head2.next
    l1=l1.next
  return head1

l = LinkedList(2)
l.add(3)
l.add(2)
l.add(1)
l.add(2)
l.add(5)
l.add(3)
l.add(7)
l.print() # 23212537
l.next.next.next.next.next.next.next.next=l.next.next.next.next.next # joining 7 and 5
print(loop(l).value)# 5

def magic_trick(l1): # worst case is O(n)
  head1=l1.next
  head2=l1.next.next
  while head1!=head2:#Worst case it wont be bigger than N so it's O(n)
    head1=head1.next
    head2=head2.next.next
  while l1!=head1:#this is O(n) cause magic
    l1=l1.next
    head1=head1.next
  return head1

print(magic_trick(l).value)# 5

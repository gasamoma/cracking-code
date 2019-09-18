#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
# is kth > than n? A:could be
#can i store the size of the LinkedList somewhere? A:No, cause it could be a very big list
class LinkedList:
  def __init__(self,value):
    self.next=None
    self.value=value
  def add(self,value):
    head = self
    while head.next != None:
      head = head.next
    head.next= LinkedList(value)
  def remove(self,value):
    head = self
    if head.value == value:
      self=head.next
      return
    while head.next != None:
      if head.next.value == value:
        head.next = head.next.next
      head = head.next
  def print(self):
    head = self
    while head.next != None:
      print(head.value, end = '')
      head = head.next
    print(head.value)
    

def kth_to_last(head,k): #O(n)
  second_head=head
  while second_head.next!=None and k > 1: # this is O(n)
    second_head=second_head.next
    k-=1
  if k > 1:
    return None
  while second_head.next != None: # this is O(n)
    second_head=second_head.next
    head=head.next
  return head

l = LinkedList(2)
l.add(3)
l.add(2)
l.add(1)
l.add(2)
l.add(5)
l.add(3)
l.add(7)
l.print() # 23212537
kth = kth_to_last(l,3)
print(kth.value) # 5
kth.print() # 537
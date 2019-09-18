#Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
#EXAMPLE
#Input:the node c from the linked lista->b->c->d->e->f
#Result: nothing is returned, but the new linked list looks like a->b->d->e->f
#Can i Write my own linked list class? A: sure
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

def deleteMiddleNode(node): # worst case O(n)
  while node.next.next!=None:# this is O(n)
    node.value = node.next.value
    node = node.next
  node.value = node.next.value
  node.next = None
  return

l = LinkedList(2)
l.add(3)
l.add(2)
l.add(1)
l.add(2)
l.add(5)
l.add(3)
l.add(7)
l.print() # 23212537
deleteMiddleNode(l.next.next)
l.print() # 2312537
#can't think a better way to do this, if i understood well the problem

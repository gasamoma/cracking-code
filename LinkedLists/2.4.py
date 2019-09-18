#Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 
# is there any logic in the order of the output like why in the example the 1 comes 
# before the 2 or it does not matter A: it does not matter 3 1 2 could be in any open
# if there are multiple values of x do they need to be together? A: No
#I would say i need to start swapping the elements but im not sure abot carring more than
#one x value forward ill start implementing and see how far i'd go
#does it matter if I moddify the list if X does not exist? A: yes, you sould not alter it
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

def partition(head, x):
  exist=False
  back = None
  front = None
  tail=None
  while True:
    if x == head.value:
      exist=True
    if head.value < x:
      if front is None:
        front=LinkedList(head.value)
        tail=front
      else:
        front=front.push(head.value)
    else:
      if back is None:
        back = LinkedList(head.value)
      else:
        back = back.push(head.value)
    if head.next is None:
      break
    head=head.next

  if exist:
    tail.next=back
    return front
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
partition(l,3).print() # 21227353
# I think i could do this without extra space  having 2 index
# No, I dont know how to do it better


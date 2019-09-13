#Remove Dups! Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?
# I’d assume is a slightly linked list
# do I leave the first ones or the last one A:First element should stay
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
   print("")
  
 
def remove_dups(llist):#this is O(n*n)
 while llist.next!=None:# this is O(n) worst case
   llist.next.remove(llist.value)# this is also O(n) worst case
   llist=llist.next
 return
 
l = LinkedList(2)
l.add(3)
l.add(2)
l.add(1)
l.add(2)
l.add(5)
l.add(3)
l.add(7)
l.print() # 2321253
remove_dups(l)
l.print() # 2315
# i think im solving the problem wihtout any temporary buffer


#Sum Lists: You have two numbers represented by a linked list, where each node contains a 
#single digit. The digits are stored in reverse order, such that the 1 's digit is at the 
# head of the list. Write a function that adds the two numbers and returns the sum as a 
# linked list.
#EXAMPLE
#Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
#Output: 2 -> 1 -> 9. That is, 912.
#FOLLOW UP
#Suppose the digits are stored in forward order. Repeat the above problem.
#EXAMPLE
#input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
#Output: 9 -> 1 -> 2. That is, 912.
# do i have to do the sum in place? A:that is the idea, not creating any other list besides 
# the one you are returning
# for the first one is very stright forward, since a sum happens fron the right digit to #the last one, for the other one i could just extract the numbers and modulus and #multiplicate them to get the result wanted
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


def sumlists(list1,list2): #O(n+m)
  result=LinkedList(0)
  carry_on=0
  while list1 or list2:# O(n+m)
    l_sum=0
    if list1:
      l_sum+=list1.value
      list1=list1.next
    if list2:
      l_sum+=list2.value
      list2=list2.next
    l_sum+=carry_on
    if l_sum>9:
      carry_on = 1
    else:
      carry_on = 0
    result.add(l_sum%10) #O(n|m)
  if carry_on==1:
    result.add(1)
  return result.next

l = LinkedList(7)
l.add(1)
l.add(6)

l2 = LinkedList(5)
l2.add(9)
l2.add(2)
l.print() # 716
l2.print() # 592
sumlists(l,l2).print() # 219

def inversed_sumlists(l1,l2):# worst case O(n+m)
  num1=0
  num2=0
  while l1 or l2: #this is O(n+m)
    if l1:
      num1=(num1*10)+l1.value
      l1=l1.next
    if l2:
      num2=(num2*10)+l2.value
      l2=l2.next
  lsum=num1+num2
  result=LinkedList(0)
  digits=1
  while lsum%(10**digits) != lsum:#this o(log10(n))
    digits+=1
  digits-=1
  while digits>=0:#this is O(log10(n))
    result.add(int(lsum/(10**digits)))
    lsum=lsum%10**digits
    digits-=1
  return result.next

l = LinkedList(6)
l.add(1)
l.add(7)

l2 = LinkedList(2)
l2.add(9)
l2.add(5)
l.print() # 617
l2.print() # 295
inversed_sumlists(l,l2).print() #912
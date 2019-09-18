#Palindrome: Implement a function to check if a linked list is a palindrome. 
# only letters from a-z? A:Yes
# no caps right? A:No there are no caps
# simple linked list? A:yes
#can i use hash a: NO
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

def palindrom(word): #O(n)
  copy=word
  rever=LinkedList(word.value)
  word=word.next
  while word: # O(n)
    rever=rever.push(word.value)#this isO(1)
    word = word.next
  while copy or rever: # this is O(n)
    if copy.value != rever.value:
      return False
    copy=copy.next
    rever=rever.next
  return True

word1=LinkedList("a")
word1.add("n")
word1.add("i")
word1.add("t")
word1.add("a")
word1.add("l")
word1.add("a")
word1.add("v")
word1.add("a")
word1.add("l")
word1.add("a")
word1.add("t")
word1.add("i")
word1.add("n")
word1.add("a")
word1.print() # anitalavalatina
print(palindrom(word1)) #true
word2=LinkedList("n")
word2.add("o")
word2.add("n")
word2.add("u")
word2.add("c")
word2.add("n")
word2.print() # nonucn
print(palindrom(word2)) # false
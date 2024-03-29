#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false
#Do i assume ascii? A Yes, all strings are in lowercase letters from a-z
#There are any restrictions arrays or else?A:you can use whatever you want
#I would say that the idea is to find differences between the 2 strs so i can just
# have a list of occurrences if there is only 1 difference of size 1 then is a 1 step if not then is more of them
def steps(str1,str2): #O(n)
 stores_1=[0]*25
 stores_2=[0]*25
 a_char=ord('a')
 for ith in str1: #this is O(n)
   stores_1[ord(ith)-a_char]+=1
 for ith in str2: #this is O(n)
   stores_2[ord(ith)-a_char]+=1
 differences=0
 for ith in range(25): #this is O(1)
   differences += abs(stores_1[ith]-stores_2[ith])
   if (len(str1) != len(str2) and differences >1) or (len(str1) == len(str2) and differences > 2):
     return False
 return True

print(steps("pale", "ple"))
print(steps("pales", "pale"))
print(steps("pale", "bale"))
print(steps("pale", "bake"))


#String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
#do special caracters as spaces are in the strign or do they matter A:only letters from a-z
#if the word is terbottlewa erbottlewat
# i dont know how to make it o(n) will use 2 indices and see how far i go
def rotation(str1,str2):# O(n)
 ith=0
 jth=0
 while jth < len(str2): #this is O(n)
   if str1[ith]==str2[jth]:
     ith+=1
   else:
     ith=0
   jth+=1
 return isSubstring(str2[:-ith], str1)
 
def isSubstring(str1,str2):
 return str1 in str2 #this is O(n)
 
print (rotation("terbottlewa","erbottlewat"))
print (rotation("waterbottle","erbottlewat"))
#lol i did it in O(n)  i was considering that the string checks could lead me
#to a different O(n*sub(n)) or something like it
# i think this solution might be faulty


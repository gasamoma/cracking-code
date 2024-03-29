#String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# should i compress Upercase and lower case sepparated i.e. A2a2 is a possible scenario A:Yes
# i could achive this by traversing the string and just count
def compress(str1): #O(n)
 if str1 == "":
   return str1
 current=str1[0]
 count=0
 compressed=list()
 for ith in range(len(str1)): #this is O(n)
   if current== str1[ith]:
     count+=1
   else:
     compressed.append(current)#appends are O(1)
     compressed.append(str(count))
     current=str1[ith]
     count=1
 compressed.append(current)
 compressed.append(str(count))
 if len(str1)<=len(compressed):
   return str1
 else:
   return ''.join(compressed) #this is O(n)

print(compress("aabcccccaaa"))
#i had to read the hints i could not figgure a way to do it better


#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
#Do I assume ascii? No
#Can I use other data strucutures? Yes
#Not So efficent solution would be
#to sort both strings and to check if they are the same

def check_perm(str1,str2): # O(n*logn+n*logn+n) = O(n*(2logn+1))=O(nlogn)
 if len(str1)!= len(str2):
   return False
 str1=sorted(str1)
 str2=sorted(str2)
 if str1 != str2:
   return False
 return True

print(check_perm("houdie", "eiduoh"))

# another solution would be to hash the string1 and then with traverse string2
# and if the string2 hast is not equal to hash string1 its not a Permutation
def check_perm2(str1,str2):# O(n+n)=O(n)
 if len(str1) != len(str2):
   return False
 hash_1 = dict()

 for ith in str1:
   if hash_1.get(ith,None) is None:
     hash_1[ith]=1
   else:
     hash_1[ith]+=1

 for ith in str2:
   if hash_1.get(ith, None) is None:
     return False
   if hash_1[ith] == 1:
     hash_1.pop(ith)
   else:
     hash_1[ith]-=1
 if hash_1 == {}:# this check isnt needed..., well only if the str1 and str2 are ""
   return True

print(check_perm2("houdie", "eidouh"))
#So i decided to optimized while coding to avoid using another n space with the extra hash
# instead i started substracting until no items are left
# Another question that i could have asked is if the str could be different in size
# and if the strs are always different those could saved me some lines


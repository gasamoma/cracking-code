def uniques(string): #with data structures O(n)
 stores=dict()
 for ith in string:
   if stores.get(ith,0) !=0:
     return False
   stores[ith] = 1
 return True

print(uniques("HELLO"))

def uniques_pro(string): #without data structures O(n*logn +n)= o(n*logn)
 string = sorted(string)
 for ith in range(len(string)-1):
   if string[ith+1]==string[ith]:
     return False
 return True

print(uniques_pro("HELLO"))

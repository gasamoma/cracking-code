#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
# literally 4 bytes? yes
#i'm going to start without doing it in place
#rotating means 0,0 goes to 0,n 1,0 goes to 0, n-1
# this seems to mean that for the first row dest is ith,0 to 0, n-ith
def rotate_90(image):#O(n*n)
  n=len(image)
  resulting = list()
  
  jth=0
  while jth < n:#this is O(n)
    ith=n
    to_append = list()
    while ith > 0:#this is O(n)
      to_append.append(image[ith-1][jth])# this is O(byte)=O(k)
      ith-=1
    resulting.append(to_append)# this is O(n)
    jth+=1
  return resulting

arr = [[5, 10, 15, 20, 25,"["],
       [4, 9, 14, 19, 24,"p"],
       [3, 8, 13, 18, 23,"o"],
       [2, 7, 12, 17, 22,"i"],
       [1, 6, 11, 16, 21,"u"],
       ["q","w","e","r","t","y"]]
#print(arr)
#print(rotate_90(arr))
#to do it on place i would have to make the 4 swaps for each item theorically i need to #traverse it differently like a pyramid no , afer drawing it it better move a corner of the
# matrix len is even is easy (n/2) if is odd n(ceil(n/2)) 
# i .e. 
#  1  2  3  4  5 x
#  6  7  8  9 10 y
# 11 12 13 14 15 u 
# 16 17 18 19 20 i
# 21 22 23 24 25 o 
#  z  c  v  b  n m 
import math
def rotate_90_pro(image): #this is O(n*n)
  n=len(image)
  top=math.floor(n/2)
  ith = 0
  while ith < top:
    jth = 0
    while jth<=top:
      temp=image[ith][jth]
      image[ith][jth]=image[n-1-jth][ith]
      image[n-1-jth][ith]=image[n-1-ith][n-1-jth]
      image[n-1-ith][n-1-jth]=image[jth][n-1-ith]
      image[jth][n-1-ith]=temp
      print(ith, jth)
      jth+=1
    print(image)
    ith+=1
  return image
print(rotate_90_pro(arr))
#When i tested i got a bug i cant figgure it out is about boundaries and not repeating already rotated items i think im missing some rule if even or odd
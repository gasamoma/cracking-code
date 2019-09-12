#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
# should i work in the same matrix A: no but if you can its a plus
# all are going to be integers or should i consider 0.x as 0 A:All ints only 0 is the one
# i will just capture the 0 axis and the clear the axis, this si to avoid extra work
def zero_matrix(matrix):# O(n*m)+O(n)+O(n-m)= O(n*m)
 x_axis=dict()
 y_axis=dict()
 for ith in range(len(matrix)): #this is O(n*m)
   for jth in range(len(matrix[ith])):
     if matrix[ith][jth] == 0:
       x_axis[ith]=1
       y_axis[jth]=1
  for ax in x_axis.keys():# worst case this is o(n)
   matrix[ax]=[0]*len(matrix[ax])
 for ay in y_axis.keys():
   for ith in range(len(matrix)):#worst case this is O(n*m)
     matrix[ith][ay]=0
 return matrix
 
print(zero_matrix([[1,0,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
 
##Interesting tip 102 idk how to
 


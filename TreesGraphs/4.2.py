#Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.
# an example would be like [ 1 5 6 8 11 55 66 102 111]
# I grab the middle and insert it i.e 11 then i grab the middle node if the left half and insert it
# and the same to the right half so left: 6 and right 102 and so on until i done all of them
import math
class balancedTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def add(self,value):
        if value < self.value:
            if self.left is None:
                self.left=balancedTree(value)
            else:
                self.left.add(value)
        elif value > self.value:
            if self.right is None:
                self.left=balancedTree(value)
            else:
                self.right.add(value)
    def print_dfs(self):
        if self.left is None and self.right is None:
            print(self.value)
            return
        if self.left is not None:
            self.left.print_dfs()
        if self.right is not None:
            self.right.print_dfs()
        print(self.value)



def from_array_to_tree(arr):#O(n)
    size=len(arr)
    if size%2==0:
        ith=int(size/2)
        curr=balancedTree(arr[ith])
        curr.left=insert_to_tree(arr,0,ith-1)
        curr.right=insert_to_tree(arr,ith+1,size-1)
        return curr
    else:
        ith=int(math.floor(size/2))
        curr=balancedTree(arr[ith])
        curr.left=insert_to_tree(arr,0,ith-1)
        curr.right=insert_to_tree(arr,ith+1,size-1)
        return curr

def insert_to_tree(arr,i,j):
    if i>j:
        return None
    if i == j:
        return balancedTree(arr[i])
    size=j-i+1
    if size % 2 == 0:
        ith = int(size / 2)+i
        curr = balancedTree(arr[ith])
        curr.left = insert_to_tree(arr, i, ith - 1)
        curr.right = insert_to_tree(arr, ith + 1, j)
        return curr
    else:
        ith = int(math.floor(size / 2)) + i
        curr = balancedTree(arr[ith])
        curr.left = insert_to_tree(arr, i, ith - 1)
        curr.right = insert_to_tree(arr, ith + 1, j)
        return curr

a=from_array_to_tree([1,5,6,8,11,55,66,102,111,112])
a.print_dfs()#1 5 8 11 6 66 102 112 111 55
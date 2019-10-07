#Check Balanced: Implement a function to check if a binary tree is balanced.
#For the purposes of this question, a balanced tree is defined to be a tree
#such that the heights of the two subtrees of any node never differ by more than one.
class BinTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def add(self,value): #O(log(n)) worst case O(n)
        if value < self.value:
            if self.left is None:
                self.left=BinTree(value)
            else:
                self.left.add(value)
        elif value > self.value:
            if self.right is None:
                self.right=BinTree(value)
            else:
                self.right.add(value)

def inbalance(tree):#O(n)
    if tree is None:
        return 0
    right=inbalance(tree.right)
    left=inbalance(tree.left)
    if right is None or left is None or not(-2<left-right<2):
        return None
    return max(left,right)+1

def check_balance(tree):
    if inbalance(tree) is None:
        return False
    return True

tree=BinTree(5)
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(4)
tree.add(9)
tree.add(7)
tree.add(6)
tree.add(8)
tree.add(12)
tree.add(10)
tree.add(13)
tree.add(14)
print(check_balance(tree))#True
tree.add(15)
print(check_balance(tree))#False

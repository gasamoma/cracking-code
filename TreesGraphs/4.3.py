#List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
#at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
#is the tree complete? A: Not necessarily
#is the tree balanced? A:Not necessarily
#How do I return the linked lists? A: just do it with a returning array of linked lists
class LList:
    def __init__(self):
        self.value=None
        self.next=None
    def add(self,value):
        if self.next is None:
            self.next=LList()
            self.next.value=value
        else:
            self.next.add(value)
    def pprint(self):
        if self.next is None:
            print(self.value)
            return
        else:
            print(self.value,end=' ')
            self.next.pprint()
class BinTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def add(self,value):
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
def dept(tree,llists,dp):
    if tree is None:
        return
    lli_len=len(llists)
    if lli_len>dp:
        llists[dp].add(tree.value)
    else:
        new_lli=LList()
        new_lli.value=tree.value
        llists.append(new_lli)
    dept(tree.left,llists,dp+1)
    dept(tree.right,llists,dp+1)

def list_of_depths(tree):
    llists=[]
    dept(tree,llists,0)
    return llists

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
llists=list_of_depths(tree)
for l in llists:
    l.pprint()
# 5
#2 9
#1 3 7 12
#4 6 8 10 13
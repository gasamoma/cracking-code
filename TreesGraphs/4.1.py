#Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
#route between two nodes
# How do I receive the Graph, A: matrix
# how do I receive the 2 nodes A: as x,y coordinates from 0 to N
# does the matrix is squared? A: Not necessarily
# how do I interpret if a node is connected or not? A: True or false
# can I use a queue? A:No
# DFS implementation with arrays
def find_connection(graph,n1x,n1y,n2x,n2y):# worst case scenario this is O(n*m)
    if n1x<0 or n1x>= len(graph) or n1y<0 or n1y>= len(graph[0]) or graph[n1x][n1y]==False or graph[n1x][n1y]==2:
        return False
    else:
        graph[n1x][n1y]=2
    if n1x==n2x and n1y == n2y:
        return True
    if find_connection(graph,n1x+1,n1y,n2x,n2y):
        return True
    if find_connection(graph,n1x,n1y+1,n2x,n2y):
        return True
    if find_connection(graph,n1x-1,n1y,n2x,n2y):
        return True
    if find_connection(graph,n1x,n1y-1,n2x,n2y):
        return True
    return False

graph=[
    [True,True,True,True],
    [True,True,True,True],
    [True,True,True,True],
    [True,True,True,True],
    [True,True,True,True]]
print(find_connection(graph,0,0,3,3)) #True
graph2=[
    [True,True,True,True],
    [True,True,True,False],
    [False,True,False,True],
    [True,True,True,False],
    [True,True,True,True]]
print(find_connection(graph2,0,0,2,3)) #False
graph2=[
    [True,True,True,True],
    [True,True,True,True],
    [False,True,False,False],
    [True,True,True,True],
    [True,True,True,True]]
print(find_connection(graph2,0,0,3,3)) #True
#this could be improved with a BFS
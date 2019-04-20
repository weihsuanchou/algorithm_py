from collections import deque
from collections import defaultdict

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
    
  def addEdge(self, node, neighbor):
    self.graph[node].append(neighbor)
    
  def BFS_MY_CODE(self, start):

    myQueue = deque()
    myQueue.append(start)
    mySet = set()
    result = []   

    while myQueue: 
        cur = myQueue.popleft()
        mySet.add(cur)
        result.append(cur)
        print('cur : ',cur)
        list = self.graph[cur] 
        print('list : ',list)
        for i in range(0, len(list)):
            print('ele ', list[i])
            if (list[i] in mySet):
                print('ele exist')
            else: 
                myQueue.append(list[i])
                print('adding ele ', list[i])

    print('result: ',result)


  def BFS(self, start):

    myQueue = deque() 
    visited = [False] * len(self.graph)
    myQueue.append(start) 
    
    while myQueue: 
        cur = myQueue.popleft()
        visited[cur] = True 
        print(cur, end= ' ')

        list = self.graph[cur]  
        for i in range(0, len(list)): 
            if (visited[list[i]] == False):  
                myQueue.append(list[i]) 
 


def main():
    print( "hello Doctor!") 
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.BFS(2)

if __name__ == "__main__":
    main()
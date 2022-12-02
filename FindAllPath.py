from collections import deque
class myQueue:
    def __init__(self):
        self.Q = deque()
    def deQueue(self):
        return self.Q.popleft()
    def enQueue(self, x):
        return self.Q.append(x)
    def isEmpty(self):
        return False if self.Q else True

def findAllPaths(vertices, gList, source , destination):
    allPaths=[]
    path=[]
    visited = {v:False for v in vertices}
    findAllPathsRecursive(vertices, gList, source, destination, visited, path, allPaths)
    return allPaths

def findAllPathsRecursive(vertices, gList, src, dest, visited, path, allPaths):
    visited[src] = True
    path.append(src)
    if (src == dest):
        allPaths.append(path.copy())
    for e in gList[src]:
        if not visited[e]:
            findAllPathsRecursive(vertices, gList, e, dest, visited, path, allPaths)
    path.pop()
    visited[src]=False

def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))
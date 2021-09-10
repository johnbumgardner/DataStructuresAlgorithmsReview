from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, start, end):
        if start not in self.graph or end not in self.graph:
            print("bad")
            return None
        visited = [False]* (max(self.graph) + 1)
        routes = {}
        queue = [start]
        visited[start] = True
        routes[start] = [start]
        if start == end:
            return routes[start]
        while queue:
            node = queue.pop(0)
            print(str(node) +  " ")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    routes[neighbor] = [neighbor] + routes[node] 
                    visited[neighbor] = True
                    if neighbor == end:
                        return routes[neighbor]
        return None



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 5)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
print(g.BFS(2,6))
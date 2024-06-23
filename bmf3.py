import time
class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []

    def add_edges(self,u,v,w):
        self.graph.append((u,v,w))

    def bellman_ford(self,src):
        global c
        c=0
        dist = [float("inf")] * self.v
        dist[src] = 0
        iteration = 0
        index = 0
        for _ in range(self.v-1):
            iteration +=1
            for s,d,w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    index +=1
                    dist[d] = dist[s] + w
                    c+=1
                    print("Iteration: ",index)
                    print(dist)

        for s,d,w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
        return dist



g = Graph(10)

g.add_edges(0, 1, 4)
g.add_edges(0, 8, 9)
g.add_edges(1, 2, 2)
g.add_edges(1, 8, 3)
g.add_edges(1, 9, 3)
g.add_edges(2, 3, 4)
g.add_edges(3, 4, 2)
g.add_edges(3, 6, 11)
g.add_edges(4, 5, 5)

g.add_edges(4, 6, 2)
g.add_edges(5, 6, 1)
g.add_edges(6, 7, 1)
g.add_edges(7, 8, 2)
g.add_edges(8, 1, 5)
g.add_edges(8, 9, 5)
g.add_edges(9, 1, 4)
g.add_edges(9, 8, 5)  
# g.add_edges(0,1,1)
# g.add_edges(0,2,1)
# g.add_edges(1,3,2)
# g.add_edges(2,4,2)
# g.add_edges(3,5,-2)
# g.add_edges(4,6,1)
# g.add_edges(5,7,3)
# g.add_edges(6,8,4)
# g.add_edges(0,9,8)


src = 0
st=time.time()
result = g.bellman_ford(src)
et =time.time()
print()
print("Iterations: ",c)
print()
for i in range(len(result)):
    print(f"Vertex({i}) distance from source is {result[i]}")
print()
print("Time Taken: ",et-st,"seconds")
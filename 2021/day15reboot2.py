#from copy import deepcopy
# import sys
# import time
from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []        
    def add_edge(self, u, v, weight):
            self.edges[u][v] = weight
            self.edges[v][u] = weight





bignegative = -1

f = open("day15.testin")
contents = (f.readlines())

inputmap = []
widelist = []
for i in range(len(contents[0]) + 1):
    widelist.append(bignegative)
inputmap.append(widelist)
for l in contents:
    inlist = []
    tmpstr = l.strip()
    inlist.append(bignegative)
    for c in tmpstr:
        inlist.append(int(c))
    inlist.append(bignegative)
    inputmap.append(inlist)

inputmap.append(widelist)
width = len(inputmap[0]) - 1
height= len(inputmap) - 1

print(inputmap)

def allaround(row,col):
    outlist = []
    outlist.append([row -1, col])    
    outlist.append([row, col -1])
    outlist.append([row, col +1])
    outlist.append([row +1, col])    
    return outlist

rules = {}
costs = {}

for row in range(1,height):
    for col in range(1,width):
        costs[str(row) + ',' + str(col)] = inputmap[row][col]
        edgelist = []
        for c in allaround(row,col):
            if inputmap[c[0]][c[1]] > 0:
                edgelist.append(str(c[0]) + ',' +str(c[1]))
        rules[str(row) + ',' + str(col)] = edgelist
            


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

edges = []
for k in rules.keys():
    for i in rules[k]:
        edges.append((k,i,costs[i]))

g = Graph(len(costs))

for edge in edges:
    g.add_edge(*edge)

print(edges)

d = (dijsktra(g,'1,1'))
print(d)
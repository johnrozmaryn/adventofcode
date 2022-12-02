#from copy import deepcopy
import sys
# import time
from collections import defaultdict
from collections import deque
from queue import PriorityQueue
import heapq

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return



def dijkstra(aGraph, start, target):
    print('Dijkstras shortest path')
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
 





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
            



g = Graph()

edges = []
start = 1
for k in rules.keys():
    for i in rules[k]:
        edges.append((start,i,costs[i]))

for k in costs.keys():
    g.add_vertex(k)
    
for e in edges:
    g.add_edge(*e)

print ('Graph data:')
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

dijkstra(g, g.get_vertex('1,1'), g.get_vertex('10,10')) 

target = g.get_vertex('e')
path = [target.get_id()]
shortest(target, path)
print('The shortest path : %s' %(path[::-1]))

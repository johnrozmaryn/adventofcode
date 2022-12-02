#from copy import deepcopy
# import sys
# import time


f = open("day12.in")
contents = (f.readlines())

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
            
def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

print(dijsktra(rules,'1,1','10,10'))
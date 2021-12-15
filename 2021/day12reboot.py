#from copy import deepcopy
# import sys
# import time


f = open("day12.in")
contents = (f.readlines())

rules = {}
for l in contents:
    splitlist = l.strip('\n').split('-')
    if splitlist[0] in rules.keys():
        rules[splitlist[0]].append(splitlist[1])
    else:
        rules[splitlist[0]] = []
        rules[splitlist[0]].append(splitlist[1])
    if splitlist[1] in rules.keys():
        rules[splitlist[1]].append(splitlist[0])
    else:
        rules[splitlist[1]] = []
        rules[splitlist[1]].append(splitlist[0])
        
def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if (node not in path) or (node.upper() == node):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

pathlist = find_all_paths(rules,'start','end')
print(len(pathlist))
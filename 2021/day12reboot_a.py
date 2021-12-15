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
        
def oktoaddnode(path,node):
    if path.count('start') == 1 and node == 'start':
        return False
    if path.count('end') == 1 and node == 'end':
        return False
    if node not in path:
        return True
    elif node.upper() == node:
        return True
    elif node.lower() == node:
        if path.count(node) < 2:
            tmplower = lowerlist.copy()
            tmplower.remove(node)
            for i in tmplower:
                if path.count(i) == 2:
                    return False
            return True
    else:
        return False
        
lowerlist = []
for i in rules.keys():
    if i.lower() == i:
        lowerlist.append(i)
lowerlist.remove('start')
lowerlist.remove('end')
print(lowerlist)              
        
        
def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if oktoaddnode(path,node):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

pathlist = find_all_paths(rules,'start','end')
trimmedlist = []
for i in pathlist:
    if i not in trimmedlist:
        trimmedlist.append(i)
        
print(len(trimmedlist))
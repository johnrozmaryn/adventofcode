f = open("day12.in")
contents = f.readlines()


#I want to use graph_tool. https://graph-tool.skewed.de/static/doc/quickstart.html#creating-and-manipulating-graphs
#....but, I'll end up using NetworkX: https://networkx.org/

#import networkx as nx

from dijkstar import Graph,find_path

width = len(contents[0].strip())
height = len(contents)

posd = {}   #Dictionary of all my positions, in the form r_c, where 0_0 is top left

start = ''
end = ''
conv = 'abcdefghijklmnopqrstuvwxyz'
aroundvec = [[0,1],[-1,0],[1,0],[0,-1]]
graph = Graph()

def aroundlist(addr):
    addl = addr.split('_')
    r = int(addl[0])
    c = int(addl[1])
    adjlist = []
    for vec in aroundvec:
        adjlist.append([r+vec[0],c+vec[1]])
    t = []
    for pos in adjlist:
        if (str(pos[0]) + '_' + str(pos[1])) in posd:
            t.append(str(pos[0]) + '_' + str(pos[1]))
    return t

##make my big dictionary
for r in range(height):
    l = contents[r].strip()
    for c in range(len(l)):
        addr = str(r) + '_' + str(c)
        if l[c] == 'S':
            start = addr
            posd[addr] = conv.find('a')          
        elif l[c] == 'E':
            end = addr
            posd[addr] = conv.find('z')
        else:
            posd[addr] = conv.find(l[c])

##add edges where the height difference is 0 or 1
for r in range(height):
    l = contents[r].strip()
    for c in range(len(l)):
        addr = str(r) + '_' + str(c)
        for cell in aroundlist(addr):
            if (posd[cell] - posd[addr]) <=1 :
                graph.add_edge(addr,cell,1)
 
print(find_path(graph,start,end))

# def fp(addr,r,c):
#     if nx.has_path(graph,addr,str(r) + '_' + str(c)):
#         print(nx.shortest_path(graph,addr,str(r) + '_' + str(c)))
#     else:
#         print(False)
        
    
                
        

      
            
        
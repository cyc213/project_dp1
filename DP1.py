#Input: graph
#output: Vectors p*(G) and x*(G)
#graph convert to tree / 

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.get(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.get(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_top(graph):
    return next(iter(graph))

def find_descend_of_top(graph, top, end):
    descend = [0, 0, 0, 0, 0, 0]
    for i in find_all_paths(graph, top, end):
        for j in i:
            temp = (int)(j[1]) - 1
            descend[temp] = 1
    return descend

def find_x(graph):
    x = [0, 0, 0, 0, 0, 0]
    for i in graph:
        temp = (int)(i[1]) - 1
        x[temp] = 1
    return x

def find_G_right(descend, x):
    j = 0
    for i in descend:
        if(i == 1):
            x[j] = 0
        j+=1
    return x

def find_G_left(top, x):
    temp = (int)(top[1]) - 1
    x[temp] = 0
    return x

def create_newGraph(graph, x):
    new_graph = {}
    for i in graph:
        temp = (int)(i[1]) - 1
        if(x[temp] != 0):
            new_graph[i] = graph[i]
    return new_graph


def DP1(graph, output = []):
    if(graph == {}):
        return graph
    else:
        top = find_top(graph)
        x = find_x(graph)
        descend = find_descend_of_top(graph, top, 'v6')
        G_left = create_newGraph(graph, find_G_left(find_top(graph), x))
        G_right = create_newGraph(graph, find_G_right(descend, x))
        DP1(G_left)
        DP1(G_right)
        output.append(find_x(graph))
    return output

graph = {'v1': ['v2', 'v4', 'v5'],
         'v2': ['v3'],
         'v3': ['v6'],
         'v4': ['v5', 'v6'],
         'v5': ['v6'],
         'v6': ['']}

vertex_w_p = {'v1': [4, 1],
              'v2': [1, 2],
              'v3': [3, 1],
              'v4': [3, 2],
              'v5': [2, 3],
              'v6': [2, 2]}

weight = 8

output = DP1(graph)
print(output)
# output_tree = {}
# j = 0
# for i in DP1(graph):
#     temp = 'G' + str(j)
#     output_tree[temp] = i
#     j += 1

# print(output_tree)

# for i in output_tree:
#     print(output_tree[i])

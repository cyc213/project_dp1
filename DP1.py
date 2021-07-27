#Input: graph
#output: Vectors p*(G) and x*(G)

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

def find_G_right(graph, top, end, x):
    for i in find_all_paths(graph, top, end):
        for j in i:
            if(j != top):
                temp = (int)(j[1]) - 1
                x[temp] = 1
    return x

graph = {'v1': ['v2', 'v4', 'v5'],
         'v2': ['v3'],
         'v3': ['v6'],
         'v4': ['v5', 'v6'],
         'v5': ['v6'],
         'v6': ['']}

x = [0, 0, 0, 0, 0, 0]

print(find_G_right(graph, 'v1', 'v6', x))
# for i in find_all_paths(graph, 'v1', 'v6'):
#     for j in i:
#         if(j != 'v1'):
#             temp = (int)(j[1]) - 1
#             x[temp] = 1

# print(x)




    
# for i in graph:
#     for j in graph[i]:
#         print(j)

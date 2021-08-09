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

def find_p(graph_dic, p_output = {}, x_output = {}):
    for i in graph_dic:
        sub_p_output = []
        sub_x_output = []
        if(len(graph_dic[i]) == 1):
            for j in range(0, 9):
                sub_p_output.append(p_singleton(graph_dic[i], j))
                sub_x_output.append(x_singleton(graph_dic[i], j))
        else:
            top = find_top(graph_dic[i])
            x = find_x(graph_dic[i])
            descend = find_descend_of_top(graph_dic[i], top, 'v6')
            p_left = create_newGraph(graph_dic[i], find_G_left(top, x))
            p_right = create_newGraph(graph_dic[i], find_G_right(descend, x))
            for j in range(0, 9):
                if((j - vertex_w_p[top][0]) < 0):
                    sub_p_output.append(0)
                    sub_x_output.append(0)
                else:
                    if(p_left == {}):
                        left_value = 0
                    else:
                        for k in graph_dic:
                            if(p_left == graph_dic[k]):
                                left_value = vertex_w_p[top][1] + p_output[k][(j - vertex_w_p[top][0])]
                                break
                    
                    if(p_right == {}):
                        right_value = 0
                    else:
                        for k in graph_dic:
                            if(p_right == graph_dic[k]):
                                right_value = p_output[k][j]
                                break

                    sub_p_output.append(max(left_value, right_value))
                    if(left_value >= right_value):
                        sub_x_output.append(1)
                    else:
                        sub_x_output.append(0)
        p_output[i] = sub_p_output
        x_output[i] = sub_x_output
    return p_output, x_output

def p_singleton(graph, w):
    if(w >= vertex_w_p[find_top(graph)][0]):
        return vertex_w_p[find_top(graph)][1]
    return 0

def x_singleton(graph, w):
    if(w >= vertex_w_p[find_top(graph)][0]):
        return 1
    return 0


def tree_of_graph(graph, vertex_num, result = {}):
    if(graph == {}):
        vertex_num -= 1
        return vertex_num, result
    else:
        top = find_top(graph)
        x = find_x(graph)
        descend = find_descend_of_top(graph, top, 'v6')
        G_left = create_newGraph(graph, find_G_left(find_top(graph), x))
        G_right = create_newGraph(graph, find_G_right(descend, x))
        origin = vertex_num
        temp = vertex_num + 1
        vertex_num, result = tree_of_graph(G_left, temp)
        if(G_right != {} and G_left != {}):
            vertex_num, result = tree_of_graph(G_right, vertex_num + 1)
            result_num = origin
        else:
            result_num, result = tree_of_graph(G_right, temp)

        result[result_num] = graph
        return vertex_num, result


graph = {'v1': ['v2', 'v4', 'v5'],
         'v2': ['v3'],
         'v3': ['v6'],
         'v4': ['v5', 'v6'],
         'v5': ['v6'],
         'v6': ['']}

vertex = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']
vertex_w_p = {'v1': [4, 1],
              'v2': [1, 2],
              'v3': [3, 1],
              'v4': [3, 2],
              'v5': [2, 3],
              'v6': [2, 2]}

weight = 8

output, output_dic = tree_of_graph(graph, 0)
p_output, x_output = find_p(output_dic)

for i in p_output:
    print(i, p_output[i])

for i in x_output:
    print(i, x_output[i])
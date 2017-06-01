graph = {'A': (['B', 'C']),
         'B': (['A', 'D', 'E']),
         'C': (['A', 'F']),
         'D': (['B']),
         'E': (['B', 'F']),
         'F': (['C', 'E'])}

def dfs(graph,vertex):
    stack = [vertex]
    visited = [vertex]
    while stack:
        try:
            vertex = min(list(set(graph[vertex]) - set(visited)))
            stack.append(vertex)
            visited.append(vertex)
        except:
            stack.pop()
            if (len(stack) > 0):
                vertex = stack[-1]
    if len(visited)>1:
        return visited
    else:return "error"

def addVertex(c):
    print (c)
    return 0


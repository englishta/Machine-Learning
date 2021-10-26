def make_tree():
    node = []
    with open('out.txt', mode='r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            node.append(line)

    n = len(node)
    depth = [-1]*n # depth[i]:=i?????????

    for i in range(n):
        depth[i] = (len(node[i])-len(node[i].lstrip(' ')))//2
    
    for i in range(n):
        node[i] = node[i].lstrip(' ')

    r = [-1]*n
    r[0] = 0
    graph = [[] for _ in range(n)]

    for i in range(1, n):
        r[depth[i]] = i
        graph[r[depth[i]-1]].append(i)
        graph[i].append(r[depth[i]-1])
    
    return node, graph

def dfs_struct_search(now, graph, node, struct_list):
    if now >=20: return
    if 'Struct:' in node[now]:
        struct_list.append(node[now].replace('Struct:', '').replace(' ', ''))
    for next in graph[now]:
        if next < now: continue
        dfs_struct_search(next, graph, node, struct_list)

def dfs_array_search1(now, graph, node, array_root):
    if 'ArrayDecl:' in node[now]:
        array_root.append(now)
    for next in graph[now]:
        if next < now: continue
        dfs_array_search1(next, graph, node, array_root)

def dfs_array_search2(now, graph, node, name, type, size):
    if 'ID:' in node[now]:
        size = node[now].replace('ID:', '').replace(' ', '')
    for next in graph[now]:
        if next < now: continue
        name, type, size = dfs_array_search2(next, graph, node, name, type, size)
    return name, type, size

# ?????????????        
class Array():
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size

def main(): 
    node, graph = make_tree()
    array_root = [] # ???????????
    array_list = [] # Array???????????
    struct_list = []
    dfs_struct_search(0, graph, node, struct_list)
    dfs_array_search1(20, graph, node, array_root)
    for id in array_root:
        name, type, size = dfs_array_search2(id, graph, node, "", "", "")
        comp = Array(name, type, size)
        array_list.append(comp)
    
    print(array_root)
    print(struct_list)
    for e in array_list:
        print(e.size)
        print(e.type)
        print(e.name)
    

if __name__ == "__main__":
    main()
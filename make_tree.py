def make_tree():
    node = []
    with open('out.txt', mode='r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            node.append(line)

    n = len(node)
    depth = [-1]*n # depth[i]:=i行目のノードの深さ

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
    # if 'Decl: main' in node[now]: return # main関数を読み込まない
    if now>29: return

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
    if 'IdentifierType:' in node[now]:
        type = node[now].replace('IdentifierType:', '').replace(' ', '').replace('[', '').replace(']', '').replace("'", '')
    if 'Struct:' in node[now]:
        type = node[now].replace('Struct:', '').replace(' ', '')
    if 'TypeDecl:' in node[now]:
        name = node[now].replace('TypeDecl:', '').replace(' ', '').replace('[', '').replace(']', '').replace(',', '')

    for next in graph[now]:
        if next < now: continue # 親は訪問しない
        name, type, size = dfs_array_search2(next, graph, node, name, type, size)
    return name, type, size

def review(struct_list, array_list):
    for st in struct_list:
        used = False
        for comp in array_list:
            if comp.type == st:
                used = True
                print("Struct", st, "is Used in Array :", comp.name)
        if not used:
            print("Struct", st, "is Not Used")


# 配列の情報を記録するクラス
class Array():
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size

if __name__ == "__main__":
    node, graph = make_tree()
    array_root = [] # 配列宣言部分木の根番号
    array_list = [] # Arrayクラスを要素に持つ配列
    struct_list = []
    dfs_struct_search(0, graph, node, struct_list)
    dfs_array_search1(0, graph, node, array_root)
    for id in array_root:
        name, type, size = dfs_array_search2(id, graph, node, "", "", "")
        comp = Array(name, type, size)
        array_list.append(comp)
    
    for comp in array_list:
        print(comp.name)
        print(comp.size)
        print(comp.type)
    
    print(struct_list)

    review(struct_list, array_list)

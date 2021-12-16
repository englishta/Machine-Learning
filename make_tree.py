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


def dfs_struct_search1(now, graph, node, struct_root):
    if 'Decl: main' in node[now]: return # main関数を読み込まない
    if now>29: return
    if 'Struct:' in node[now]:
        struct_root.append(now)
    for next in graph[now]:
        if next < now: continue
        dfs_struct_search1(next, graph, node, struct_root)

def dfs_struct_search2(parent, now, graph, node, struct_count, var_type="None"):
    # if 'Decl: main' in node[now]: return # main関数を読み込まない
    if now>29: return
    if 'ArrayDecl:' in node[now]: var_type = 'Array'
    if 'Struct:' in node[now]:
        Struct_Name = node[now].replace('Struct:', '').replace(' ', '')
        struct_detail[struct_count].append(("Struct_Name", Struct_Name))
    if 'IdentifierType:' in node[now]:
        type = node[now].replace('IdentifierType:', '').replace(' ', '').replace('[', '').replace(']', '').replace("'", '')
        if var_type == "Array": type+='_array'
        name = node[parent].replace('TypeDecl:', '').replace(' ', '').replace('[', '').replace(']', '').replace(',', '')
        struct_detail[struct_count].append((type, name))

    for next in graph[now]:
        if next<now: continue # 親は訪問しない
        dfs_struct_search2(now, next, graph, node, struct_count, var_type)


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
                print(f'Struct {st} is used in Array {comp.name}')
        if not used:
            print(f'Struct {st} is not used')

# 宣言されている構造体が仕様書どうりであるかを調査する関数
def struct_review():
    memo = []
    n = int(input())
    for i in range(n):
        k = int(input())
        v = []
        name = str(input())
        v.append(("Struct_Name", name))
        for _ in range(k):
            type, var_name = map(str, input().split())
            v.append((type, var_name))
        name_find = False
        for id in range(len(struct_detail)):
            if struct_detail[id] == []: break
            if name == struct_detail[id][0][1]:
                name_find = True
                for Ty, Na in v:
                    find = False
                    for Ty_, Na_ in struct_detail[id]:
                        if Ty == Ty_ and Na == Na_:
                            find = True
                            break
                    if not find:
                        memo.append(f'Struct {name} : ({Ty}, {Na}) not found')
        if not name_find:
            memo.append(f'Struct [{name}] not found')
    for s in memo:
        print(s)


# 配列の情報を記録するクラス
class Array():
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size

# 構造体を記録する二次元配列
struct_detail = [[] for _ in range(100)]

if __name__ == "__main__":
    node, graph = make_tree()
    array_root = [] # 配列宣言部分木の根番号
    array_list = [] # Arrayクラスを要素に持つ配列
    struct_root = []
    struct_list = []
    # dfs_struct_search(0, graph, node, struct_list)
    dfs_array_search1(0, graph, node, array_root)
    dfs_struct_search1(0, graph, node, struct_root)

    for id in array_root:
        name, type, size = dfs_array_search2(id, graph, node, "", "", "")
        comp = Array(name, type, size)
        array_list.append(comp)

    struct_count = 0
    for id in struct_root:
        dfs_struct_search2(-1, id, graph, node, struct_count)
        struct_count+=1
    
    print(struct_root)
    print(struct_detail)
    print("\n**************Struct_Review**********************")

    struct_review()

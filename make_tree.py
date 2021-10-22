node = []
with open('out.txt', mode='r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        node.append(line)

n = len(node)
depth = [-1]*n # depth[i]:=i行目のノードの深さ

for i in range(n):
    depth[i] = (len(node[i])-len(node[i].lstrip(' ')))//2
print(depth)

# for i in range(n): node[i] = node[i].lstrip(' ')

r = [-1]*n
r[0] = 0
graph = [[] for _ in range(n)]

for i in range(1, n):
    r[depth[i]] = i
    graph[r[depth[i]-1]].append(i)
    graph[i].append(r[depth[i]-1])

print(graph)

# for e in graph[2]:
    # print(node[e])

# 深さ優先探索
def dfs(now):
    print(node[now])
    for next in graph[now]:
        if next < now: continue
        dfs(next)

dfs(0)
# 複雑な深さ優先探索
# struct_list = [] #構造体名を記録するリスト
# array_list = []
# main_on = False

# def DFS(now):
#     for next in graph[now]:
#         if next < now: continue
#         if 'Decl:main' in node[i]:
#             main_on = True
#         if not main_on:
#             # main関数外の読み取り
#             if 'Struct:' in node[now]:
#                 struct_list.append(node[now].replace('Struct', ''))
#         else:
#             # main関数内の読み取り
#             if 'ArrayDecl:' in node[i]:
#                 array_list.append(now)
#         dfs(next)

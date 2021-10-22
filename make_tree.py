node = []
with open('out.txt', mode='r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        node.append(line)

n = len(node)
depth = [-1]*n # depth[i]:=is–Ú‚Ìƒm[ƒh‚Ì[‚³

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

# [‚³—Dæ’Tõ
def dfs(now):
    print(node[now])
    for next in graph[now]:
        if next < now: continue
        dfs(next)

dfs(0)
# •¡G‚È[‚³—Dæ’Tõ
# struct_list = [] #\‘¢‘Ì–¼‚ğ‹L˜^‚·‚éƒŠƒXƒg
# array_list = []
# main_on = False

# def DFS(now):
#     for next in graph[now]:
#         if next < now: continue
#         if 'Decl:main' in node[i]:
#             main_on = True
#         if not main_on:
#             # mainŠÖ”ŠO‚Ì“Ç‚İæ‚è
#             if 'Struct:' in node[now]:
#                 struct_list.append(node[now].replace('Struct', ''))
#         else:
#             # mainŠÖ”“à‚Ì“Ç‚İæ‚è
#             if 'ArrayDecl:' in node[i]:
#                 array_list.append(now)
#         dfs(next)

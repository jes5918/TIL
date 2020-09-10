def dfs(node,r_graph,result):
    for r_node in r_graph[node]:
        if r_node in result:
            continue
        dfs(r_node,r_graph,result)
    result.append(node)

for tc in range(1,11):
    v,e=map(int,input().split())
    node=list(map(int, input().split()))
    r_graph=[[] for _ in range(v+1)]
    result=[]

    for i in range(0,len(node),2):
        r_graph[node[i+1]].append(node[i])

    for i in range(1,v+1):
        if i in result:
            continue
        dfs(i,r_graph,result)

    print('#{}'.format(tc),end=' ')
    for node in result:
        print(node,end=' ')
    print()
#problem - given n nodes and m edges determine if all nodes are reachable from nay nde i.e there is only one connected component
#approach - build an adjacency list of graph , start dfs or bfs from node 1 (for nay node)
#count how many nodes are visited - if the count equals n , the grapgh is connected - print yes otherwise print no

#edge cases - if n-1 ,its trivially connected , if n=0 and n=1 then its disconnected

from collections import defaultdict, deque

def is_connected(n , edges ):
    if n==1:
        return True
    if not edges:
        return False

    #build adjacency list
    graph= defaultdict(list)
    for u , v in edges:
        graph[u].append(v)
        graph[v].append(u)

    #bfs
    visited[false]*(n+1)
    queue= deque([1])
    visited[1]= True
    count=1

    while queue:
        node= queue.popleft()
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour]=True
                queue.append(neighbour)
                count+=1
    return count==n

n , m = map(int , input().split())
edges= [tuple(map(int , input().split())) for _ in range(n)]

print('Yes' if is_connected(n , edges) else 'No')


































# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/133500?language=python3


import sys
sys.setrecursionlimit(10**7)


def solution(n, lighthouse):
    graph = [[] for _ in range(n+1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    
    def dfs(u):
        visited[u] = True
        dp[u][0] = 0
        dp[u][1] = 1
        
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
                dp[u][0] += dp[v][1]
                dp[u][1] += min(dp[v][0], dp[v][1]) # 자식 노드가 dp[v][0]인 경우, 더 비용이 나가는 케이스가 존재
    
    dfs(1)
    
    
    return min(dp[1][0], dp[1][1])


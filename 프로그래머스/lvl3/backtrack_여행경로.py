# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/43164


from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for airport in graph:
        graph[airport].sort(reverse=True)

    stack = ['ICN']   
    path = []       

    while stack:
        top = stack[-1]
        if graph[top]:
            next_airport = graph[top].pop()
            stack.append(next_airport)
        else:
            path.append(stack.pop())

    return path[::-1]





"""
시간 복잡도: O(E logE)
- E => ticket 수
- V => 공항 수

graph 생성 => O(E)
공항별 정렬 => O(E logE)
오일러 트레일 => O(E)
O(E) + O(E logE) + O(E) => O(E logE) (상수 제거)

래프의 오일러 트레일(Eulerian trail) 알고리즘
- 그래프의 모든 간선(edge)를 정확히 한번씩 통과하는 경로를 구하는 알고리즘

오일러 트레일 방식
- edge를 따라 가능한 깊게 따라간다
- 더 이상 나갈 간선이 없으면, 그 정점을 경로에 추가(backtrack)
- 이 후, 남은 간선이 있을 때까지 반복

오일러 트레일 전제
- 모든 노드가 연결
- 모든 간선을 단 한번씩만 통과하는 길

 # 하이엘호저 알고리즘 => 모든 간선을 정확히 한 번만 사용하는 경로를 찾기, 
    # 막다른 길이 나오면 역으로 되돌아오며 경로를 기록

First Trial [X]
"""


# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3

def solution(n: int, costs: list):
    # 부모 노드를 저장하는 배열
    parent = [i for i in range(n)]

    # find 연산: 부모 노드를 재귀적으로 찾고, 경로 압축
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # union 연산: 두 집합을 하나로 합치기
    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    # 비용 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):  # 사이클이 발생하지 않으면 연결
            total_cost += cost

    return total_cost


"""
[해설]
크루스칼 알고리즘 활용
- 간선 중심 연결 => 사이클 회피
- Union-Find 자료구조 활용
"""







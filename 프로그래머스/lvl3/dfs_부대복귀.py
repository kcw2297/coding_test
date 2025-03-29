from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    # [1] 그래프 초기화: 각 지역을 key로 하고, 연결된 이웃 지역들을 리스트로 저장
    graph = defaultdict(list)
    for a, b in roads:
        # roads는 양방향이므로 a <-> b 모두 추가
        graph[a].append(b)
        graph[b].append(a)

    # [2] 거리 정보 초기화: 인덱스가 지역 번호, 값이 destination까지의 최단거리 (-1은 미방문)
    distance = [-1] * (n + 1)

    # [3] BFS 탐색 시작: 목적지(destination)부터 시작
    queue = deque([destination])
    distance[destination] = 0  # 목적지 자신까지의 거리는 0

    # [4] BFS 실행: 큐가 빌 때까지 반복
    while queue:
        current = queue.popleft()  # 현재 지역

        # [5] 현재 지역과 연결된 모든 이웃 지역을 확인
        for neighbor in graph[current]:
            # 아직 방문하지 않은 지역이면 (거리 정보가 -1이면)
            if distance[neighbor] == -1:
                # 현재까지의 거리 + 1로 설정 (간선의 가중치가 모두 1이므로)
                distance[neighbor] = distance[current] + 1
                # 이후 탐색을 위해 큐에 추가
                queue.append(neighbor)

    # [6] 각 source에서 destination까지의 최단거리 결과를 리스트로 반환
    # 도달 불가능한 경우에는 -1로 유지됨
    return [distance[source] for source in sources]
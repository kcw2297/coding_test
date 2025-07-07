# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/87694


from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 102  # 2배 확장: 최대 좌표 50 * 2 + 2
    board = [[0] * SIZE for _ in range(SIZE)]

    # 1. 사각형 영역을 채움
    for x1, y1, x2, y2 in rectangle:
        # 2배 확장
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # 테두리면 1, 내부면 2
                if x == x1 or x == x2 or y == y1 or y == y2:
                    if board[x][y] != 2:
                        board[x][y] = 1
                else:
                    board[x][y] = 2


    # 2. BFS 시작
    q = deque()
    visited = [[False] * SIZE for _ in range(SIZE)]
    startX, startY = characterX * 2, characterY * 2
    endX, endY = itemX * 2, itemY * 2
    q.append((startX, startY, 0))
    visited[startX][startY] = True

    # 4방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, dist = q.popleft()
        if x == endX and y == endY:
            return dist // 2  # 2배 확장했으니 실제 거리는 절반

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))




# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/136797


from collections import defaultdict, deque

def solution(numbers):
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    
    # 숫자 -> 좌표 매핑
    pos = {}
    for r in range(4):
        for c in range(3):
            pos[keypad[r][c]] = (r, c)
    
    # 두 숫자 간 최소 거리 (가중치) 계산
    def calc_cost(start, end):
        if start == end:
            return 1
        sr, sc = pos[start]
        er, ec = pos[end]
        dr, dc = abs(sr - er), abs(sc - ec)
        if dr + dc == 1:
            return 2  # 상하좌우
        elif dr == 1 and dc == 1:
            return 3  # 대각선
        else:
            # 복잡한 경우: BFS로 최단 가중치 계산
            visited = set()
            queue = deque([(sr, sc, 0)])
            while queue:
                r, c, cost = queue.popleft()
                if (r, c) == (er, ec):
                    return cost
                for nr, nc, move_cost in [(r+1,c,2),(r-1,c,2),(r,c+1,2),(r,c-1,2),
                                          (r+1,c+1,3),(r-1,c-1,3),(r+1,c-1,3),(r-1,c+1,3)]:
                    if 0 <= nr < 4 and 0 <= nc < 3:
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc, cost + move_cost))
    
    # 모든 쌍에 대해 비용 미리 계산
    cost_map = {}
    digits = [1,2,3,4,5,6,7,8,9,0]
    for a in digits:
        for b in digits:
            cost_map[(a, b)] = calc_cost(a, b)

    dp = defaultdict(int)
    # 시작 상태: 왼손 4, 오른손 6
    dp[(4, 6)] = 0

    for ch in numbers:
        num = int(ch)
        new_dp = defaultdict(int)
        for (left, right), cur_cost in dp.items():
            if num == left:
                # 왼손 그대로 사용
                new_dp[(num, right)] = min(new_dp[(num, right)], cur_cost + 1)
            elif num == right:
                # 오른손 그대로 사용
                new_dp[(left, num)] = min(new_dp[(left, num)], cur_cost + 1)
            else:
                # 왼손 이동
                new_dp[(num, right)] = min(new_dp[(num, right)], cur_cost + cost_map[(left, num)])
                # 오른손 이동
                new_dp[(left, num)] = min(new_dp[(left, num)], cur_cost + cost_map[(right, num)])
        dp = new_dp

    return min(dp.values())


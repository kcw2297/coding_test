# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/150365


def solution(n, m, x, y, r, c, k):
    # 출발점과 도착점 사이 최소 이동 횟수 (맨해튼 거리)
    min_distance = abs(x - r) + abs(y - c)
    
    # k번 안에 도달 가능한지, k와 최소거리의 홀짝이 맞는지 확인
    if min_distance > k or (k - min_distance) % 2 != 0:
        return "impossible"
    
    # 방향 우선순위: 사전순으로 가장 빠른 문자열을 위해
    # 'd' < 'l' < 'r' < 'u'
    moves = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    result = []
    cur_x, cur_y = x, y
    rem = k  # 남은 이동 횟수
    
    # 남은 이동 횟수만큼 반복
    for _ in range(k):
        found = False
        # 사전순으로 가능한 이동 방향을 시도합니다.
        for ch, dx, dy in moves:
            nx, ny = cur_x + dx, cur_y + dy
            # 격자 범위를 벗어나면 continue
            if not (1 <= nx <= n and 1 <= ny <= m):
                continue
            
            # 목표까지의 남은 맨해튼 거리
            dist = abs(nx - r) + abs(ny - c)
            # 남은 이동 횟수에서 1을 사용한 후, 목표까지 도달 가능한지 (남은 이동횟수 >= 거리)
            # 그리고 (남은 이동횟수 - 거리)의 홀짝성도 일치해야 한다.
            if dist <= rem - 1 and (rem - 1 - dist) % 2 == 0:
                result.append(ch)
                cur_x, cur_y = nx, ny
                rem -= 1
                found = True
                break
        
        # 어떤 이동도 선택할 수 없다면 경로 구성 불가능
        if not found:
            return "impossible"
    
    # 모든 이동을 사용한 후 정확히 목표에 도착했는지 확인
    return "".join(result) if (cur_x, cur_y) == (r, c) else "impossible"



"""
해설:
맨헤튼 거리 
설명 => 2차원 평면 공간에서 두 점 p와 q 사이의 거리를 측정하는 방법
공식 => ∣p1−q1∣ + ∣p2−q2∣
"""




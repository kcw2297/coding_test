# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/68646


def solution(a):
    n = len(a)
    
    # 왼쪽에서부터의 최소값을 저장할 리스트
    left_min = [0] * n
    left_min[0] = a[0]
    
    for i in range(1, n):
        # 왼쪽에서 현재 위치까지의 최소값을 저장
        left_min[i] = min(left_min[i - 1], a[i])

    # 오른쪽에서부터의 최소값을 저장할 리스트
    right_min = [0] * n
    right_min[-1] = a[-1]
    
    for i in range(n - 2, -1, -1):
        # 오른쪽에서 현재 위치까지의 최소값을 저장
        right_min[i] = min(right_min[i + 1], a[i])
    
    # 살아남을 수 있는 풍선 개수 카운트
    count = 0

    for i in range(n):
        # 현재 풍선이 왼쪽 최소값보다 작거나 혹은 오른쪽 최소값보다 작으면 최후까지 살아남을 수 있음
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            count += 1

    return count
    


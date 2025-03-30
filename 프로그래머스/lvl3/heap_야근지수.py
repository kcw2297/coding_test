# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/12927


import heapq

def solution(n, works):
    max_heap = []
    
    # works의 최대 값을 순차적으로 빼는 문제로, 최대힙 사용
    for work in works:
      heapq.heappush(max_heap, (-work, work))

    for _ in range(n):
        max_work = heapq.heappop(max_heap)[1]
        if not max_work:
            return 0
        
        heapq.heappush(max_heap, (-(max_work-1), max_work-1))

    result = 0
    while max_heap:
        current_work = heapq.heappop(max_heap)[1]
        if current_work:
            result += current_work**2

    return result
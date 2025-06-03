# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/86053


def solution(a, b, g, s, w, t):
    n = len(g)
    
    left, right = 0, 10**18
    answer = right
    
    while left <= right:
        mid = (left + right) // 2  # 검사할 시간 T
        
        total_gold = 0     # T 시간에 운반 가능한 금 합계
        total_silver = 0   # T 시간에 운반 가능한 은 합계
        total_both = 0     # T 시간에 운반 가능한 (금+은) 합계
        
        for i in range(n):
            # 한 도시 i의 트럭이 왕복 가능한 횟수
            # 편도 t[i] -> 왕복 2*t[i]
            round_trips = mid // (2 * t[i])
            
            # 만약 마지막에 돌아올 필요 없이 한 번 더 편도로 갈 수 있다면
            if mid % (2 * t[i]) >= t[i]:
                round_trips += 1
            
            # i번 트럭이 운반할 수 있는 최대 총 중량
            capacity = round_trips * w[i]
            
            # 실제로 금, 은, 둘 합계 중에서 얼마나 가져올 수 있는지 계산
            take_gold = min(g[i], capacity)
            take_silver = min(s[i], capacity)
            take_both = min(g[i] + s[i], capacity)
            
            total_gold += take_gold
            total_silver += take_silver
            total_both += take_both
        
        # 목표치를 모두 채울 수 있는지 확인
        if total_gold >= a and total_silver >= b and total_both >= a + b:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer




"""
시간 복잡도: O(logN)

binary search => 탐색 범위 => 이 문제에서는 (시간)을 기준으로 최적의 시간값 도출

First Trial[X]
"""

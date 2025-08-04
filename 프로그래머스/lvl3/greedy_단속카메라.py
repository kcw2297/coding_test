# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    
    result = 0
    camera_pos = -30001 
    
    for route in routes:
        if route[0] > camera_pos:
            camera_pos = route[1]  
            result += 1
    
    return result


"""
First Trial: [X]
시간 복잡도: N log(N) => 초기 정렬 
알고리즘 유형: Greedy
"""


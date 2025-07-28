# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/12938



def solution(n, s):
    if n > s:
        return [-1]
    
    result = []

    quotient = s // n
    remainder = s % n
    
    result = [ quotient for _ in range(n)]

    for i in range(remainder):
        result[i] += 1

    return sorted(result)
    


"""
First Trial: [O]
"""

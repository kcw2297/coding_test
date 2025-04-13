# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/131703


import copy
from itertools import product


def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    min_count = float('inf')

    # 행을 뒤집을 경우의 수를 완전탐색
    for row_flip in product([False, True], repeat=n):
        temp = copy.deepcopy(beginning)
        flip_count = 0

        # 1. 행 뒤집기
        for i in range(n):
            if row_flip[i]:
                flip_count += 1
                for j in range(m):
                    temp[i][j] ^= 1  # 0 -> 1, 1 -> 0

        # 2. 열 뒤집기 판단
        for j in range(m):
            if temp[0][j] != target[0][j]:
                flip_count += 1
                for i in range(n):
                    temp[i][j] ^= 1

        # 3. 결과가 타겟과 일치하는지 확인
        if temp == target:
            min_count = min(min_count, flip_count)

    return min_count if min_count != float('inf') else -1



"""
이진 행렬: B = {0, 1}의 항목이있는 행렬이다. 이러한 행렬은 한 쌍의 유한 집합 사이의 이진 관계(이항관계)를 나타 내기 위해 사용될 수 있다.
행 => 완전탐색(brute-force)
열 => greedy
"""


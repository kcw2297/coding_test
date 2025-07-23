# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/12942


# 일반적인 dp 풀이안
# def solution(matrix_sizes):
#     n = len(matrix_sizes)
#     dp = [[float('inf')] * n for _ in range(n)]

#     # 자기 자신 곱셈은 0
#     for i in range(n):
#         dp[i][i] = 0

#     # chain_len: 부분 행렬 체인의 길이
#     for chain_len in range(2, n + 1):
#         for i in range(n - chain_len + 1):
#             j = i + chain_len - 1
#             for k in range(i, j):
#                 # cost: 왼쪽 dp + 오른쪽 dp + 둘을 합치는 cost
#                 cost = (
#                     dp[i][k] +
#                     dp[k + 1][j] +
#                     matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]
#                 )
#                 if cost < dp[i][j]:
#                     dp[i][j] = cost
#     return dp[0][n - 1]


# 비용 최적화 정답안
def solution(matrix_sizes):
    n = len(matrix_sizes)
    
    """ p 변수 역할
        p[i] = 행렬 i의 row, p[i+1] = 행렬 i의 col
        p는 각 행렬의 row와 col을 차례로 이어 붙인 배열.
        
        A: 5x3, B: 3x10, C: 10x6일 때,
        → p = [5, 3, 10, 6]
        즉, i번째 행렬은 p[i] x p[i+1] 크기입니다.
    """
    p = [matrix_sizes[0][0]] + [ms[1] for ms in matrix_sizes]
    
    # dp[i][j]: i번째~j번째 행렬을 곱하는 데 필요한 최소 곱셈 연산 수를 저장.    
        # 예: dp[0][0]	A
        # 예: dp[0][1]	AB
        # 예: dp[0][2]	ABC
        # 예: dp[1][2]	BC
        # 예: dp[1][3]	BCD
    dp = [[0] * n for _ in range(n)]

    # 부분 체인 길이, l: 곱하려는 연속된 행렬 개수 (2개~n개)
        # dp의 작은 문제 => 큰 문제 순차적 파악 목적
        # 예: 체인 2 => (A,B), (B,C), (C,D)
        # 예: 체인 3 => (A)(BC) or (AB)(C), (B)(CD) or (BC)(D)
        # 예: 체인 4 => (A)(BCD), (AB)(CD), (ABC)(D)
            # 결국 작은 체인의 결과 값을 이용 가능
            
    for l in range(2, n+1):
        # i: 부분 체인의 시작 인덱스
        for i in range(n - l + 1):
            # j: 부분 체인의 끝 인덱스
            j = i + l - 1
            # dp 값 저장하기 전 inf로 초기화
            dp[i][j] = float('inf')
            
            # 괄호 위치 k를 순회하며 최소값 찾기, i~j 사이에서 어디서 괄호를 칠지 모든 위치(k)를 확인
            for k in range(i, j):
                # 예: k 0 => ((A)B)C
                # 예: k 1 => (A)(BC)
                # dp[0][0] + dp[1][2] + p[0] * p[1] * p[3]
                    # dp는 이전 단계에 저장해둔 값
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]

                if cost < dp[i][j]:
                    dp[i][j] = cost
   
    return dp[0][n-1]




"""
First Trial: [X]
"""
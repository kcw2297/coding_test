# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    MOD = 1_000_000_007
    dp = [0] * (n + 1)
    dp[0] = 1  
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin] % MOD
    return dp[n]


"""
First Trial: [X]

dp => 특정 값을 도달하기 위해 중간 값을 버퍼/캐싱 하는 특징
    => n까지의 값에 도달하기 위해 중간 과정인 결과값을 dp에 저장

시간 복잡도: N * M
- money 순회
- coin ~ n 순회

"""



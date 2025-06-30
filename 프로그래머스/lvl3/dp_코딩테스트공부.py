# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/118668



def solution(alp, cop, problems):
    # TODO: 최대 alp, cop 값 할당
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)

    # TODO: 최소 alp, cop 값 할당
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    # TODO: 최대 경우에서 +1을 한 상태 및 인덱스를 고려해 +2 실행
    # TODO: dp => 해당 상태까지 걸리는 최소 시간
    dp = [[float('inf')] * (max_cop + 2) for _ in range(max_alp + 2)]

    # TODO: 시작 상태 0시간
    dp[alp][cop] = 0

    # TODO: 가능한 모든 능력치 조합에 대해 순회, 모든 상태를 그리드 순회하면서 DP 값을 갱신합니다.
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    # TODO: 보상이 지나치게 커져도 목표 이상은 고려 안 한다는 뜻.
                    new_alp = min(max_alp, a + alp_rwd)
                    new_cop = min(max_cop, c + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[a][c] + cost)

    return dp[max_alp][max_cop]



"""
First Trial [X]
"""






# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/131129?language=python3

import sys

def solution(target):
    MAX = sys.maxsize
    
    # 가능한 점수와 싱글/불 여부 표시
    scores = []
    for i in range(1, 21):
        scores.append((i, 1))       # 싱글
        scores.append((i * 2, 0))  # 더블
        scores.append((i * 3, 0))  # 트리플
    scores.append((50, 1))          # 불

    dp = [(MAX, 0)] * (target + 1)
    dp[0] = (0, 0)  # (던진 횟수, 싱글/불 개수)

    for i in range(1, target + 1):
        for score, is_single_or_bull in scores:
            if i - score >= 0:
                prev_darts, prev_s_or_b = dp[i - score]
                new_darts = prev_darts + 1
                new_s_or_b = prev_s_or_b + is_single_or_bull

                # 더 적은 다트를 사용하거나,
                # 다트 수가 같다면 싱글/불을 더 많이 쓴 경우로 갱신
                if new_darts < dp[i][0] or (new_darts == dp[i][0] and new_s_or_b > dp[i][1]):
                    dp[i] = (new_darts, new_s_or_b)

    return list(dp[target])


"""
First Trial: [X]
"""
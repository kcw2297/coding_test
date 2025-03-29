# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/258709

from itertools import combinations
from collections import defaultdict

def solution(dice):
    # [INFO] A와 B가 반반의 주사위를 가집니다.
    n = len(dice)
    half = n // 2

    def compute_distribution(dice_subset: list) -> dict:
        """
            합성곱을 통해 주사위의 경우의 수열들을 합칩니다.
            
            A 주사위 합 분포:   {1:1, 2:1, 3:1}      (주사위1)
            B 주사위:           [2, 4, 6]            (주사위2)

            → 가능한 조합:
                1 + 2 = 3
                1 + 4 = 5
                ...
                3 + 6 = 9
        """
        dp = {0: 1}  # 초기 합 0, 경우의 수 1, 초기 시작인 상황은 오직 1가지 경우를 의미
        for d in dice_subset:
            new_dp = defaultdict(int)

            for current_sum, cnt in dp.items():
                for face in d:
                    new_dp[current_sum + face] += cnt # 이전까지 나온 합분포를 합산
            dp = new_dp # 새로운 수열을 할당
        return dp # 현재 주사위(수열)들의 누적(합성곱) 합을 반환

    best_win_count = -1 
    best_combination = None

    dice_indices = list(range(n))
    
    # [INFO] combination과 합성곱을 통해 전체 합상 경우의 수를 확인
    for comb in combinations(dice_indices, half):
        A_dice = [dice[i] for i in comb]
        B_dice = [dice[i] for i in dice_indices if i not in comb]

        dist_A = compute_distribution(A_dice)
        dist_B = compute_distribution(B_dice)

        win_count = 0 

        for sum_A, count_A in dist_A.items():
            for sum_B, count_B in dist_B.items():
                if sum_A > sum_B:
                    win_count += count_A * count_B 

        if win_count > best_win_count:
            best_win_count = win_count
            best_combination = comb

 
    return sorted([i + 1 for i in best_combination])



"""
합성곱 => 두 개의 수열을 결합해서 새로운 수열을 만드는 연산
합성곱 정의 링크 => https://namu.wiki/w/%ED%95%A9%EC%84%B1%EA%B3%B1

합성곱에서는 모든 조합을 개별적으로 계산해야 합니다.

경우의 수는 => (A의 한 면) + (B의 한 면) = 합 → 이 한 조합이 1가지 경우입니다.
"""



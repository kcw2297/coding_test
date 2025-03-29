from collections import defaultdict
from itertools import combinations

def solution(dice):
    half = len(dice) // 2
    dice_indices = list(range(len(dice)))
    
    current_max_value = -1
    current_comb = []
    
    
    def compute_convolution(dice_subset: list) -> dict:
        dp = {0: 1}
           

        for d in dice_subset:
            new_dp = defaultdict(int)
            
            for current_sum, cnt in dp.items():
                for face in d:
                    new_dp[current_sum + face] += cnt
            dp = new_dp

        return dp
    
    
    # [INFO] combination을 통해 A_dice와 B_dice가 나오는 경우의 수를 모두 고려
    for comb in combinations(dice_indices, half):
        A_dice = [dice[i] for i in comb]
        B_dice = [dice[i] for i in dice_indices if i not in comb]        

        
        return
    

    
    return [i + 1 for i in sorted(current_comb)]



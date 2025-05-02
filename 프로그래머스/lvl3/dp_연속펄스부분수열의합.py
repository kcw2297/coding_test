# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/161988



def solution(sequence: list):
    dp_pos = sequence[0]
    dp_neg = -sequence[0]

    max_sum = max(dp_pos, dp_neg)

    for x in sequence[1:]:
        new_dp_pos = max(dp_neg + x, x)
        new_dp_neg = max(dp_pos - x, -x)                

        max_sum = max(max_sum, new_dp_pos, new_dp_neg)

        dp_pos = new_dp_pos
        dp_neg = new_dp_neg

    return max_sum
        



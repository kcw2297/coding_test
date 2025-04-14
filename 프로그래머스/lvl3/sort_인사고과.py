# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/152995



def solution(scores: list) -> int:
    # 완호의 점수와 두 점수 합을 미리 구해 둡니다.
    target = scores[0]
    target_sum = target[0] + target[1]
    
    # 인덱스 정보를 함께 저장합니다.
    scores_with_idx = [(a, b, idx) for idx, (a, b) in enumerate(scores)]
    
    # '근무 태도' 점수를 기준으로 내림차순, 같은 경우 '동료 평가' 점수를 오름차순으로 정렬합니다.
    scores_with_idx.sort(key=lambda x: (-x[0], x[1]))
    
    max_peer = -1          # 지금까지 나온 동료 평가 점수의 최대값
    eligible_sums = []     # 인센티브 대상 사원의 두 점수 합을 저장
    target_is_eligible = False  # 완호(인덱스 0)가 대상인지 여부
    
    # 정렬된 순서대로 탐색하며 탈락 여부를 판별합니다.
    for a, b, idx in scores_with_idx:
        # 현재 사원의 동료 평가 점수가 지금까지 나온 최대 점수보다 작다면
        # 앞서 나온 사원 중 적어도 하나가 두 점수 모두 더 높으므로 탈락합니다.
        if b < max_peer:
            if idx == 0:  # 만약 완호라면 바로 -1 반환
                return -1
            continue
        
        # 탈락하지 않은 경우, 현재 사원은 인센티브 대상입니다.
        max_peer = b          # 동료 평가 점수 최대값 갱신
        eligible_sums.append(a + b)
        if idx == 0:
            target_is_eligible = True
    
    # 혹시 완호가 인센티브 대상이 아니라면 -1을 반환합니다.
    if not target_is_eligible:
        return -1
    
    # 인센티브 대상자 중 완호보다 합계 점수가 높은 사원의 수를 카운트합니다.
    higher_count = sum(1 for s in eligible_sums if s > target_sum)
    
    # 순위는 (자신보다 높은 사원 수 + 1) 입니다.
    return higher_count + 1
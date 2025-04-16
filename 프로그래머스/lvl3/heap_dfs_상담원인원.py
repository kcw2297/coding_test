# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/214288

from heapq import heappush, heappop
from collections import defaultdict

def simulate_requests(requests, mentor_count):
    """
    주어진 상담 요청(requests: [(시작시각, 상담시간), ...])
    와 mentor_count (해당 유형에 배정된 멘토 수)가 주어지면,
    상담 시뮬레이션을 진행하여 전체 대기 시간의 합을 반환합니다.
    
    시뮬레이션 방식:
      - 모든 멘토는 처음에 0분에 상담 가능(즉, 빈 상태)입니다.
      - 각 요청에 대해, 가장 빠르게 상담 가능한 멘토를 선택합니다.
      - 상담 시작 시간은 max(요청 시각, 멘토의 현재 가능 시각)입니다.
      - 기다린 시간은 (상담 시작 시각 - 요청 시각)이며, 상담이 시작되면
        해당 멘토의 다음 가능 시각은 (상담 시작 시각 + 상담시간)으로 갱신됩니다.
    """
    heap = [0] * mentor_count  # 멘토가 사용할 수 있는 시각을 저장 (초기: 모두 0)
    total_wait = 0
    for start, duration in requests:
        avail = heappop(heap)  # 가장 빨리 상담 가능한 멘토 선택
        start_consult = max(avail, start)  # 상담 시작 시간
        wait_time = start_consult - start       # 대기 시간 = 상담 시작 시간 - 요청 시각
        total_wait += wait_time
        heappush(heap, start_consult + duration)  # 해당 멘토의 다음 가능 시각 업데이트
    return total_wait

def solution(k, n, reqs):
    """
    k: 상담 유형의 개수
    n: 전체 멘토 수 (각 유형에 최소 1명씩 할당해야 함)
    reqs: 각 상담 요청 [시작시각, 상담시간, 상담유형]
    
    전체 로직:
      1. 각 상담 유형별로 요청을 분리합니다.
      2. 각 유형에 대해 1 ~ n명 할당 시의 전체 대기 시간(simulation result)을 미리 구합니다.
      3. 각 유형에 최소 1명씩 배정하며, 전체 멘토 수가 n이 되는 모든 경우를 DFS(혹은 완전탐색)로 확인하여
         전체 대기 시간 합이 최소가 되는 값을 찾습니다.
    """
    # 1. 유형별 상담 요청 분리
    cat_reqs = defaultdict(list)
    for a, b, c in reqs:
        # 각 요청은 (시작시각, 상담시간) 형태로 저장
        cat_reqs[c].append((a, b))
    # 안전하게 요청 시각 기준 정렬 (입력에 정렬되어 있다고 하더라도)
    for c in cat_reqs:
        cat_reqs[c].sort(key=lambda x: x[0])
    
    # 2. 유형별 멘토 수에 따른 시뮬레이션 결과 사전(sim[c][멘토수])
    sim = {}
    for c in range(1, k+1):
        sim[c] = {}
        # 만약 해당 유형에 요청이 없다면 대기 시간은 0입니다.
        if c not in cat_reqs:
            for m in range(1, n+1):
                sim[c][m] = 0
        else:
            for m in range(1, n+1):
                sim[c][m] = simulate_requests(cat_reqs[c], m)
    
    # 3. DFS를 이용해 각 유형에 할당할 멘토 수를 결정 (각 유형 최소 1명 할당)
    #    할당한 경우의 전체 대기 시간의 합이 최소가 되는 값(best)을 찾습니다.
    best = float('inf')
    
    def dfs(i, remain, current_sum):
        """
        i: 현재까지 배정 완료한 유형의 개수 (0부터 k-1까지)
        remain: 할당할 수 있는 남은 멘토 수
        current_sum: 지금까지 누적된 대기 시간 합
        """
        nonlocal best
        if i == k:
            if remain == 0:
                best = min(best, current_sum)
            return
        
        # i번째 유형(실제 유형은 i+1)에 적어도 1명의 멘토를 할당합니다.
        # 남은 멘토 수가 remain이고, 나머지 유형에는 최소 1명씩 필요하므로 x의 범위는
        # 1부터 remain - (k - i - 1) 까지 가능합니다.
        for x in range(1, remain - (k - i - 1) + 1):
            dfs(i+1, remain - x, current_sum + sim[i+1][x])
    
    dfs(0, n, 0)
    return best



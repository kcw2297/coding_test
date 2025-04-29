# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/258707



def solution(coin: int, cards: list[int]) -> int:
    n = len(cards)
    # 1) 초기 손에 든 카드 개수, 드로우 라운드 수
    initial = n // 3
    M = (n - initial) // 2  # 최대 드로우 라운드

    # 2) 각 카드의 원위치 인덱스
    pos = {c: i for i, c in enumerate(cards)}
    target = n + 1

    # 3) 보완쌍 j에 대해 (활성화 라운드 r_j, 비용 c_j) 계산
    pairs: list[tuple[int,int]] = []
    for x in range(1, target // 2 + 1):
        y = target - x
        p1, p2 = pos[x], pos[y]

        # 손에 든 카드면 round=0, 아니면 드로우 순서 계산
        def draw_round(p: int) -> int:
            if p < initial:
                return 0
            return (p - initial) // 2 + 1

        r = max(draw_round(p1), draw_round(p2))
        r = max(1, r)  # 최소 round 1부터 매칭 가능

        cost = (1 if p1 >= initial else 0) + (1 if p2 >= initial else 0)
        pairs.append((r, cost))

    # 4) L 드로우 라운드 생존 가능 여부 검사
    INF = 10**18
    def can_survive(L: int) -> bool:
        if L == 0:
            return True
        # 활성화 라운드 ≤ L인 쌍만 남기고, 라운드 순으로 정렬
        tasks = [(r,c) for (r,c) in pairs if r <= L]
        tasks.sort(key=lambda t: t[0])

        # dp[j] = j개 쌍을 쓰기 위한 최소 코인 소모
        dp = [INF] * (L + 1)
        dp[0] = 0

        # 유효성: j번째로 고른 쌍의 활성화 라운드 r_j는 j ≤ r_j 이어야 함
        # (j번째 가장 느린 활성화 ≤ 그 라운드 번호)
        for r, c in tasks:
            # 뒤에서부터 갱신
            upper = min(L, len(tasks))
            for j in range(upper, 0, -1):
                # j번째로 이 쌍을 고를 때
                if r <= j and dp[j-1] + c < dp[j]:
                    dp[j] = dp[j-1] + c

        return dp[L] <= coin

    # 5) 이분탐색으로 최대 L 찾기
    lo, hi, best = 0, M, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_survive(mid):
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    # 6) 게임에서 도달할 라운드는 '드로우 생존 라운드 + 1'
    return best + 1







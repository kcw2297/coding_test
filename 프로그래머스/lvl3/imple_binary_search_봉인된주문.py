# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/389481



from bisect import bisect_left

def solution(n: int, bans: list[str]) -> str:
    """
        알파벳 고려 시: 
        길이별 조합 가능한 알파벳 개수 => 26 ^ n
    """
    # 1) banned 문자열을 길이별로 정리하고 정렬
    banned_by_len = {L: [] for L in range(1, 12)}
    
    for b in bans:
        L = len(b)
        if 1 <= L <= 11:
            banned_by_len[L].append(b)
    
    for L in banned_by_len:
        banned_by_len[L].sort()
    
    # 2) 길이 별, 조합 가능한 알파벳 개수
    pow26 = [1] * 12
    for i in range(1, 12):
        pow26[i] = pow26[i-1] * 26

    rem = n
    # 3) 길이 1부터 11까지 순차적으로 몇 개의 문자열이 남는지 확인
    for L in range(1, 12):
        total = pow26[L]
        banned_cnt = len(banned_by_len[L])
        avail = total - banned_cnt
        if rem > avail:
            rem -= avail
        else:
            # 4) 이 길이 L 안에서 rem번째(=k번째) 문자열을 찾는다
            k = rem
            banned_list = banned_by_len[L]
            prefix = ""
            # 각 자리마다 알파벳을 하나씩 결정
            for pos in range(L):
                for ci in range(26):
                    c = chr(ord('a') + ci)
                    npref = prefix + c
                    
                    cnt_sub = pow26[L - pos - 1] # 남은 자리수의 알파벳 조합 총 개수
                    
                    lo = bisect_left(banned_list, npref)
                    hi = bisect_left(banned_list, npref + '{')
                    banned_sub = hi - lo # 해당 문자열 길이의 ban 개수

                    good_sub = cnt_sub - banned_sub
                    if k > good_sub:
                        k -= good_sub
                    else:
                        prefix = npref
                        break
            return prefix
    # 범위를 벗어나면 빈 문자열
    return ""







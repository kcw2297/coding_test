# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/389481


"""
문제 설명
어느 날, 전설 속에 전해 내려오는 비밀 주문서가 세상에 다시 모습을 드러냈습니다. 이 주문서에는 마법 세계에서 사용되는 모든 주문이 적혀 있는데, 각 주문은 알파벳 소문자 11글자 이하로 구성되어 있습니다. 주문서에는 실제로 마법적 효과를 지니지 않는 의미 없는 주문들 즉, 알파벳 소문자 11글자 이하로 쓸 수 있는 모든 문자열이 고대의 규칙에 따라 아래와 같이 정렬되어 있습니다.

글자 수가 적은 주문부터 먼저 기록된다.
글자 수가 같다면, 사전 순서대로 기록된다.
예를 들어, 주문서의 시작 부분은 다음과 같이 구성됩니다.

"a"→"b"→"c"→"d"→"e"→"f"→...→"z"
→"aa"→"ab"→...→"az"→"ba"→...→"by"→"bz"→"ca"→...→"zz"
→"aaa"→"aab"→...→"aaz"→"aba"→...→"azz"→"baa"→...→"zzz"
→"aaaa"→...→"aazz"→"abaa"→...→"czzz"→"daaa"→...→"zzzz"
→"aaaaa"→...
하지만 이 주문서에는 오래전 봉인된 저주받은 주문들이 숨겨져 있었고, 이를 악용하려는 자들을 막기 위해 마법사들이 몇몇 주문을 주문서에서 삭제했습니다. 당신은 삭제가 완료된 주문서에서 n번째 주문을 찾아내야 합니다.

예를 들어, 주문서에서 "d", "e", "bb", "aa", "ae" 5개의 주문을 지웠을 때, 주문서에서 30번째 주문을 찾으려고 합니다.

1~3번째 주문은 "a", "b", "c" 입니다.
"d"와 "e"는 삭제됐으므로 4~24번째 주문은 "f" ~ "z"입니다.
"aa"는 삭제됐으므로 25~27번째 주문은 "ab", "ac", "ad"입니다.
"ae"는 삭제됐으므로 28~30번째 주문은 "af", "ag", "ah"입니다.
따라서 30번째 주문은 "ah"가 됩니다. 삭제된 주문 중 “bb”와 같이 n번째 주문보다 뒤에 위치해 있어서 n번째 주문을 찾는 데 영향을 주지 않는 주문도 존재할 수 있습니다.

정수 n과 삭제된 주문들을 담은 1차원 문자열 배열 bans가 매개변수로 주어질 때, 삭제가 완료된 주문서의 n번째 주문을 return 하도록 solution 함수를 완성해 주세요.

제한사항
1 ≤ n ≤ 1015
1 ≤ bans의 길이 ≤ 300,000
bans의 원소는 알파벳 소문자로만 이루어진 길이가 1 이상 11 이하인 문자열입니다.
bans의 원소는 중복되지 않습니다.
입출력 예
n	bans	result
30	["d", "e", "bb", "aa", "ae"]	"ah"
7388	["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]	"jxk"
테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹 내의 테스트 케이스를 모두 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹	총점	추가 제한 사항
#1	15%	n ≤ 1,000, bans의 길이 ≤ 100
#2	15%	n ≤ 1,000,000
#3	70%	추가 제한 사항 없음
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

주어진 주문을 지운 후 주문서의 7,388 번째 주문은 "jxk"입니다.
따라서 "jxk"를 return 합니다.
"""

from bisect import bisect_left
from collections import defaultdict

def solution(n, bans) -> str:
    # 1) banned 문자열을 길이별로 정리하고 정렬
    banned_by_len = defaultdict(list)
    for ban in bans:
        banned_by_len[len(ban)].append(ban)
    
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







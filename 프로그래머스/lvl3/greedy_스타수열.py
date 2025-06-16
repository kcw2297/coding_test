# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/70130


from collections import Counter

def solution(a):
    counter = Counter(a)

    max_length = 0

    for key in counter:

        # TODO: 최적화 조건 => key 기준으로, 부분 수열 최대 길이보다 적을 시 넘김
        if counter[key] * 2 <= max_length:
            continue  

        # TODO: key로 만들 수 있는 쌍 개수
        pair_count = 0
        i = 0


        while i < len(a) - 1:
            if (a[i] != a[i+1]) and (key == a[i] or key == a[i+1]):
                pair_count += 1
                i += 2 
            else:
                i += 1

        max_length = max(max_length, pair_count * 2)

    return max_length


"""
First Trial[X]



"""


# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/67258


from collections import defaultdict

def solution(gems):
    # TODO: 전체 보석 종류 수
    total_types = len(set(gems))
    gem_count = defaultdict(int)
    
    answer = [0, len(gems) - 1]
    start = 0
    
    # TODO: gems 전체 개수를 순회하며 최소 범위 파악
    for end in range(len(gems)):
        # TODO: 현재 순회의 보석을 임시 캐싱에 추가
        gem_count[gems[end]] += 1 
        
        # TODO: 모든 보석이 포함되는 구간인 경우, 최소 범위 확인
        while len(gem_count) == total_types:
            # TODO: 현재 구간이 기존 정답보다 짧은 경우 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            # TODO: start 포인터를 이동하며 윈도우를 줄일 수 있는지 확인
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]
            start += 1
    

    # 진열대 번호는 1부터 시작하므로 +1
    return [answer[0] + 1, answer[1] + 1]



"""
First Trial[X]

시간 복잡도: O(100_000) => gems 최대 개수

"""




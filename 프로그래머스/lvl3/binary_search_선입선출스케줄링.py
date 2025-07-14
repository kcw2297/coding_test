# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/12920



def solution(n, cores):
    if n <= len(cores):
        return n  # 초기 작업은 바로 각 코어에 할당됨

    # 이진 탐색 범위 설정
    left = 0
    right = max(cores) * n

    # 작업 수 기준으로 최소 시간 탐색
    while left < right:
        mid = (left + right) // 2

        # mid 시간까지 처리 가능한 작업 수 계산
        done = len(cores)  # 0초에 각 코어가 하나씩 작업 시작함
        for core in cores:
            done += mid // core

        if done >= n:
            right = mid
        else:
            left = mid + 1

    # right (또는 left): 마지막 작업이 끝나는 시간
    t = right
    done = len(cores)
    for core in cores:
        done += (t - 1) // core  # 직전 시간까지 끝난 작업 수

    # t 시점에 끝나는 작업 중에서 n번째 작업 찾기
    for i, core in enumerate(cores):
        if t % core == 0:
            done += 1
            if done == n:
                return i + 1  # 코어 번호는 1부터 시작


"""
First Trial: [X]

"""
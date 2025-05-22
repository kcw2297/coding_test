# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/42895


def solution(N, number):
    # TODO: dp의 각 idx별, N의 사용 횟수에 따라 만들 수 있는 값 할당
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # TODO: dp i번에 N이 i번 중첩된 값을 할당
        dp[i].add(int(str(N) * i))

        # TODO: dp 내에, N을 i번 사용해 얻을 수 있는 값 조합 연산
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b)

        if number in dp[i]:
            return i

    return -1



"""
시간 복잡도: O(8² * M²)
- 8² => i * j(8제한)
- M => dp[j]의 평균 크기 * dp[i-j]의 평균 크기
  - 각 dp내 값이 크지 않음


First Trial[X]

"""



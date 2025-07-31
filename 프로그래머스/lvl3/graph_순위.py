# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    wins = [set() for _ in range(n + 1)]
    losses = [set() for _ in range(n + 1)]

    for winner, loser in results:
        wins[winner].add(loser)
        losses[loser].add(winner)
    
    for k in range(1, n + 1):
        for j in range(1, n + 1):
            for i in range (1, n + 1):
                if j in wins[k] and i in wins[j]:
                    wins[k].add(i)
                    losses[k].add(i)

    answer = 0
    for player in range(1, n + 1):
        if len(wins[player]) + len(losses[player]) == n - 1:
              answer += 1      
    
    return answer


"""
First Trial: [X]

# 유형: graph
플로이드-워셜 알고리즘
든 정점 간의 최단 경로를 구하는 알고리즘 => 도달 가능성 여부 확인 용도로 사용
"""
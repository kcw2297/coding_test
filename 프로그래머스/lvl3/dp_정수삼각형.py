# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/43105


from collections import defaultdict

def solution(triangle):
    # dp key로 (lvl, idx): val저장하여 참조
    dp = defaultdict(int)
    result = 0
    cur_lvl = 0

    for triangle_level in triangle: 
        for node_idx in range(len(triangle_level)):
            node_value = triangle_level[node_idx]

            if cur_lvl == 0:
                result = node_value
                dp[(cur_lvl, 0)] = node_value
                continue
            
            if node_idx == 0:
                parent_value = dp[(cur_lvl - 1, node_idx)]
                dp[(cur_lvl, node_idx)] = parent_value + node_value
                if parent_value + node_value > result:
                    result = parent_value + node_value
            elif node_idx == len(triangle_level) - 1:
                parent_value = dp[(cur_lvl - 1, node_idx - 1)]
                dp[(cur_lvl, node_idx)] = parent_value + node_value
                if parent_value + node_value > result:
                    result = parent_value + node_value
            else:
                parent_value1 = dp[(cur_lvl - 1, node_idx)]
                parent_value2 = dp[(cur_lvl - 1, node_idx - 1)]

                if parent_value1 > parent_value2:
                    dp[(cur_lvl, node_idx)] = parent_value1 + node_value
                    if parent_value1 + node_value > result:
                        result = parent_value1 + node_value
                else:
                    dp[(cur_lvl, node_idx)] = parent_value2 + node_value
                    if parent_value2 + node_value > result:
                        result = parent_value2 + node_value

        cur_lvl += 1

            
    return result



"""
시간 복잡도: O(N)
DP => 트리 Root 노드부터 순차적 순회
    => 상위 노드의 value 값을 dp 저장, 이후 child node에서 parent node value 참조

First Trial[X]
"""


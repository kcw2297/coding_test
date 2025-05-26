# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/43105


from collections import defaultdict

def solution(triangle):
    # TODO: dp key로 (lvl, idx): val저장
    dp = defaultdict(int)
    result = 0
    cur_lvl = 0

    for triangle_level in triangle: 
        for node_idx in range(len(triangle_level)):
            node_value = triangle_level[node_idx]

            # TODO: 현재 루트 레벨은 별도 처리
            if cur_lvl == 0:
                result = node_value
                dp[(cur_lvl, 0)] = node_value
                continue
            
            # TODO: 끝 좌, 끝 우 인 경우, 한개의 상위 노드 참조
            # TODO: 끝 좌 => 인덱스 0
            if node_idx == 0:
                parent_value = dp[(cur_lvl - 1, node_idx)]
                dp[(cur_lvl, node_idx)] = parent_value + node_value
                if parent_value + node_value > result:
                    result = parent_value + node_value
            # TODO: 끝 우 => 자기 인덱스 - 1
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






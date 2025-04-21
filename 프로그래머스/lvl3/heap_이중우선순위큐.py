# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/42628


import heapq


def solution(operations):
    max_heap = []
    min_heap = []


    for operation in operations:
        operation: str
        alpha, raw_data = operation.split(' ')
        data = int(raw_data)

        if alpha == 'I':
            heapq.heappush(max_heap, [-data, data])
            heapq.heappush(min_heap, data)
        else:
            if not max_heap:
                continue

            if data == 1:
                heapq.heappop(max_heap)
                min_heap = [ele[1] for ele in max_heap]
                heapq.heapify(min_heap)
            else:
                heapq.heappop(min_heap)
                max_heap = [[-ele, ele] for ele in min_heap]
                heapq.heapify(max_heap)

    
    if not max_heap:
        return [0, 0]
    
    max_data = heapq.heappop(max_heap)[1]
    min_data = heapq.heappop(min_heap)

    return [max_data, min_data]
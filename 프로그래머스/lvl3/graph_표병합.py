# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/150366


def solution(commands: list):
    N = 50
    size = N * N

    parent = list(range(size)) # parent[i]: i번 셀의 상위(대표) 노드 인덱스
    members = {i: {i} for i in range(size)} # r번 대표 노드가 관할하는 모든 셀 인덱스 집합
    value_map = {} # r번 대표 노드가 관리하는 병합된 셀의 값

    def find(x):
        """
            Disjoint Set Union의 find은 "원소 X"가 어떤 집합에 속하는지 알려주는 대표 원소 반환
        """
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        """
            원소 x가 속한 집합과 원소 y가 속한 집합을 하나로 합칩
        """
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        
        # rb 소속 멤버들을 전부 ra로 합친다
        for m in members[rb]:
            parent[m] = ra
            members[ra].add(m)
        members.pop(rb)
        va, vb = value_map.get(ra), value_map.get(rb)
        if va is None and vb is not None:
            value_map[ra] = vb
        value_map.pop(rb, None)

    def idx(r, c):
        return (r - 1) * N + (c - 1)

    result = []

    for cmd in commands:
        cmd: str
        parts = cmd.split()
        op = parts[0]

        if op == "UPDATE" and len(parts) == 4:
            r, c = map(int, parts[1:3])
            v = parts[3]
            i = idx(r, c)
            ri = find(i)
            value_map[ri] = v

        elif op == "UPDATE" and len(parts) == 3:
            v1, v2 = parts[1], parts[2]
            for root, val in list(value_map.items()):
                if val == v1:
                    value_map[root] = v2

        elif op == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            i1, i2 = idx(r1, c1), idx(r2, c2)
            union(i1, i2)

        elif op == "UNMERGE":
            r0, c0 = map(int, parts[1:])
            i0 = idx(r0, c0)
            root0 = find(i0)
            old_val = value_map.get(root0)

            # 병합된 셀 이전 상태로 초기화
            group = members[root0].copy()
            members.pop(root0)
            
            for m in group:
                parent[m] = m
                members[m] = {m}

            value_map.pop(root0, None)
            # 5) 선택 셀만 old_val 유지
            if old_val is not None:
                value_map[i0] = old_val

        else:  
            r, c = map(int, parts[1:])
            i = idx(r, c); ri = find(i)
            result.append(value_map.get(ri, "EMPTY"))

    return result


"""
First Trial [X]

DSU(Disjoin Set Union), Union-Find 자료구조로 서로소(partition) 집합들을 관리하면서 “같은 집합인지”를 판단하거나, 필요할 때 두 집합을 합치는 작업을 효율적으로 처리
"""


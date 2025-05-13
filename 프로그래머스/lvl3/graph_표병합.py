# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/150366


def solution(commands):
    N = 50
    size = N * N

    # DSU 초기화
    parent = list(range(size))
    members = {i: {i} for i in range(size)}
    value_map = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        # rb를 ra에 합치기
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
        parts = cmd.split()
        op = parts[0]

        if op == "UPDATE" and len(parts) == 4:
            r, c = map(int, parts[1:3]); v = parts[3]
            i = idx(r, c); ri = find(i)
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

            # 1) 그룹 멤버 목록 복사
            group = members[root0].copy()
            # 2) 기존 루트 키 제거
            members.pop(root0)
            # 3) 각 멤버를 개별 루트로 복원
            for m in group:
                parent[m] = m
                members[m] = {m}
            # 4) 값 맵에서 옛 루트 삭제
            value_map.pop(root0, None)
            # 5) 선택 셀만 old_val 유지
            if old_val is not None:
                value_map[i0] = old_val

        else:  # PRINT
            r, c = map(int, parts[1:])
            i = idx(r, c); ri = find(i)
            result.append(value_map.get(ri, "EMPTY"))

    return result



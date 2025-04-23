# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/340210



def solution(expressions):
    digits = set()
    known = []
    unknown = []

    for expr in expressions:
        expr: str

        A_str, op, B_str, _, C_str = expr.split()
        for s in (A_str, B_str):
            for ch in s:
                if ch.isdigit():
                    digits.add(int(ch))

        if C_str != 'X':
            for ch in C_str:
                if ch.isdigit():
                    digits.add(int(ch))
            known.append((A_str, op, B_str, C_str))
        else:
            unknown.append((A_str, op, B_str))

    min_base = max(max(digits) + 1, 2)

    candidates = list(range(min_base), 10)

    def to_dec(s, base):
        return int(s, base)
    
    def to_base(n, base):
        if n == 0:
            return "0"
        
        digits = []
        while n > 0:
            digits.append(str(n % base))
            n //= base

        return "".join(reversed(digits))

    def holds(triple, base):
        A_str, op, B_str, C_str = triple
        A = to_dec(A_str, base)
        B = to_dec(B_str, base)
        C = to_dec(C_str, base)
        return (A + B == C) if op == "+" else (A - B == C)


    candidates = [
        b for b in candidates
        if all(holds(expr, b) for expr in known)
    ]

    result = []
    for A_str, op, B_str in unknown:
        outs = set()
        for b in candidates:
            A = to_dec(A_str, b)
            B = to_dec(B_str, b)
            val = A + B if op == "+" else A - B
            outs.add(to_base(val, b))

        fill = outs.pop() if len(outs) == 1 else "?"
        result.append(f"{A_str} {op} {B_str} = {fill}")

    return result


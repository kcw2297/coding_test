# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import product


def solution(user_id, banned_id):
    # TODO:  bans => 각 ban별로 매칭 되는 user 할당    
    mapping_bans = []
    for ban in banned_id:
        cur_ban_mapping = []
        for user in user_id:
            match = True
            # TODO: 글자 수 동일 여부 확인
            if len(user) != len(ban):
                continue

            for idx in range(len(ban)): # FIX: all(p=='*' or p==c for p, c in zip(ban, user)):
                # TODO: 순차적으로 *인 경우 패쓰, 그외 문자 동일 여부 확인
                if ban[idx] == '*':
                    continue

                if ban[idx] != user[idx]:
                    match = False

            if match:
                cur_ban_mapping.append(user)

        mapping_bans.append(cur_ban_mapping)
            


    all_cases = set()

    for comb in product(*mapping_bans):
        # 유저 중복 여부 확인
        if len(set(comb)) == len(comb):
            # 순서를 무시하고 동일 조합으로 처리하기 위해 frozenset 사용
            all_cases.add(frozenset(comb))

    return len(all_cases)
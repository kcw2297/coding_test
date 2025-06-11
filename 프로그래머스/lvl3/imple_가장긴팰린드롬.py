# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/12904


def solution(s):
    # TODO: 문자열 전체 기준 => 홀수/짝수 동일 여부 확인
    def check_palindrome(string):
        is_even = len(string) % 2

        if not is_even:
            before_half = string[:len(string)//2]
            after_half = string[:len(string)//2-1:-1]
            return before_half == after_half
        else:
            before_half = string[:len(string)//2]
            after_half = string[:len(string)//2:-1]
            return before_half == after_half



    # TODO: 조합을 순회하며 palindrome 확인 
    for idx in range(len(s), -1, -1):
        for n_idx in range(len(s) - idx + 1):
            cur_comb = s[n_idx:(len(s)-(len(s)-idx)+n_idx)]
            is_palindrome = check_palindrome(cur_comb)
            if is_palindrome:
                return len(cur_comb)


    return 0

"""
First Trial[O]
"""


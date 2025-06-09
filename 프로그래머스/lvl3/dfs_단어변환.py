# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3



def solution(begin, target, words):
    result = 0
    
    def check(word1, word2):
        single = 0
        for idx in range(len(word1)):
            if word1[idx] != word2[idx]:
                single += 1

        if single != 1:
            return False
        else:
            return True


    def dfs(cur_word, loop, available):
        nonlocal result

        if not available:
            return
        
        
        if cur_word == target:
            if not result:
                result = loop
            else:
                result = min(result, loop)
            return

        for idx in range(len(available)):
            word = available[idx]
            match = check(cur_word, word)
            if match:
                dfs(word, loop + 1, available[:idx] + available[idx+1:])
            

    dfs(begin, 0, words)


    return result

"""
First Trial [O]
"""
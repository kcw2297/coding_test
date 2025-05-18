# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/42579


from collections import defaultdict

def solution(genres, plays):
    generes_total = defaultdict(int)
    generes_track = defaultdict(list)

    for idx in range(len(genres)):
        generes_total[genres[idx]] += plays[idx]
        generes_track[genres[idx]].append((plays[idx], idx))
    

    genere_rank = []
    
    for(key, value) in generes_total.items():
        genere_rank.append((value, key))


    genere_rank.sort(key=lambda key: -key[0])    

    total_two = 2

    result = []
    
    for rank in genere_rank:
        cur_key = rank[1]

        cur_genre = generes_track[cur_key]

        cur_genre.sort(key=lambda key: -key[0])

        if len(cur_genre) == 1:
            result.append(cur_genre[0][1])
        else:
            if cur_genre[0][1] == cur_genre[1][1]:
                result.append(cur_genre[1][1])
                result.append(cur_genre[0][1])
            else:
                result.append(cur_genre[0][1])
                result.append(cur_genre[1][1])


        total_two -= 1


    return result




"""
First Trial [O]

"""



# 링크 => https://school.programmers.co.kr/learn/courses/30/lessons/17678



from collections import deque

def solution(n, t, m, timetable):
    crew_times = sorted(
        int(h) * 60 + int(minute)
        for time in timetable
        for h, minute in [time.split(':')]
    )

    shuttle_times = [540 + i * t for i in range(n)]

    crew = deque(crew_times)
    
    last_possible = 0
    for depart in shuttle_times:
        boarded = []
        while crew and crew[0] <= depart and len(boarded) < m:
            boarded.append(crew.popleft())
   
        if len(boarded) < m:
            last_possible = depart
        else:
            last_possible = boarded[-1] - 1

   
    hh = last_possible // 60
    mm = last_possible % 60
    return f"{hh:02d}:{mm:02d}"



"""
First Trial [X]

"""
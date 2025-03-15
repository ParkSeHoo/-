
# N = N*N -> 운전판
# M == 태워야하는 목표 승객수
# fuel = 초기연료

N, M, fuel = map(int, input().split())

taxi_map =[]
for _ in range(N):
    taxi_map.append(list(map(int,input().split())))

startx, starty = map(int,input().split())


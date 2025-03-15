
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하좌우 이동

def checktomatoexception(field):
    """ 익지 못하는 토마토가 있는지 확인 """
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 0:  # 익지 않은 토마토 찾기
                blocked = True
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and field[nx][ny] != -1:
                        blocked = False
                        break
                if blocked:  # 0이 완전히 -1로 둘러싸여 있으면 익힐 수 없음
                    return False
    return True

def spread_tomatoes(field):
    """ 토마토 익히기 (BFS 없이 최적화) """
    day = 0
    ripe_tomatoes = [(i, j) for i in range(len(field)) for j in range(len(field[0])) if field[i][j] == 1]  # 초기 익은 토마토 위치 저장

    while True:
        new_ripe = []  # 새롭게 익는 토마토 저장 리스트
        for x, y in ripe_tomatoes:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and field[nx][ny] == 0:
                    field[nx][ny] = 1  # 바로 익히기
                    new_ripe.append((nx, ny))  # 다음 날 익을 토마토 저장

        if not new_ripe:  # 더 이상 확산할 토마토가 없으면 종료
            break

        ripe_tomatoes = new_ripe  # 새로운 익은 토마토 리스트 업데이트
        day += 1  # 하루 증가

    return day if all(0 not in row for row in field) else -1


row, col = map(int, input().split())  # 가로, 세로 크기
field = [list(map(int, input().split())) for _ in range(col)]  # 밭 정보

    # 예외 처리: 익지 못하는 토마토가 있으면 -1 출력
if not checktomatoexception(field):
    print("-1")
else:
    print(spread_tomatoes(field))

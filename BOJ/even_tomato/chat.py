import sys

sys.stdin = open("input.txt")

T = 5  # 테스트 케이스 개수
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하좌우 이동


def checktomatoexception(field):
    """ 예외 처리: 익지 못하는 토마토가 있는지 확인 """
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
    """ 토마토 익히기 진행 """
    day = 0
    while True:
        changed = False  # 익은 토마토가 있는지 확인
        new_field = [row[:] for row in field]  # 복사본 생성

        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == 1:  # 익은 토마토라면
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and field[nx][ny] == 0:
                            new_field[nx][ny] = 1  # 새롭게 익히기
                            changed = True

        if not changed:  # 더 이상 익힐 토마토가 없다면 종료
            break

        field[:] = new_field  # 원본 업데이트
        day += 1  # 하루 증가

    return day if all(0 not in row for row in field) else -1


for tc in range(1, T + 1):
    row, col = map(int, input().split())  # 가로, 세로 크기
    field = [list(map(int, input().split())) for _ in range(col)]  # 밭 정보

    # 예외 처리: 익지 못하는 토마토가 있으면 -1 출력
    if not checktomatoexception(field):
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {spread_tomatoes(field)}")

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    
    # 2개씩 묶어서 리스트 만들기
    paired_list = [list(pair) for pair in zip(temp[::2], temp[1::2])]
    
    final_list = []  # 정렬된 결과 리스트
    start_list = []  # 현재 탐색 중인 시작점 리스트
    
    # 시작점을 찾기
    start_dict = {start: end for start, end in paired_list}  # 딕셔너리 변환 (더 빠름)
    end_set = {end for _, end in paired_list}  # 모든 끝점 저장
    
    start = None
    for s in start_dict:
        if s not in end_set:  # 어떤 끝점에서도 시작되지 않는 값이 시작점
            start = s
            break
    
    # 첫 번째 요소 추가
    final_list.append([start, start_dict[start]])
    del start_dict[start]  # 사용한 요소 삭제
    
    # 순서대로 연결된 쌍을 찾기
    while start_dict:
        for s in list(start_dict.keys()):  # 동적으로 변경 가능하도록 리스트 변환
            if final_list[-1][1] == s:  # 마지막 끝점과 일치하는 시작점을 찾음
                final_list.append([s, start_dict[s]])
                del start_dict[s]  # 사용한 요소 삭제
                break

    # 리스트 평탄화 후 공백으로 구분된 문자열로 변환
    flattened = ' '.join(map(str, sum(final_list, [])))
    
    print(f'#{tc} {flattened}')

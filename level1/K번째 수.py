def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j] # 슬라이싱[start:end], 인덱스 start부터 end이전까지 가져옴
        slice.sort()
        answer.append(slice[k-1])
    return answer
# 구매한 번호 lottos
# 당첨 번호 win_nums
def solution(lottos, win_nums):
    answer = []
    count = 0 # 맞은 갯수
    best_count = 0 # 알아볼 수 없는 번호(0) 포함 맞은 갯수
    worst_count = 0 # 알아볼 수 없는 번호(0) 제외 맞은 갯수
    # 0이 다 맞으면 최고등수, 다 안맞으면 최저등수
    # 배열의 원소 비교
    
    for i in range(6): # 총 6개의 번호 비교
        if lottos[i] == 0:
            best_count += 1 # 알아볼 수 없는 번호가 맞는다면
        for j in range(6):
            if lottos[i] == win_nums[j]:
                count += 1
                
    best_count += count
    worst_count = count
    
    if best_count == 6:
        answer.append(1)
    elif best_count == 5:
        answer.append(2)
    elif best_count == 4:
        answer.append(3)
    elif best_count == 3:
        answer.append(4)
    elif best_count == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    if worst_count == 6:
        answer.append(1)
    elif worst_count == 5:
        answer.append(2)
    elif worst_count == 4:
        answer.append(3)
    elif worst_count == 3:
        answer.append(4)
    elif worst_count == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    return answer

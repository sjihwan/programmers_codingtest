def solution(answers):
    who_king = []
    # 맞은 문제 수(점수)
    noMath1 = 0
    noMath2 = 0
    noMath3 = 0

    # 수포자 3명의 찍는 패턴
    noMath1_arr = [1, 2, 3, 4, 5]
    noMath2_arr = [2, 1, 2, 3, 2, 4, 2, 5]
    noMath3_arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 채점: 정답과 수포자들의 답안지 비교
    for i in range(len(answers)):
        if answers[i] == noMath1_arr[i % 5]:
            noMath1 += 1

        if answers[i] == noMath2_arr[i % 8]:
            noMath2 += 1

        if answers[i] == noMath3_arr[i % 10]:
            noMath3 += 1

    # 수포자들의 점수를 비교
    best_score = max(noMath1, noMath2, noMath3)

    if best_score == noMath1:
        who_king.append(1)
    if best_score == noMath2:
        who_king.append(2)
    if best_score == noMath3:
        who_king.append(3)

    return who_king
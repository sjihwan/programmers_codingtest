# 초기 랜덤으로 주어진 인형들이 있는 2차원 배열 board
# 크레인이 움직인 위치 moves
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stacklist.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)  # 맨위꺼 삭제*2
                        stacklist.pop(-1)
                        answer += 2  # 터진 인형 갯수 추가
                break
    return answer
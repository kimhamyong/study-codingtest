# 카드는 총 c장이며, 각 카드에는 1부터 카드 개수가지 있음
# 처음에는 1이 제일 위에 있고, 순서대로 카드의 개수가지 쌓여있다. 즉 카드의 개수를 의미하는 숫자가 젤 아래에
# 1~C 중에서 1~n / (n+1)~(C-n) / (C-n+1)~C 근데 여기서 n이 처음 N이랑 나중 N이랑 다르다 n을 여러번 입력 받을 수 있음
# (n+1)~(C-n) 이 사이의 값은 순서를 유지해서 -> 걍 그대로 들고 위에 쌓는다.
# (n+1)~(C-n) > 2*n dlf 경우에 (n+1)~(C-n)을 가지고 카드 섞기 한다.
# (n+1)~(C-n) <= 2*n 이면 카드 섞기 1회 완료!


c = int(input())  # 총 카드 장 수, 전부 엔터로 입력 받는다
p = int(input())  # 연산 횟수
n = [int(input()) for n in range(p)]  # 각 연산의 n 값 리스트

card = [i for i in range(1, c + 1)]

def shuffle(cards, n):
    left = cards[:n]  # 1 ~ n
    middle = cards[n:len(cards) - n]  # (n+1) ~ (C-n)
    right = cards[len(cards) - n:]  # (C-n+1) ~ C

    if len(middle) > 2 * n:
        middle = shuffle(middle, n)

    return middle + left + right

for j in n:
    card = shuffle(card, j)

print(' '.join(map(str, card)))


# 초기 상태: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# left: [1, 2]
# middle: [3, 4, 5, 6, 7, 8]
# right: [9, 10]
# [3, 4, 5, 6, 7, 8, 1, 2 9, 10]
# 여기서 
# middle 길이(6) > 2 * n(4): [3, 4, 5, 6, 7, 8]
# left: [3,4]
# middle: [5,6]
# right: [7,8]
# [5, 6, 3, 4, 7, 8]

# 1회 카드 섞기 완료(n =2)
# [5, 6, 3, 4, 7, 8, 1, 2, 9, 10]

# 두 번째 연산 (n=3):
# left: [5, 6, 3]
# middle: [4, 7, 8, 1]
# right: [2, 9, 10]

# [4,7,8,1,5,6,3,2,9,10]
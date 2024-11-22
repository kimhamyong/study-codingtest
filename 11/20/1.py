# 게임으로 습득할 수 있는 아이템은 6개
# 주인공은 아이템 총 3개 가질 수 있음
# 주인공은 일단 아이템 다 줍는다. -> 큐로 동작
# 이미 있는 아이템을 중복으로 주웠으면 순서만 바뀐다. -> 버린건 아니다.


input = input().split()  # 입력받은 아이템 리스트
item = []  # 주인공의 아이템 주머니 (최대 3개)
answer = []  # 버려진 아이템 리스트

for i in input:
    if len(item)<3:
        item.insert(0, i)
    elif len(item) == 3:
        if i in item:
            item.remove(i)
        else:
            answer.append(item.pop(2))

# 버려진 아이템 출력
print(' '.join(answer))

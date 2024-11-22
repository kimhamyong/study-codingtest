# 100장에서 카드 꺼내기 (1 제외)
# 준비한 카드 == 작은 상자 개수
# 상자 무작위로 섞고 나열하기 -> 안에 무작위 숫자가 들어있는 상자에 번호 부여
# 그 다음 상자를 선택해서 숫자 확인하기 -> 그 숫자에 해당하는 상자 열기

# 상자 안에 들어있는 카드 번호를 배열로 제공, 여기서는 +1 해서 생각하면 됨
# opened[] 만들어서 상자 열었는지 확인하기

# 반복문 안에서 answer 최대값 비교하기


def solution(cards):

    opened = []
    opened = [0 for i in range(len(cards))]

    group = [0]
    answer = 0

    for k in range(len(cards)):
        if 0 not in opened:
            break
        q = 0
        group.insert(q, 0)
        opened[k] =1
        group[q] +=1
        i = cards[k]-1
    
        while opened[i]==0:
            opened[i]=1
            group[q]+=1
            i = cards[i]-1
            
            if opened[i]==1 and 0 in opened:
                q +=1
                group.insert(q, 0)
                i = opened.index(0)
            
            elif 0 not in opened:
                break
            
        group.sort(reverse=True)
        
        if answer <= group[0]*group[1]:
            answer = group[0]*group[1]
            
    return answer
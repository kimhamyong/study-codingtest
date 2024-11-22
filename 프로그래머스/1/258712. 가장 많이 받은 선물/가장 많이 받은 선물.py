#선물을 가장 많이 받을 친구가 받을 선물의 개수 구하기

#선물 지수 = 이번 달 까지 내가 선물 한 수 - 받은 선물 수
#선물 지수가 커야 선물을 받는다.. -> 내가 선물을 더 많이 했으면 공평하게 선물을 준다.

# friends = [] #friends - 이름을 1차원 문자열 배열에 담기, 2<= 친구의 수 <= 50
# gifts = [] #gifts - 선물 기록, A B(공백으로 구분): A가 B에게 선물 줌


#each-gift 전부 [1][2], [2][1] 비교하고 num-gift에 +1 -> 대소 관계 없을 시 point-gift 이용

#1. gifts에서 원소 하나 가져와서 each-gift(주고 받은 선물 점수) 구하기
#1-1. each-gift 구하는 방법: friends로 2차원 배열 만든 후, gifts 배열에서 리스트 전부 꺼내서 "a b"인 경우 [a][b]에 +1
#2. point-gift(선물 지수) 구하기 - 배열로 만든다 -> friends 순서대로, 즉 동일한 순서여서 동일한 friends에 매칭됨
#2-1. gift 에서 "a b"인 경우 a인 배열값 +1, b인 배열값 -1
#3. num-gift(각자 받을 선물 개수)구하기 - 모든 값 비교하기(for문 사용)
#3-1. 1번 수행 후, point-gift 대소 관계 후 +1
#4. num-gift이 젤 큰 friend 반환: 내림 차순 정렬 후 맨 앞의 원소 반환

def solution(friends, gifts):
    
    eachgift = [[0 for j in friends] for i in friends] #friends로 주고 받은 선물 점수 2차원 배열로 구현
    #for i in friends:
    #   row = []
    #   for j in frineds:
    #      row.append(0) 이랑 같음
    
    pointgift = [0 for i in range(len(friends))] #선물 지수 1차원 배열로 구현, 일단 0 넣기
    numgift = [0 for i in range(len(friends))] #선물 몇 개나 받을지 넣어놀 값 배열로 구현

    for i in gifts:
        a = i #누가 누구에게 선물 줌
    
        found_f = friends.index(a.split()[0]) #프렌즈 배열에서 스플릿된 a와 순서 매칭하기
        found_b = friends.index(a.split()[1])
        
        eachgift[found_f][found_b] +=1 #매칭된 순서의 배열에 +1하기
        
        pointgift[found_f] +=1 #선물 준 사람 선물 지수 +1
        pointgift[found_b] -=1 #선물 받은 사람 선물 지수 -1
        
    for i in range(len(friends)):
        for j in range(len(friends)):
            if eachgift[i][j] > eachgift[j][i]:
                numgift[i] +=1
            elif eachgift[i][j] == eachgift[j][i]:
                if pointgift[i] > pointgift[j]:
                    numgift[i] +=1
                    
    numgift.sort(reverse=True)
    
    answer = numgift[0]
    return answer
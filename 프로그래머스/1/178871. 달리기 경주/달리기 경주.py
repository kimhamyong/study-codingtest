def solution(players, callings):

    dic_players={players[index]:index for index in range(len(players))}

    for i in range(len(callings)):
        j = dic_players[callings[i]]
        dic_players[callings[i]]=j-1
        dic_players[players[j-1]]=j
        players[j-1], players[j] = players[j], players[j-1]


    return players
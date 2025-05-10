
def climbingLeaderboard(ranked, player):
 
    unique_ranks = sorted(set(ranked), reverse=True)
    result = []
    n = len(unique_ranks)
    i = n - 1  

   
    for score in player:
     
        while i >= 0 and score >= unique_ranks[i]:
            i -= 1
        result.append(i + 2)  
    return result


ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
print(climbingLeaderboard(ranked, player)) 

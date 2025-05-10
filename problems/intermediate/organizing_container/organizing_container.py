def organizingContainers(containers):
    
    n = len(containers)
    
    container_capacities = [sum(row) for row in containers]
   
    type_totals = [sum(containers[i][j] for i in range(n))
                   for j in range(n)]
    

    return "Possible" if sorted(container_capacities) == sorted(type_totals) else "Impossible"

c1 = [[1, 4],
      [2, 3]]
print(organizingContainers(c1)) 

c2 = [[0, 2, 1],
      [1, 1, 1],
      [2, 0, 0]]
print(organizingContainers(c2))  

import collections 
from collections import deque

def number_of_islands(grid):

    if not grid:
        return
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft() # **BFS uses pop from the left for queue behavior**
            # row, col = q.pop() it is for DFS

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                # print(r,'rrr')
                # print(c,'ccc')
                if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r,c)
                islands += 1

    return islands



grid=[['1','1','1','0'],
      ['1','1','0','0'],
      ['1','0','0','0'],
      ['1','0','1','1'],]

print(number_of_islands(grid))



def n_islands(grid):

    if not grid:
        return None
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft()

            dirctns = [[1,0],[0,1],[-1,0],[0,-1]]

            for dr, dc in dirctns:

                r, c = row + dr, col + dc

                if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                bfs(r,c)
                islands += 1

        
    return islands






def islands(grid):

    if not grid:
        return
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    island = 0


    def bfs(r,c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))

        while q:
            row,col = q.popleft()

            directns =  [[1,0],[0,1],[-1,0],[0,-1]]

            for dr, dc in directns:
                r,c = row + dr, col + dc

                if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                    visit.add((r,c))
                    q.append((r,c))


    for r in range(rows):
        for c in range(cols):
            if (r,c) not in visit and grid[r][c] == "1":
                bfs(r,c)
                island += 1
    
    return island


grid=[['1','1','1','0'],
      ['1','1','0','0'],
      ['1','0','0','0'],
      ['1','0','0','0'],]

print(n_islands(grid))
print(islands(grid))



























#number of islands

# 1 1 1 0
# 1 1 0 1
# 1 1 0 0
# 0 0 1 1
#output = 3, the count of islands in the grid

# we need to return the number of islands (1's grouped together), how?

# intuition
# We can check every cell in the grid if it's a 1 and it hasn't been
# visited, we can then apply a Breadth First Search starting from
# this cell to explore all of its neighbors and mark them visited.
# Since we've found an island (1) then we can also increment the 
# island count before checking the next cells in the grid.
# 
# Breadth First Search (using a queue)
# We can take the location of the island (1) cell, mark it visited, add 
# it to our queue and begin BFS. While the queue is not empty, we pop
# the first cell to get its location and then check its neighbors/adjacent
# cells. If we find a neighbor cell that is an island (1), has not been
# visited, and within the grid's boundaries, then we mark it visited
# and add it to the queue.



import collections


def islandNums(grid):
    ROWS, COLS = len(grid), len(grid[0])
    ans = 0
    dq = collections.deque()
    visited = set()

    # the neighboring nodes of starting nodes so the next layers
    def checkCells(r,c):
        if (r>=0 and c>=0 and r<ROWS and c<COLS and (r,c) not in visited
            and grid[r][c] == 1):
            visited.add((r,c))
            dq.append((r,c))

    def bfs(i,j):
        dq.append((i,j))
        visited.add((i,j))
        while dq:
            r,c = dq.popleft()
            checkCells(r+1,c)
            checkCells(r-1,c)
            checkCells(r,c+1)
            checkCells(r,c-1)


    for i in range(ROWS):
        for j in range(COLS):
            # the starting nodes
            if grid[i][j] == 1 and (i,j) not in visited:
                bfs(i,j)
                ans += 1

    return ans



grid = [
    [1,1,1,0],
    [1,1,0,1],
    [1,0,1,0],
    [0,0,1,1]
]

print(islandNums(grid))
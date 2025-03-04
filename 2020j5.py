from collections import deque

rows = int(input())
cols = int(input())

# Create a 2D list to store the grid
grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))

factors = {}

def get_possible_moves(n):
    if n in factors:
        return factors[n]
    moves = []
    max = int(n**0.5)
    for i in range(1, max+1):
        if n % i == 0:
            tup = (i, n//i)
            tup2 = (n//i, i)
            if tup[0] <= rows and tup[1] <= cols:
                moves.append(tup)
            if tup2[0] <= rows and tup2[1] <= cols:
                moves.append(tup2)
    factors[n] = moves
    return moves
    
def bfs(grid):
    q = deque()
    q.append((1, 1))
    visited = set()
    while q:
        current = q.popleft()
        for move in get_possible_moves(grid[current[0]-1][current[1]-1]):
            if move == (rows, cols):
                print('yes')
                return
            if move not in visited:
                q.append(move)
                visited.add(move)
    print('no')

bfs(grid)

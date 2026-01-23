dx = [0, -1]
dy = [-1, 0]
n = 3
for i in range(n):
    m = [[0] * n for _ in range(n)]
r = 0
c = 0
start, stop = 2, 2
m[r][c] = 1
rows, cols = len(m), len(m[0])
def inMatrix(i , j):
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return False
    return True

def traverse_paths(r, c):
    for row in range(r, rows):
        for col in range(c, cols):
            past_r_one = dx[0] + row
            past_c_one = dy[0] + col
            if inMatrix(past_r_one, past_c_one):
                m[row][col] += m[past_r_one][past_c_one]    
            past_r_two = dx[1] + row
            past_c_two = dy[1] + col
            if inMatrix(past_r_two, past_c_two):
                m[row][col] += m[past_r_two][past_c_two]
            if row == start and col == stop:
                return m[row][col]
print(traverse_paths(r, c))


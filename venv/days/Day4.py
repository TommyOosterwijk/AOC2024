input = """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
"""

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

array_2d = [list(line) for line in input.strip().split("\n")]
rows = len(array_2d)
cols = len(array_2d[0])

def do_recursive_search(x, y, target, dir):
    if target == "":
        return 1

    targetLetter = target[0:1]

    nx, ny = x + directions[dir][1], y + directions[dir][0]
    if 0 <= ny < rows and 0 <= nx < cols:
        if array_2d[ny][nx] == targetLetter:
            return do_recursive_search(nx, ny, target[1:], dir)
    return 0

anwserA = 0
answerB = 0
for y in range(len(array_2d)):        # Loop over rows (x)
    for x in range(len(array_2d[0])):
        if (array_2d[y][x] == "X"):
            for i in range(len(directions)):
                anwserA += do_recursive_search(x,y, "MAS", i)
        elif (array_2d[y][x] == "A" and y > 0 and y < len(array_2d)-1 and x > 0 and x < len(array_2d[0])-1):
            if (array_2d[y-1][x-1] == "M" and array_2d[y+1][x+1] == "S") or (array_2d[y-1][x-1] == "S" and array_2d[y+1][x+1] == "M"):
                if (array_2d[y-1][x+1] == "M" and array_2d[y+1][x-1] == "S") or (array_2d[y-1][x+1] == "S" and array_2d[y+1][x-1] == "M"):
                    answerB+= 1

print(anwserA)
print(answerB)

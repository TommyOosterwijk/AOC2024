import copy

input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

directions = [ (-1, 0), (0, -1),
              (1, 0), (0, 1)]

array_2d = [list(line) for line in input.strip().split("\n")]
rows = len(array_2d)
cols = len(array_2d[0])

def go_hiking(y, x, targetValue, map):
    counter = 0
    if array_2d[y][x] == "9" and str(targetValue) == "9":
        map[y][x] = "T"
        return 1
    elif array_2d[y][x] == str(targetValue):
        for i in range(len(directions)):
            newY = y + directions[i][0]
            newX = x + directions[i][1]
            if 0 <= newY < rows and 0 <= newX < cols:
                counter += go_hiking(newY, newX, targetValue + 1, map)
    return counter

answerA = 0
answerB = 0
for y in range( rows):
    for x in range( cols):
        if array_2d[y][x] == "0":
            map = copy.deepcopy(array_2d)
            answerB += go_hiking(y,x,0, map)
            answerA+= sum(row.count("T") for row in map)
print("AnswerA: ", answerA)
print("AnswerB: ", answerB)

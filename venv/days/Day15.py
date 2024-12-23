input = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######
"""

moves = """<vv<<^^<<^^^"""

directions = [ (-1, 0), (0, 1), (1, 0), (0, -1)]
def do_move(pos, direction, object):
    targetY = pos[0] + directions[int(direction)][0]
    targetX = pos[1] + directions[int(direction)][1]

    if not 0 <= targetY < rows and 0 <= targetX < cols:
        return pos
    if array[targetY][targetX] == "O":
        do_move((targetY, targetX), direction, "O")

    if array[targetY][targetX] == ".":
        array[targetY][targetX] = object
        array[pos[0]][pos[1]] = "."
        if object == "@":
            return (targetY, targetX)
    return pos
rows = input.strip().splitlines()
array = [list(row) for row in rows]

arrayB = []
for row in rows:
    string = ""
    for str in row:
        if str == "#":
            string+= "##"
        if str == "O":
            string+= "[]"
        if str == ".":
            string+= ".."
        if str == "@":
            string+= "@."
    arrayB.append(list(string))

rows = len(array)
cols = len(array[0])
robotLocation = (0,0)
for y in range(cols):
    for x in range(rows):
        if array[y][x] == "@":
            robotLocation = (y,x)

moves = moves.replace("^", "0")
moves = moves.replace(">", "1")
moves = moves.replace("v", "2")
moves = moves.replace("<", "3")
moves = moves.replace("\n", "")

for direction in list(moves):
    robotLocation = do_move(robotLocation, direction, "@")
answerA = 0
for y in range(cols):
    for x in range(rows):
        if array[y][x] == "O":
            answerA+= (100 * y) + x

print("AnswerA ", answerA)

def do_move_B(pos, direction, object):
    targetY = pos[0] + directions[direction][0]
    targetX = pos[1] + directions[direction][1]

    if not 0 <= targetY < rows and 0 <= targetX < cols:
        return pos
    if direction == 3:
        if arrayB[targetY][targetX] == "]":
            do_move_B((targetY, targetX-1), direction, "O")

        if arrayB[targetY][targetX] == ".":
            if object == "O":
                arrayB[targetY][targetX] = "["
                arrayB[targetY][targetX+1] = "]"
                arrayB[targetY][targetX+2] = "."
            else:
                arrayB[targetY][targetX] = "@"
                arrayB[targetY][targetX+1] = "."
                return (targetY,targetX)

    return pos
rowsB = len(arrayB[0])
colsB = len(arrayB)
robotBLocation = (0,0)

for y in range(len(arrayB)):
    for x in range(len(arrayB[0])):
        if arrayB[y][x] == "@":
            robotBLocation = (y,x)

for direction in list(moves):
    robotBLocation = do_move_B(robotBLocation, int(direction), "@")

"""for y in range(len(arrayB)):
    for x in range(len(arrayB[0])):
        print(arrayB[y][x], end='')
    print()"""

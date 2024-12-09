import copy

input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

array_2d = [list(line) for line in input.strip().split("\n")]
output = array_2d.copy()
rows = len(array_2d)
cols = len(array_2d[0])

antennas = {}

def create_antinodes(baseAntenna, targetAntenna, yRange, xRange, keepGoing):
    targetY = 0
    targetX = 0
    counter = 1
    while True:
        if baseAntenna[0] < targetAntenna[0]:
            targetY = baseAntenna[0] - (yRange * counter)
        elif baseAntenna[0] >= targetAntenna[0]:
            targetY = baseAntenna[0] + (yRange * counter)

        if baseAntenna[1] < targetAntenna[1]:
            targetX = baseAntenna[1] - (xRange * counter)
        elif baseAntenna[1] >= targetAntenna[1]:
            targetX = baseAntenna[1] + (xRange * counter)

        if 0 <= targetY < rows and 0 <= targetX < cols:
            if keepGoing:
                output[targetY][targetX] = "}"
            else:
                output[targetY][targetX] = "#"
        else:
            break

        if not keepGoing:
            break
        counter+=1

for y in range(rows):
    for x in range(cols):
        if array_2d[y][x] != ".":
            antennaValue = array_2d[y][x]
            if antennaValue not in antennas:
                antennas[antennaValue] = [ (y,x)]
            else:
                antennas[antennaValue].append((y,x))

antennasB = copy.deepcopy(antennas)

for key, value in antennas.items():
    while len(value) > 0:
        firstAntenna = value.pop(0)
        for targetAntenna in value:
            yRange = abs(firstAntenna[0] - targetAntenna[0])
            xRange = abs(firstAntenna[1] - targetAntenna[1])
            create_antinodes(firstAntenna, targetAntenna, yRange, xRange, False)
            create_antinodes(targetAntenna, firstAntenna, yRange, xRange, False)

answerA = 0
for y in range(rows):
    for x in range(cols):
        if output[y][x] == "#":
            answerA+=1

print("AnswerA: " , answerA)

for key, value in antennasB.items():
    add = False
    if len(value) > 1:
        add = True
    while len(value) > 0:
        firstAntenna = value.pop(0)
        if add:
            output[firstAntenna[0]][firstAntenna[1]] = "}"
        for targetAntenna in value:
            yRange = abs(firstAntenna[0] - targetAntenna[0])
            xRange = abs(firstAntenna[1] - targetAntenna[1])
            create_antinodes(firstAntenna, targetAntenna, yRange, xRange, True)
            create_antinodes(targetAntenna, firstAntenna, yRange, xRange, True)
answerB = 0
for y in range(rows):
    for x in range(cols):
        if output[y][x] == "}":
            answerB+=1

print("AnswerB: " , answerB)

import copy
import threading


input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

array_2d = [list(line) for line in input.strip().split("\n")]
output = array_2d.copy()
rows = len(array_2d)
cols = len(array_2d[0])
startingPos = ()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answerA = 0


def move_gaurd_till_finish(y, x, map):
    cache = []
    dir = 0
    while 0 <= y < rows and 0 <= x < cols:
        nx, ny = x + directions[dir][1], y + directions[dir][0]
        cacheString = f"{x}|{y}|{dir}"
        if cacheString in cache:
            return False
        else:
            cache.append(cacheString)
        if not (0 <= ny < rows and 0 <= nx < cols):
            break
        if map[ny][nx] == "#":
            dir += 1
            if dir > 3:
                dir = 0
        else:
            x, y = x + directions[dir][1], y + directions[dir][0]
            output[y][x] = "O"
    return True

for y in range(rows):
    for x in range(cols):
        if array_2d[y][x] == "^":
            startingPos = (y, x)
            output[y][x] = "O"

move_gaurd_till_finish(startingPos[0], startingPos[1], array_2d)

for y in range(rows):
    for x in range(cols):
        if output[y][x] == "O":
            answerA += 1

print("AnswerA: ", answerA)

obstrutionMap = copy.deepcopy(output)

answerB = 0
"""for y in range(rows):
    for x in range(cols):
        if obstrutionMap[y][x] == "O":

            array_2d[y][x] = "#"
            if not move_gaurd_till_finish(startingPos[0], startingPos[1], array_2d):
                answerB+=1
            array_2d[y][x] = "."
print("AnswerB: ", answerB)"""

def process_row(y, cols, obstrutionMap, array_2d, startingPos, answerB_lock):
    global answerB
    for x in range(cols):
        if obstrutionMap[y][x] == "O":
            array_2d[y][x] = "#"

            # Check move_gaurd_till_finish logic
            if not move_gaurd_till_finish(startingPos[0], startingPos[1], array_2d):
                with answerB_lock:  # Use a lock to ensure thread-safe access
                    answerB += 1

            array_2d[y][x] = "."

# Create threads to process rows concurrently
threads = []
answerB_lock = threading.Lock()

for y in range(rows):
    t = threading.Thread(target=process_row, args=(y, cols, obstrutionMap, array_2d, startingPos, answerB_lock))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Final answerB: {answerB}")

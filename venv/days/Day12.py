input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
class Region:
    def __init__(self):
        self.tiles = []
        self.fence = 0
        self.value = 0

array_2d = [list(line) for line in input.strip().split("\n")]
rows = len(array_2d)
cols = len(array_2d[0])

directions = [ (-1, 0), (0, -1),
               (1, 0), (0, 1)]

def create_map(tiles):
    min_y = min(tile[0] for tile in tiles)
    max_y = max(tile[0] for tile in tiles)
    min_x = min(tile[1] for tile in tiles)
    max_x = max(tile[1] for tile in tiles)

    height = max_y - min_y + 1
    width = max_x - min_x + 1
    grid = [["." for _ in range(width)] for _ in range(height)]

    for y, x in tiles:
        grid[y - min_y][x - min_x] = "#"

    for y in range(height):
        for x in range(width):
            print(grid[y][x], end='')
        print()
    return grid
def groupByValue(region, y, x):
    array_2d[y][x] = "."
    region.tiles.append((y,x))
    fence = 4
    for i in range(len(directions)):
        newY = y + directions[i][0]
        newX = x + directions[i][1]

        if 0 <= newY < rows and 0 <= newX < cols:
            if array_2d[newY][newX] == region.value:
                groupByValue(region, newY, newX)
                fence-=1
            elif (newY,newX) in region.tiles:
                fence-=1
    region.fence+= fence
    return region

def count_corners(grid):

    rows = len(grid)
    cols = len(grid[0])

    corners = 0
    diagonal_directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    overlap = 0
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == "#":
                neighbours = 0
                for i in range(len(directions)):
                    newY = y + directions[i][0]
                    newX = x + directions[i][1]
                    if 0 <= newY < rows and 0 <= newX < cols:
                        if grid[newY][newX] == ".":
                            neighbours+=1
                    else:
                        neighbours+=1

                if neighbours == 3:
                    corners+= 2
                elif neighbours == 2:
                    if (0 <= y-1 and grid[y - 1][x] == "#") and (y + 1 < rows and grid[y + 1][x] == "#"):
                        print("", end='')
                    elif (0 <= x-1 and grid[y][x - 1] == "#") and (x + 1 < cols and grid[y][x + 1] == "#"):
                        print("", end='')
                    else:
                        corners+=1
                elif neighbours == 4:
                    corners+= 4
            elif grid[y][x] == ".":
                neighbours = 0
                for i in range(len(directions)):
                    newY = y + directions[i][0]
                    newX = x + directions[i][1]
                    if 0 <= newY < rows and 0 <= newX < cols:
                        if grid[newY][newX] == "#":
                            neighbours+=1

                if neighbours == 3:
                    corners+= 2
                elif neighbours == 2:
                    if (0 <= y-1 and grid[y - 1][x] == "#") and (y + 1 < rows and grid[y + 1][x] == "#"):
                        print("", end='')
                    elif (0 <= x-1 and grid[y][x - 1] == "#") and (x + 1 < cols and grid[y][x + 1] == "#"):
                        print("", end='')
                    else:
                        corners+=1
                        if 0 <= y-1 < rows and 0 <= x+1 < cols and grid[y - 1][x] == "#" and grid[y][x+1] == "#" and grid[y - 1][x+1] == ".":
                            overlap+=1
                        elif 0 <= y+1 < rows and 0 <= x+1 < cols and grid[y][x+1] == "#" and grid[y+1][x] == "#" and grid[y + 1][x+1] == ".":
                            overlap+=1
                        elif 0 <= y+1 < rows and 0 <= x-1 < cols and grid[y + 1][x] == "#" and grid[y][x-1] == "#" and grid[y + 1][x-1] == ".":
                            overlap+=1
                        elif 0 <= y-1 < rows and 0 <= x-1 < cols and grid[y][x-1] == "#" and grid[y-1][x] == "#" and grid[y - 1][x-1] == ".":
                            overlap+=1

                elif neighbours == 4:
                    corners+= 4
    return corners - overlap


answerA = 0
answerB = 0
for y in range(rows):
    for x in range(cols):
        if array_2d[y][x] != ".":
            region = Region()
            region.value = array_2d[y][x]
            region = groupByValue(region, y, x)
            answerA+= len(region.tiles) * region.fence
            grid = create_map(region.tiles)
            print(len(region.tiles) , " * ", count_corners(grid) , " = ", count_corners(grid) * len(region.tiles))
            answerB += count_corners(grid) * len(region.tiles)

print("AnswerA: ", answerA)
print("AnswerB: ", answerB) #should be 1206 in example not 866648 in production

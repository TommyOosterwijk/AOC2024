data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def remove_by_positions(row, position):
    rows = list(map(int, row.split()))
    return rows[:position] + rows[position+1:]

def line_function_A(row):
    print(row)
    if not row or len(row) < 2:
        return True

    increasing = all((row[i] - row[i - 1] > 0 and row[i] - row[i - 1] <= 3) for i in range(1, len(row)))
    decreasing = all((row[i] - row[i - 1] < 0 and abs(row[i] - row[i - 1]) <= 3) for i in range(1, len(row)))

    return increasing or decreasing


counter = 0
for line in data.strip().split("\n"):
    if line_function_A(list(map(int, line.split()))):
        counter+= 1

print(f"A: {counter}")


counterB = 0
for line in data.strip().split("\n"):
    if line_function_A(list(map(int, line.split()))):
        counterB+= 1
    else:
        len2 = len(list(map(int, line.split())))
        for i in range(len2) :
            if line_function_A(remove_by_positions(line, i)):
                counterB+= 1
                break
print(f"B: {counterB}")

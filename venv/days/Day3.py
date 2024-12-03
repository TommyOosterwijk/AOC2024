line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def is_strict_integer(string):
    return string.isdigit() and not string.isspace()

makeItCount = True
resultA = 0
resultB = 0
for row in line.split(")"):
    if row[-3:] == "do(":
        makeItCount = True
    elif row[-6:] == "don't(":
        makeItCount = False
    else:
        parts = row.split(",")
        num1 = parts[len(parts)-1]
        secondPart = parts[len(parts)-2].split("(")
        num2 = secondPart[len(secondPart)-1]
        lastLine = secondPart[len(secondPart)-2]

        if lastLine[-3:] == "mul":
            if is_strict_integer(num1) & is_strict_integer(num2):
                resultA+= int(num2) * int(num1)
                if makeItCount:
                    resultB+= int(num2) * int(num1)
print("A: ", resultA)
print("B: ", resultB)

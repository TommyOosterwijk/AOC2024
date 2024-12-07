import copy

input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
def do_operation(targetValue, currentValue, numbers):
    if currentValue == targetValue:
        return True
    elif currentValue > targetValue:
        return False

    if len(numbers) == 0:
        return False

    value = numbers.pop(0)
    newNumbers = copy.deepcopy(numbers)
    newValue = 0
    if currentValue == 0:
        newValue = value
    else:
        newValue = currentValue * value

    if( do_operation(targetValue, currentValue+value, newNumbers)):
        return True
    secondNumbers = copy.deepcopy(numbers)
    if(do_operation(targetValue, newValue, secondNumbers)):
        return True

    thirdNumbers = copy.deepcopy(numbers)
    stringV = str(currentValue) + "" + str(value)
    if(do_operation(targetValue, int(stringV), thirdNumbers)):
        return True

answerA = 0
for line in input.strip().split("\n"):
    l1 = line.split(":")
    targetValue = int(l1[0])
    numbers = l1[1]

    if(do_operation(targetValue, 0, list(map(int, numbers.strip().split(" "))))):
        answerA+= targetValue

print("Answer A: ", answerA)

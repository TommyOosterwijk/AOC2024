import copy

input = """2333133121414131402"""

class File:
    def __init__(self, id, value, moved):
        self.id = id
        self.value = value
        self.moved = moved
class Container:
    def __init__(self):
        self.items = []  # List to hold Item objects

    def add_item(self, file):
        self.items.append(file)

    def insert_item(self, file, index):
        self.items.insert(index, file)

container = Container()
containerB = Container()
counter = 0
for index, letter in enumerate(input, start=1):  # start=1 to match 1-based step
    if index % 2 == 0:
        for i in range(int(letter)):
            container.add_item(File(".", 0, False))
        containerB.add_item(File(".", int(letter), False))
    else:
        for i in range(int(letter)):
            container.add_item(File(counter, 0, False))
        containerB.add_item(File(counter, int(letter), False))
        counter+=1

startIndex = 0
endIndex = len(container.items)-1
while startIndex < endIndex:
    if container.items[startIndex].id == ".":
        if not container.items[endIndex].id == ".":
            container.items[startIndex].id = container.items[endIndex].id
            container.items[endIndex].id = "."
        else:
            endIndex-=1
    else:
        startIndex+=1

answerA = 0
cnt = 0
for file in container.items:
    if file.id != ".":
        answerA+= (cnt * int(file.id))
        cnt+=1

print("AnswerA: ", answerA)

for i in containerB.items:
    print(i.id, end = '')

print()
for i in reversed(range(len(containerB.items))):
    item = containerB.items[i]
    if item.id != "." and item.moved == False:
        for i2 in range(i):
            if containerB.items[i2].id == "." and containerB.items[i2].value >= item.value:
                biggervalue = False
                value = 0
                if containerB.items[i2].value > item.value:
                    biggervalue = True
                    value = containerB.items[i2].value - item.value
                containerB.items[i2].id = item.id
                containerB.items[i2].moved = True
                containerB.items[i2].value = item.value
                containerB.items[i].id = "."

                if biggervalue:
                    containerB.insert_item(File(".", value, False), i2+1)

                break

counter = 0
answerB = 0
for i in containerB.items:
    for i2 in range (i.value):
        if i.id != ".":
            answerB+= counter * int(i.id)
        counter+=1

print("AnswerB: ", answerB)

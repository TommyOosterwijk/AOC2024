stringStones = """4189 413 82070 61 655813 7478611 0 8""".strip().split(" ")
stones = []
class Stone:
    def __init__(self, value, times):
        self.value = value
        self.times = times

for i in range(len(stringStones)):
    stones.append(Stone(str(stringStones[i]), 1))

def combine_records(array):
    combined = {}
    for item in array:
        if item.value in combined:
            combined[item.value].times += item.times
        else:
            combined[item.value] = Stone(item.value, item.times)
    return list(combined.values())

for i in range(75):
    stoneLen = len(stones)
    for i in range(stoneLen):
        stone = stones.pop(0)
        val = str(stone.value)
        if val == "0":
            stones.append(Stone("1", stone.times))
        elif len(val) % 2 == 0:
            midpoint = len(val) // 2
            stones.append(Stone(str(int(val[:midpoint])),stone.times))
            stones.append(Stone(str(int(val[midpoint:])),stone.times))
        else:
            stones.append(Stone(str(int(val) * 2024), stone.times))
    stones = combine_records(stones)
answerA = 0
for i in range(len(stones)):
    answerA += int(stones[i].times)

print(len(stones))
print("AnswerA: ", answerA)

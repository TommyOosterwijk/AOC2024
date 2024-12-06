rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

pages = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

list = {}
for line in rules.strip().split("\n"):
    result = line.split("|")
    if result[0] in list:
        list[result[0]].add(result[1])
    else:
        list[result[0]] = {result[1]}

resultA = 0
linesB=[]
for line in pages.strip().split("\n"):
    go = True
    prevOrders = []
    orders = line.strip().split(",")
    for order in orders:
        if order in list and len(prevOrders) > 0:
            if any(prevOrder in list[order] for prevOrder in prevOrders):
                go = False
        prevOrders.append(order)
    if go:
        middle_index = len(orders) // 2
        resultA += int(orders[middle_index])
    else:
        linesB.append(orders)

print("ResultA: ", resultA)

resultB = 0
for order in linesB:
    holder = []
    special = []
    while len(order) > 0:
        target = order.pop(0)
        if target not in list:
            special.append(target)
        else:
            if all(o in list and target not in list[o] for o in order):
             holder.append(target)
            elif len(order) == 0:
             holder.append(target)
            else:
                order.append(target)
    if len(special) > 0:
        holder.append(special)
    middle_index = len(holder) // 2
    resultB += int(holder[middle_index])

print("ResultB: ", resultB)

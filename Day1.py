from collections import Counter

data = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

# Initialize arrays for left and right numbers
left_numbers = []
right_numbers = []

# Process each line of the data
for line in data.strip().split("\n"):
    left, right = map(int, line.split())
    left_numbers.append(left)
    right_numbers.append(right)

# Display the arrays
print("Left Numbers:", left_numbers)
print("Right Numbers:", right_numbers)

left_numbers.sort()
right_numbers.sort()

total_distance = sum(abs(left - right) for left, right in zip(left_numbers, right_numbers))

# Display the result
print("A:", total_distance)

list2_counts = Counter(right_numbers)

result_sum = sum(value * list2_counts.get(value, 0) for value in left_numbers)

# result_sum = sum(value * right_numbers.count(value) for value in left_numbers) from Bronco

# Display the result
print("B:", result_sum)








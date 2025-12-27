numbers = [1, 0, 2, 0, 3, 4, 0, 5]

zero_count = numbers.count(0)

numbers = [num for num in numbers if num != 0]

numbers.extend([0] * zero_count)

print("Number of zeroes:", zero_count)
print("Modified list:", numbers)

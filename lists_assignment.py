# Q1. Accessing List Elements

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

print("Q1:", first, middle, last)


# Q2. List Slicing

numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

first_five = numbers[:5]
last_four = numbers[-4:]
every_second_reversed = numbers[::-2]

print("Q2:", first_five, last_four, every_second_reversed)


# Q3. List Modification

fruits = ["apple", "banana", "cherry", "mango"]

fruits[1] = "orange"
fruits.insert(2, "grapes")
fruits.remove("cherry")

print("Q3:", fruits)


# Q4. Reverse Without reverse()

numbers = [12, 45, 23, 67, 89, 34]

reversed_numbers = numbers[::-1]

print("Q4:", reversed_numbers)
print("Original list:", numbers)


# Q5. Second Largest Unique Number

numbers = [45, 12, 89, 34, 89, 67, 45, 23]

unique_sorted = sorted(set(numbers))
second_largest = unique_sorted[-2]

print("Q5:", second_largest)


# Q6. Rotate a List

numbers = [10, 20, 30, 40, 50, 60]
k = 2

rotated = numbers[-k:] + numbers[:-k]

print("Q6:", rotated)


# Q7. Remove Duplicates, Preserve Order

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

without_duplicates = list(dict.fromkeys(numbers))

print("Q7:", without_duplicates)


# Q8. Flatten a Nested List

data = [[10, 20], [30, 40], [50, 60]]

flattened = data[0] + data[1] + data[2]

print("Q8:", flattened)


# Q9. Extract Data from a Matrix

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

main_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
secondary_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
middle_column = [matrix[0][1], matrix[1][1], matrix[2][1]]

main_diagonal_sum = sum(main_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)
middle_column_sum = sum(middle_column)

print("Q9 Main Diagonal:", main_diagonal, "Sum:", main_diagonal_sum)
print("Q9 Secondary Diagonal:", secondary_diagonal, "Sum:", secondary_diagonal_sum)
print("Q9 Middle Column:", middle_column, "Sum:", middle_column_sum)


# Q10. List Transformation Challenge

data = [15, 5, 25, 10, 35, 20, 30]

unique_sorted = sorted(set(data))
three_largest_ascending = unique_sorted[-3:]
two_smallest_descending = unique_sorted[:2][::-1]

result = three_largest_ascending + two_smallest_descending

print("Q10:", result)

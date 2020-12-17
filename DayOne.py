import csv
import math

# Part 1

list_of_nums = []
with open('input.txt') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_of_nums.append(int(row[0]))

result_nums = []

for num in list_of_nums:
    if math.fabs(2020 - num) in list_of_nums:
        result_nums.append(num)
        result_nums.append(int(math.fabs(2020 - num)))
        break

print(result_nums[0] * result_nums[1])

# Part 2

result_nums = []
for i in range(len(list_of_nums)):
    split_number = 2020 - list_of_nums[i]
    for j in range(len(list_of_nums)):
        if split_number - list_of_nums[j] in list_of_nums:
            result_nums.append(list_of_nums[i])
            result_nums.append(list_of_nums[j])
            result_nums.append(split_number - list_of_nums[j])
            break
    if len(result_nums) == 3:
        break
print(result_nums)
import csv
import math

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
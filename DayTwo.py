import csv

list_of_passwords = []

with open('password_input.txt') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_of_passwords.append(row[0])

valid_passwords = []

for item in list_of_passwords:
    password_checker = item.split(' ')
    password_checker[0] = password_checker[0].replace('-', ',')
    password_checker[1] = password_checker[1].replace(':', '')
    password_checker[0] = password_checker[0].split(',')
    min_times = int(password_checker[0][0])
    max_times = int(password_checker[0][1])
    if min_times <= password_checker[2].count(password_checker[1]) <= max_times:
        valid_passwords.append(password_checker[2])

print(len(valid_passwords))
new_valid_passwords = []
for item in list_of_passwords:
    password_checker = item.split(' ')
    password_checker[0] = password_checker[0].replace('-', ',')
    password_checker[1] = password_checker[1].replace(':', '')
    password_checker[0] = password_checker[0].split(',')
    password_checker[0][0] = int(password_checker[0][0]) - 1
    password_checker[0][1] = int(password_checker[0][1]) - 1
    count = 0
    if password_checker[1] == password_checker[2][password_checker[0][0]]:
        count += 1
    if password_checker[1] == password_checker[2][password_checker[0][1]]:
        count += 1
    if count == 1:
        new_valid_passwords.append(item)

print(len(new_valid_passwords))

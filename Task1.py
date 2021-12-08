"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


total_phone_numbers = []


def get_phone_numbers(data):
    phone_numbers = []
    for row in data:
        phone_numbers.append(row[0])
        phone_numbers.append(row[1])
    return phone_numbers


def count_different_numbers(numbers):
    return len(set(numbers))


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    total_phone_numbers.extend(get_phone_numbers(texts))


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    total_phone_numbers.extend(get_phone_numbers(calls))


different_numbers = count_different_numbers(total_phone_numbers)
print(f'There are {different_numbers} different telephone numbers in the records.')

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

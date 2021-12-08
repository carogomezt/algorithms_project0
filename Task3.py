"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_area_codes_and_prefixes(data, area_code):
    total_codes = []
    for row in data:
        if row[0].startswith(area_code):
            code_num = ""
            if row[1].startswith('('):
                code_num = row[1].split(')')[0] + ')'
            elif ' ' in row[1]:
                code_num = row[1][:4]

            total_codes.append(code_num)
    total_codes.sort()
    unique_area_codes_and_prefixes = set(total_codes)
    return unique_area_codes_and_prefixes


# Part A:


area_code = '(080)'
area_codes_and_prefixes = get_area_codes_and_prefixes(calls, area_code)

print('The numbers called by people in Bangalore have codes:')
for code_num in area_codes_and_prefixes:
    print(code_num)


# Part B:

def get_percentage_of_area_calls(data, area_code):
    total_calls = 0
    calls_to_fixed_line = 0
    for row in data:
        if row[0].startswith(area_code):
            total_calls += 1
            if row[1].startswith(area_code):
                calls_to_fixed_line += 1

    percentage = (calls_to_fixed_line * 100) / total_calls
    return percentage


percentage_calls = get_percentage_of_area_calls(calls, area_code)
print(f'{percentage_calls:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

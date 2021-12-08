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


def get_telephone_marketing_numbers(texts, calls):
    text_senders = set([num[0] for num in texts])
    text_receivers = set([num[1] for num in texts])
    calls_telephone = set([num[0] for num in calls])
    calls_receivers = set([num[1] for num in calls])

    telemarketers = calls_telephone - text_senders - text_receivers - calls_receivers
    telemarketers_list = list(telemarketers)
    telemarketers_list.sort()

    return telemarketers_list


telemarketers = get_telephone_marketing_numbers(texts, calls)

print('These numbers could be telemarketers: ')
[print(num) for num in telemarketers]

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


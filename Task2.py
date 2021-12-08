"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def print_longest_phone_call_time(data):
    calls_duration = {}
    for row in data:
        # calling telephone number
        if calls_duration.get(row[0]):
            calls_duration[row[0]] += int(row[3])
        else:
            calls_duration[row[0]] = int(row[3])

        # receiving telephone number
        if calls_duration.get(row[1]):
            calls_duration[row[1]] += int(row[3])
        else:
            calls_duration[row[1]] = int(row[3])

    max_call_duration_phone = max(calls_duration, key=calls_duration.get)
    max_call_duration_time = max(calls_duration.values())
    print(f'{max_call_duration_phone} spent the longest time, {max_call_duration_time} seconds, on the phone during September 2016.')


print_longest_phone_call_time(calls)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


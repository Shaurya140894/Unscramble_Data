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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def dict_key(lst):
    dict1 = {}
    for call in lst:
        if call[0] not in dict1.keys():
            dict1[call[0]] = int(call[-1])
        else:
            dict1[call[0]] += int(call[-1])

        if call[1] not in dict1.keys():
            dict1[call[1]] = int(call[-1])
        else:
            dict1[call[1]] += int(call[-1])
    return dict1


def longestduration(dict1):
    dict_duration = dict_key(dict1)
    duration = 0
    phone_number = 0

    for key in dict_duration.keys():
        if duration == 0 or duration < dict_duration[key]:
            duration = dict_duration[key]
            phone_number = key

    return "{} spent the longest time, {} seconds, on the phone during september 2016".format(phone_number, duration)


print(longestduration(calls))

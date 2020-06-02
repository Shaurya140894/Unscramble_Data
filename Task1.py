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

# print(texts)
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def phone_number(data):
    list1 = []
    list2 = []
    for item in data:
        list1.append(item[0])
        list2.append(item[1])
    return list1,list2


def all_lists(call,text):
    call_list_out = phone_number(call)[0]
    call_list_in = phone_number(call)[1]
    text_list_out = phone_number(text)[0]
    text_list_in = phone_number(text)[1]
    new_list = call_list_out + call_list_in + text_list_out + text_list_in
    set1 = set(new_list)
    return "There are {} different telephone numbers in the records.".format(len(set1))

print(all_lists(calls,texts))
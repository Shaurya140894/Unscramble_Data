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


def number_set(text,call):
    text_numbers = set()
    for num in text:
        text_numbers.add(num[0])
        text_numbers.add(num[1])
    for num in call:
        text_numbers.add(num[1])
    return text_numbers


def num_check(text,call):
    text_numbers = number_set(text,call)
    tele = set()
    for item in call:
        number = item[0]
        if number not in text_numbers:
            tele.add(number)
    return tele


def print_func(dict1,dict2):
    list1 = sorted(num_check(dict1,dict2))
    str1 = "\n"
    str1 = str1.join(list1)
    return "These numbers could be telemarketers:\n{}".format(str1)


print(print_func(texts,calls))
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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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


def all_numbers_from_bangalore(call):
    prefix = set()
    for item in call:
        if "(080)" in item[0]:
            prefix.add(item[1])
    return sorted(prefix)


def landline_numbers(call):
    data = all_numbers_from_bangalore(call)
    landline = set()
    for item in data:
        if "(" in item:
            landline.add(item)
    return sorted(landline)


def landline_number_prefix(call):
    data = list(landline_numbers(call))
    prefix = set()
    for item in data:
        prefix.add(item[0:item.find(")")+1])
    return sorted(prefix)


def mobile_numbers(call):
    data = all_numbers_from_bangalore(call)
    mobile = []
    for item in data:
        if "(0" not in item:
            mobile.append(item)
    return set(mobile)


def mobile_number_prefix(call):
    data = list(mobile_numbers(call))
    prefix = set()
    for item in data:
        prefix.add(item[0:4])
    return sorted(prefix)


def all_calls(call):
    landline = landline_number_prefix(call)
    mobile = mobile_number_prefix(call)
    new_list = landline + mobile
    str1 = "\n"
    str1 = str1.join(new_list)
    return "The numbers called by people in Bangalore have codes:\n{}".format(str1)


def banglore_to_banglore(call):
    btob = 0
    btoa = 0
    for item in call:
        if "(080)" in item[0]:
            if "(080)" in item[1]:
                btob += 1
    for item in call:
        if "(080)" in item[0]:
            btoa += 1

    percentage = round(((btob/btoa)*100),2)
    return "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."\
        .format(percentage)


# print(all_numbers_from_banagalore(calls))
# print(landline_numbers(calls))
# print(landline_number_prefix(calls))
# print(mobile_numbers(calls))
# print(mobile_number_prefix(calls))
print(all_calls(calls))
print(banglore_to_banglore(calls))

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import itertools
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def text_log(text):
    return "First record of texts, {} texts {} at time {}".format(text[0][0],text[0][1],text[0][2])


def call_log(call):
    return "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call[-1][0],call[-1][1],
                                                                                     call[-1][2],call[-1][3])


print(text_log(texts))
print(call_log(calls))

# Word Summary
#
# Download the programmers_blues.txt file. Write a program to read in the text of that file and count the number of occurrences of each word in that file. You will print one line for each word encountered, and output the number of times that word appearred in the file. The output should look something like:
#
# $ python word_count.py
# code: 1
# help: 1
# just: 3
# don't: 1
# hand,: 1
# better,: 1
# copped,: 1
# won't: 1
# keyboard: 1
# ...
# programmer's: 7
# think: 1
# analyst's,: 1
# beta: 1
# testing,: 1
# hackers: 1
# feel: 1
# megabyte: 1
# one: 2
# ...
# you'll: 1
# so: 2
# ultimate: 1
# typing,: 1
# dos: 1
# the: 15
# alone,: 1
# know: 1
# Hint: to strip away the periods and parenthesis in the text I recommend doing the following:
#
# text = text.replace('.', '').replace('(', '').replace(')', '')

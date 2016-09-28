# Word Summary
#
# Download the programmers_blues.txt file. Write a program to read in the text of that file and count the number of occurrences of each word in that file. You will print one line for each word encountered, and output the number of times that word appearred in the file. The output should look something like:
#
# Hint: to strip away the periods and parenthesis in the text I recommend doing the following:
#
# text = text.replace('.', '').replace('(', '').replace(')', '')
blues = open('programmers_blues.txt')
import pickle

blues_string = blues.read()

blues_string = blues_string.replace('.', '').replace("'", '').replace(')', '').replace(',', '').replace('!', '').replace("(", '')
blues_string = blues_string.lower()
# print blues_string.split()
blues_words = blues_string.split()


counts = {}

for word in blues_words:
    current_tally = counts.get(word, 0)
    new_tally = current_tally + 1
    counts[word] = new_tally

for word, count in counts.items():
    print "%d %s's" % (count, word)

# print words
# for char, count in words.items():
#     print "%d %s's" % (count, words)
entries = counts.items()
version 1
def mykey((word, count)):
    return count
version 2
entries.sort(key=lambda (word, count): count, reverse=True)

version 3
entries.sort(key=lambda entry: entry[1], reverse=True)



for word, count in top_10:
    print "%s appeared %d times." % (word, count)

version 4
entries.sort(key=counts.get, reverse=True)

top_10 = entries[0:10]

# from sys import argv
# script, filename = argv
# print "We're going to erase %r." % filename
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit RETURN."
#
# raw_input("?")
# 
# print "Opening the file..."
# target = open(filename, 'w')
#
# print "Truncating the file. Seeya!"
# target.truncate()
#
# print "Now I'm going to ask you for three lines."
#
# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")
#
# print "I'm going to write these to the file."
#
# target.write(line1)
# target.write("  \s\s")
# target.write(line2)
# target.write("  \s\s>")
# target.write(line3)
# target.write("  ")
#
# print "And finally, we close it."
# target.close()

#Line Count
#
# Write a program which when given the name of a file as a command line argument,
# will print the number of lines there are in the file. Example session:
# in_data = open(filename).read()
# print yin_data
# length = len(in_data)
# print "length of file is: %r" % length

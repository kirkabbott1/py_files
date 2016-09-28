# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# print txt.read()
#
# print "Type the filename again:"
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

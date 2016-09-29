
import pickle
from os.path import exists

if exists('phonebook_file'):
    print 'loading phone book.'
    phonebook_file = open('phonebook.pickle', 'r')
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()
else:
    phonebook_dict = {}
while True:
    print "Electronic Phone Book"
    print "====================="
    print ("1\. Look up an entry")
    print ("2\. Set an entry")
    print ("3\. Delete an entry")
    print ("4\. List all entries")
    print ("5\. save all entries")
    print ("6\. Quit")
    response = int(raw_input("What do you want to do? (1-5)"))


    if response == 1:
        name = raw_input("the name?").lower()
        if name in phonebook_dict:
            phone_number = phonebook_dict[name]
            print " %s's number is %s" % (name, phone_number)#look up phone number by name provided
        else:
            print "%s is not in phone book." % name
    elif response == 2:
        name = raw_input("the name?").lower()
        phone_number = raw_input("the number?")
        phonebook_dict[name] = phone_number
        print "Stored %s's number." % name
    elif response == 3:
        name = raw_input("What's the name to delete?").lower()
        if name in phonebook_dict:
            del phonebook_dict[name]
            print "deleted %s's information" % name
        else:
            print "%s inot in phone book" % name
        del phonebook_dict[name]
        print "Deleted %s's number." % name
    elif response == 4:
        sorted_phonebook_list = sorted(phonebook_dict.items(), key=lambda (name, phone): name, reverse=True)
        print "Your phonebook contains the following information:\n"
        for name, phone_number in sorted_phonebook_list:
            print "\tName: %s\n\t\tPhone number: %s" % (name, phone_number)
        print "\n"
        # print "Found %s's number: %s" % (name, phone_number)
    elif response == 5:
        phonebook_file = open('phonebook.pickle', 'w')
        pickle.dump(phonebook_dict, phonebook_file)
        phonebook_file.close()
        print 'Phone book saved.'

        #go through all entries in the dictionary and print each out to the terminal.
    else:
        print "bye"
        break


print phonebook_dict
myfile = open('phonebook.pickle', 'w')
pickle.dump(phonebook_dict, myfile)
phonebook_file.close()

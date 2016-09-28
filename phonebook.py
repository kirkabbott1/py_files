
import pickle

myfile = open('phonebook.pickle', 'w')
pickle.dump(phonebook_dict, myfile)
myfile.close()


print "Electronic Phone Book"
print "====================="
print ("1\. Look up an entry")
print ("2\. Set an entry")
print ("3\. Delete an entry")
print ("4\. List all entries")
print ("5\. Quit")

phonebook_dict = {}

def phonebookf():
    response = raw_input("What do you want to do? (1-5)")
    if response == "1":
        name = raw_input("the name?")
        print name
        print number#look up phone number by name provided
    elif response == "2":
        name = raw_input("the name?")
        number = raw_input("the number?")
        phonebook_dict[name] = number
    elif response == "3":
        name = raw_input("What's the name to delete?")
    elif response == "4":
        pass
        #go through all entries in the dictionary and print each out to the terminal.
    else:
        pass
phonebookf()

print phonebook_dict

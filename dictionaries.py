# Dictionary Exercises
#
# Exercise 1
#
# Given the following dictionary, representing a mapping from names to phone numbers:
#
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# Write code to do the following:
#
# Print Elizabeth's phone number.
# Add a entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# print phonebook_dict['Elizabeth']
# phonebook_dict['Kareem'] = "770-234-3242"
#
# del phonebook_dict['Alice']
# print phonebook_dict
# phonebook_dict['Bob'] = "345-234-2342"
# print phonebook_dict
# for key, value in phonebook_dict.items():
#     print phonebook_dict.values()

# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests.

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print ramit['email']
print ramit['interests'][0]
print ramit['friends'][0]['email']
print ramit['friends'][1]['interests'][1]

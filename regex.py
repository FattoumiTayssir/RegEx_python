# first we import the module re
import re

# a sample using re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# Regex functions
# findall : return list containing all matches
# search : return  a match object like x
# split : retun a list where the string has been split at each match
# sub : replace one or many matches with a string


# []	A set of characters	"[a-m]"
my_string = "The rain in Spain"
char_set = re.findall("[a-m]", my_string)
print(char_set)


# \	Signals a special sequence (can also be used to escape special characters)
# example "\d"
txt = "That will be 59 dollars"
# Find all digit characters:
x = re.findall("\d", txt)
print(x)


# .	Any character (except newline character)	"he..o"
txt = "hello world"
# Search for a sequence that starts with "he",
# followed by two (any) characters,
# and an "o":
x = re.findall("he..o", txt)
print(x)

# ^	Starts with	"^hello"
txt = "hello world"
# Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

# $	Ends with	"world$"
txt = "hello world"

# Check if the string ends with 'world':
x = re.findall("world$", txt)
if x:
    print("Yes, the string ends with 'world'")
else:
    print("No match")

"""
This code show the basic string manipulation
opration in python...
"""

# Input string for code testing...
print "\n"
str1 = input("Enter any string for testing : ")
print "Enterd string for testing is : " +  str1


# Use of index() and find() function...
print "\nDemo for input() and find() function..."
var1 = "s"
var2 = str1.find(var1)

if var2 == 0:
 print "Index of the " + var1 + " is :" + str(str1.index("s"))
else:
 print var1 + " is not presont in Input string ! "


# Find the lenght of the input string...
var3 = len(str1)
print "\nLength of the input string is : " + str(var3) + "\n"


# Print the string from given index renge...
print "\nDemo for printing string from given index by user !"
print "Given input must be relavent to length of the string..." 
var1 = input("Enter First Boundary : ")
var2 = input('Enter Second Boundary : ')

print "New String is : " + str1[var1:var2]

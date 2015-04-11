"""
This code show the how to print index of given input character from test1.txt...
"""
# Open test1.txt for reading...
f = open('test1.txt','r')
var1 = f.read()

# Enter char from user to find index in available data...
char1 = raw_input("Enter character for index finding : ")
var2 = var1.find(char1) # To check wether input character presant in test1.txt

if var2 == -1:
 print1 = char1 + " is not presont in test1.txt"

else:
#idx = var.index('a')
 print1 = "Index of " + char1 + " is " + str(var2)

# Write output in the output file...
f = open('output2.txt','w')
f.write(print1)

# Read and print output2.txt file...
f = open('output2.txt','r')
var = f.read()
print var



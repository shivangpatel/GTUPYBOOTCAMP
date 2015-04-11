"""
This code show the basic i/o oprations...
"""

# File reading demo...
print "\nFile Reading Demo..."
b = open('test.txt','r')
a = b.read()
print "Content of test.txt is :\n" + a + '\n'

# File reading and writing...
print "file Wring and Reading Demo..."
b = open('test.txt','wb') #open a test.txt file for writing...
a = b.write('Opss ! File Override !') #write contetn in test.txt file 

b = open('test.txt','r') #open a text.txt file for writing...
a = b.read()
print "After writing opration Content of test.txt is :\n" + a +'\n'


# File appending...
print "file appending..."
b = open('test.txt','ab+') #open a test.txt file for writing...
a = b.write('Add New Contents !') #write contetn in test.txt file 

b = open('test.txt','r') #open a text.txt file for writing...
a = b.read()
print "After appending opration Content of test.txt is :\n" + a +'\n'

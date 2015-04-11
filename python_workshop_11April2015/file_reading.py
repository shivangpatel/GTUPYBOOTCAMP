
# file reading demo...
print "File Reading Demo..."
b = open('test.txt','r')
a = b.read()
print a+'\n'


# file reading and writing...
print "file Wring and Reading Demo..."
b = open('test.txt','wb') #open a test.txt file for writing...
a = b.write('Opss ! File Override !') #write contetn in test.txt file 

b = open('test.txt','r') #open a text.txt file for writing...
a = b.read()
print a+'\n'


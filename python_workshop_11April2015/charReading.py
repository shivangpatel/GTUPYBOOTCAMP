
# Open test1.txt for reading...
f = open('test1.txt','r')
var = f.read()

#print var
#userDemand = input('')
aa = var.index('a')
#print aa

f = open('output2.txt','w')
f.write(str(aa))

f = open('output2.txt','r')
var = f.read()
print var



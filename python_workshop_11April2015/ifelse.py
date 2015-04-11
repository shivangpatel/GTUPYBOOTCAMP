f = open('test.txt','r')
var = int(f.read())

if var > 200:
 ans = 'Greater then 200' 
elif var < 200:
 ans = 'Less then 200'
else:
 ans = 'equal to 200'
print ans
b = open('output.txt','w')  
b.write(ans)

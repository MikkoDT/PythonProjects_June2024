#writing data to the file
f = open('demo.txt','w')
f.write("Hello there!")
f.close()

#reading data from the file
f = open('demo.txt','r')
print(f.read())
f.close()

#adding additional contents
f = open('demo.txt','a')
f.write('\n Hello again!')
f.close()
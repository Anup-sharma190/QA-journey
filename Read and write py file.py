#file=open("test.txt")
# read all the content of file
#print(file.read())
#file.close()
# to close the file after read
# if want to read only 2 charcter from file
#file= open("test.txt")#read n number of character by passing parameter
#print(file.read(5))# it will consider space also one character
#file.close()
# read line by line
file=open("test.txt")
#print(file.readline())# read one single line
#print(file.readline())# if keep on writing these next next line will come to print
#print(file.readline())
#file.close()
#print line by line using reading method
file=open("test.txt")
line= file.readline()
while line != " ":
    print(line)
    line = file.readline()
file.close()

w

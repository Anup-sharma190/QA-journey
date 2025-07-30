#read the file and store all the lines in list
#reverse the list
# write the list back to file
#FILE = open("test.txt")as a file :
with open("tust.txt", "r") as  reader:
    content= reader.readlines()
    reversed(content)
    with open("tust.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
with open("tust.txt", "r") as  reader:
    content= reader.readlines()
    reversed(content)
    ####################
file = open(tust.txt)
print(file)

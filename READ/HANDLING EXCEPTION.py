#from logging import exception

#itemincart= 3

#if itemincart != 2: #raise exception("not match")#raise exception

#assert(itemincart==3)
# try and catch mechanism
#try:
    #with open("popup1.txt", "r") as reader:
        #reader.read()
#except:
    #print("try block fail")
try:
    with open("popup1.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)


str= "rahul shetty"
str2=("great teacher")
print(str+" "+str2)# string concatenation
str3 = "rahul"
if str3 in str:
    print("true")
else:
    print("false")
print(str3 in str)# check string is present in parent string or not to do testing of string
string= "rahulshetty"
print(string[0:5])
x= "anup.com"
var= x.split(".")# split
print(var)
print(type(var))
print(var[0])# extract value useing index
a= (" rahul ")
print(a.strip()) # remove space both end
a= (" rahul ")
print(a.lstrip())# to remove space from left
a= (" rahul ")
print(a.rstrip())# to remove space from right
a= (" rahul ")
print(a.strip())
from pythonBasics.OopsDemo import Calculator
class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())

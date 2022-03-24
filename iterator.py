mytuple=('apple','banana','cherry')
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print('  \n xxxxx \n')
newtuple=('pineapple')
newit=iter(newtuple)

print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))


for x in (mytuple):
    print(x)

mystr="grapes"

for x in (mystr):
    print(x)

print(' \n xxxxxxxxxxx \n ')
class mynumber:
    def __iter__(self):
        self.a=10
        return(self)
    def __next__(self):
        x=self.a
        self.a += 1
        return(x)

myclass=mynumber()
myiter= iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Function inside Function

def myfunc():            #local scope
    x=300
    def interfunc():print(x,'\n')
    interfunc()

myfunc()

#Global Scope

x=300    #This x will have global scope

def newfunc():
    x=2000  #local scope
    global y             #for Global keyword first define variable then assign value
    y=2433
    print(x)

newfunc()

print(x)
print(y)





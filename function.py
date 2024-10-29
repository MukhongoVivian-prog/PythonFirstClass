# built in
y = max(32,67,54,43)
print(y)

x= min(65,3,2,56)
print( "the minimum value is",x)

z= pow(4,5)
print("the result is",z)

def greeting():
    print("Hello there!" )

greeting()   #calling a function

def multiply():
    num1 = 23
    num2 = 45
    print(num1 * num2)
multiply()


#Parameters/variable and arguments/values assigned to parameters
def add(a,b):
    print(a+b)
    return a+b
add(34,56)
add(4.5,3.4)

def employee(fullname, age,position,status):
    print(fullname,age,position,status)

employee("Shau chei",45,"CEO","married")
employee("Sei Juan",34,"manager","married")
employee("mark joe",30,"director","single")
employee("June July",36,"HR","married")
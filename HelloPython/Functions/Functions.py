def greet():
    print("Welcome to learn Python!!!")


greet()


def greet(user):
    print("Welcome ",user,", to learn Python!!!")


greet("Surajit")


def add_numbers(a, b):
    return a+b


print("The sum of 2 numbers are  - ", add_numbers(10, 20))


"""
Keywords based parameters
"""


def keyword_params(n1,n2, n3):
    print("N1 is ", n1)
    print("N2 is ", n2)
    print("N3 is ", n3)

keyword_params(n3=300,n1=100,n2=200)


"""
Default parameter functions
"""


def default_param(n1,n2=100):
    print("Sum is ", n1+n2)


default_param(200,300)
default_param(300)


"""
Multiple arguments function
"""


def multiple_args(*args_list):
    for arg in args_list:
        print(arg)


multiple_args("Hello", "This", "Is", "Surajit.")


def multiple_kwargs(**kwargs_list):
    for kwargs in kwargs_list:
        print(kwargs," = ", kwargs_list[kwargs])


multiple_kwargs(s1="This", s2="Is", s3="Surajit")

"""
Anonymous functions / lambda 
"""


mult = lambda n1,n2,n3: n1*n2*n3

print(mult(10,20,30))

def getStudentData():
    return "Ram", "Sharma", 34

fname,lname,age = getStudentData()
print("First Name is ",fname)
print("Last Name is ",lname)
print("Age is ", age)




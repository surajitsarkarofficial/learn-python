from ExceptionHandling.MyCustomException import MyCustomException

try:
    result = 100/0

except:
    print("Exception occurred and handled...")


# throw an exception
"""
threshold = 11

if threshold<=10:
    print("Within threshold limit...")

else:
    raise Exception("Threshold limit exceeded...")
"""
# handle the exception being thrown

try:
    # throw an exception
    threshold = 11

    if threshold <= 10:
        print("Within threshold limit...")

    else:
        raise Exception("Threshold limit exceeded...")
except Exception as e:
    print(e)

# handle run time exception
try:
    with open('myfile.txt') as file:
        file.read()
except Exception as e:
    print(e)

# finally
name = "Ro"
try:
    if len(name) < 3:
        raise Exception("Name must be atleast 3 characters")
    else:
        print("Name is valid..")
except Exception as e:
    print(e)
finally:
    print("Name has been validated succesfully...")

# Raise custom excpetion
age = 16

try:
    if age < 18:
        raise MyCustomException("Voter is a minor and not eligible to vote...")
except MyCustomException as me:
    print(me)



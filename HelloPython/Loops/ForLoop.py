# print 1 to 10
for i in range(1, 11):
    print(i)
# print elements of a list
fruits = ["apple", "banana", "mango", "orange", "pineapple"]
for fruit in fruits:
    print(fruit)

# iterate loops by incrementing iterator by 2
for i in range (0,20,2):
    print(i)

# print values 0 to 5
# if we do not mention start value in range then it starts from 0
for i in range(6):
    print(i)

# print values of a list based on its index
for i in range(0,len(fruits)):
    print("{} {} {} {}".format("The fruit name at index ", i,"is",fruits[i]))

# print the pattern
#   *
#   *   *
#   *   *   *
#   *   *   *   *
#   *   *   *   *   *

for row in range(1,6):
    for col in range (1,row+1):
        print("*", end="")
    print("\r")

# print sep
print(1,2,3,4,5,6,7,8,9,10,sep='-')

string = "Surajit"
for s in string:
    print(s)
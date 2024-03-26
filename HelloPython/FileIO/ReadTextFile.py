file = open('dummy.txt')
print(file.read())
file.close()
# read a single line
file = open('dummy.txt')
print(file.readline())
file.close()
# read a lines line by line
file = open('dummy.txt')
lines = file.readlines()
for line in lines:
    print(line)
file.close()

#if we don't want to handle closing of file
with open('dummy.txt') as file :
    for line in file.readlines():
        print(line)


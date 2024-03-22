# print 1 to 10
counter= 1
while counter<=10:
    print(counter)
    counter+=1

# break the loop if num is 31 in the list
numsList = [10, 99, 33, 11, 90, 92, 17, 21, 31, 56, 48, 24]
i=0
while i<len(numsList):
    if numsList[i]==31:
        break;

    print(numsList[i])
    i+=1


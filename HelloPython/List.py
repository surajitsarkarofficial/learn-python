# it is similar to link list /array list in java

rawData = [1, "mango", "Rohan", 110, 22.89, "riya", "Nifty"]

print("Printing the data of the list", rawData)

print("Last index value is ",rawData[-1])

print("Sub list from index 2 to 5 ", rawData[2:5])

#updating a value of an index
rawData[1]="MANGO"
print("Updated list is ",rawData)

#inserting a value to a list
rawData.insert(3 ,"I am a new data")
print("Updated list is ",rawData)

# append a value in the list
rawData.append("I am the last appended data")
print("Updated list is ",rawData)

#Delete a data
del rawData[4]
print("Updated list is ",rawData)


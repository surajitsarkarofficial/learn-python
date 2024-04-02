name = "surajit"
lastName = 'sarkar'
address = """Flt 100, Apna Soceity
                Sundar Road
                Apni seher
                apna rajya"""

print(name,lastName,address,sep="---")


print(name.upper())

print("name[:] = ",name[:])
print("name[0:] = ",name[0:])
print("name[:7] = ",name[:7])
print("name[0:7] = ",name[0:7])
print("name[2:6] = ",name[2:6])

print("name[-1] = ",name[-1])
print("name[-3:] = ",name[-3:])
print("name[-3:-1] = ",name[-3:-1])
print("name[::-1] = ", name[::-1])

# Operators
str = "HELLO"
print(str+str)
print(str*2)
print("HE" in str)
print ("HLO" in str)
print ("HEY" not in str)
print ("LO" not in str)
print(r"https://mypythonworld.com/login")
print("The string is %s"%(str))
print("Rahul said \"This is not Possible...\"")


#String Casing
sentence = "Hello this is Python learning..."
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())
print(sentence.swapcase())
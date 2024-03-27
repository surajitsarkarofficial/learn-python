print('Enter your name')
name=input()
print('Enter you Gender (M/F).')
gender=input()
if gender not in ['M','F']:
    raise Exception("Invalid gender...")
print('Enter Phone Number')
phn=input()
phn=int(phn)
if len(phn) !=10:
    raise Exception("Invalid Phone number...")
print('Details entered are --- ')
print(name,gender,phn,sep=" | ")
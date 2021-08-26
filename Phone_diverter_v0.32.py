#Initiate options
import re
newf=""
options = ["always", "busy", "offline", "no-answer"]
#Print instructions
print("This program relies on having your text file in the same directory as this file. Also, any numbers must be in E.164 format and on separate lines.")

#Prompt for input
fileStr=input("Enter the name of your text file: ")

#Print forwarding options
print("Option 1: Always")
print("Option 2: Busy")
print("Option 3: Offline")
print("Option 4: No-answer")

#Get user input for forwarding type
forwardStr=int(input("Enter a number: "))
if forwardStr in range (1,4):
    forwardStr=options[forwardStr-1]
else:
    print("Invalid option")
    sys.exit()
numberStr=input("Enter the forwarding number: ")
#Fix incorrect format numbers - WIP
'''
numberStr.strip()
numberStr = "".join( numberStr.split() )
formatCatch = numberStr.startswith('0')
if formatCatch is True:
    numberStr.replace("0", "64", 1)
'''
re.sub("[^0-9]", "", str(numberStr))
#Construct String
with open(fileStr,'r') as f:
    for line in f:
        newf+=line.strip()+","+str(forwardStr)+","+str(numberStr)+";"
    f.close()

#Write file    
with open(fileStr,'w') as f:
    f.write(newf)
    f.close()


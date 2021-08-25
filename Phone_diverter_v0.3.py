newf=""
options = ["always", "busy", "offline", "no-answer"]
print("This program relies on having your text file in the same directory as this file. Also, any numbers must be in E.164 format and on separate lines.")
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
numberStr=input("Enter the forwarding number: ")

#Consturct String
with open(fileStr,'r') as f:
    for line in f:
        newf+=line.strip()+","+str(forwardStr)+","+str(numberStr)+";"
    f.close()

#Write file    
with open(fileStr,'w') as f:
    f.write(newf)
    f.close()

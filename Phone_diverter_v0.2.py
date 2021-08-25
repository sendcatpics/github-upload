newf=""
print("This program relies on having your text file in the same directory as this file. Also, any numbers must be in E.64 format and on separate lines.")
fileStr=input("Enter the name of your text file: ")
forwardStr=input("Enter the forwarding type: ")
numberStr=input("Enter the forwarding number: ")
with open(fileStr,'r') as f:
    for line in f:
        newf+=line.strip()+","+str(forwardStr)+","+str(numberStr)+";"
    f.close()
with open(fileStr,'w') as f:
    f.write(newf)
    f.close()

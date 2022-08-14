import os, sys

name = input("Enter the file name: ")

if os.path.isfile(name):
    print("File is present")
    fp = open(name, 'r')
    print("The content is: ")
    data = fp.read()
    print(data)

else:
    print("file is not present")
    sys.exit(0)



fp.close()




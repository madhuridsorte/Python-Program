from genericpath import isfile
import os , sys

name = input("Enter the file name: ")

if os.path.isfile(name):
    fp = open(name, 'r')


else:
    print("File is not present")
    sys.exit(0)

lcount=wcount=ccount=0

for i in fp:
    lcount = lcount+1
    ccount = ccount+len(i)
    word = i.split()
    print(word)
    wcount=wcount+len(word) 

print(lcount)
print(ccount)   
print(wcount)
    
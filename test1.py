import os 

cwd = os.getcwd()
print("The current working directory is: ", cwd)

# os.mkdir("subdir")
# print("The subdir is created")

# os.mkdir("subdir/subdir2")
# print("The subdir is created under subdir")

# os.makedirs("sub1/sub2/sub3")
# print("sub1 and in that sub2 and in that sub3 directories created")

# os.rmdir("subdir/subdir2")
# print("subdir2 deleted")

# os.removedirs("sub1/sub2/sub3")
# print("sub1, sub2, sub3 deleted")

# os.rename('subdir', 'mydir')
# print("name changed")

print(os.listdir("."))
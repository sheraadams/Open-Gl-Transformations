# Shera Adams
# this program performs usual functions to transform long lists of numbers for easier manipulation of objects in opengl.
# The program takes input with characters and will remove unwanted characters, then transform each element and then add the necessary characters after transformation

# strip sting of unwanted spaces and character f
# the important thing here is to keep it in a string format without lines or tabs.
str1 = " 1.0f, 0.0f,  0.0f,  1.5f, -0.5f, 0.0f, -1.0f,  0.0f,  0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 1.0f,  0.0f,  0.0f,0.5f, 0.5f, 0.5f, -0.5f, 0.0f, 1.0f,  0.0f,  0.0f, 0.0f, 0.0f, -0.5f, -0.5f, 0.0f, 1.0f,  0.0f,  0.0f, 1.0f, 0.0f"
for z in range(len(str1)):
    str1 = str1.replace(" ", "")
    str1 = str1.replace("f", "")
print(str1)

transformed = []
print("Copy this list to integers to finish formatting and transformation: ")
# transform a list of integers

#Enter in list here:
integers = [-0.5,-0.5,-0.5,0.0,0.0,-1.0,0.5,-0.5,-0.5,0.0,0.0,-1.0,0.5,0.5,-0.5,0.0,0.0,-1.0,0.5,0.5,-0.5,0.0,0.0,-1.0,-0.5,0.5,-0.5,0.0,0.0,-1.0,-0.5,-0.5,-0.5,0.0,0.0,-1.0,-0.5,-0.5,0.5,0.0,0.0,1.0,0.5,-0.5,0.5,0.0,0.0,1.0,0.5,0.5,0.5,0.0,0.0,1.0,0.5,0.5,0.5,0.0,0.0,1.0,-0.5,0.5,0.5,0.0,0.0,1.0,-0.5,-0.5,0.5,0.0,0.0,1.0,-0.5,0.5,0.5,-1.0,0.0,0.0,-0.5,0.5,-0.5,-1.0,0.0,0.0,-0.5,-0.5,-0.5,-1.0,0.0,0.0,-0.5,-0.5,-0.5,-1.0,0.0,0.0,-0.5,-0.5,0.5,-1.0,0.0,0.0,-0.5,0.5,0.5,-1.0,0.0,0.0,0.5,0.5,0.5,1.0,0.0,0.0,0.5,0.5,-0.5,1.0,0.0,0.0,0.5,-0.5,-0.5,1.0,0.0,0.0,0.5]
for i in integers:
    i = i * 2
    print(i, end = ", ")
print("Copy this to str4 this is the transformed list:")

#convert the transformed vectors to opengl format and print
str4 = "-0.15, -0.15, -0.15, 0.0, 0.0, -0.3, 0.15, -0.15, -0.15, 0.0, 0.0, -0.3, 0.15, 0.15, -0.15, 0.0, 0.0, -0.3, 0.15, 0.15, -0.15, 0.0, 0.0, -0.3, -0.15, 0.15, -0.15, 0.0, 0.0, -0.3, -0.15, -0.15, -0.15, 0.0, 0.0, -0.3, -0.15, -0.15, 0.15, 0.0, 0.0, 0.3, 0.15, -0.15, 0.15, 0.0, 0.0, 0.3, 0.15, 0.15, 0.15, 0.0, 0.0, 0.3, 0.15, 0.15, 0.15, 0.0, 0.0, 0.3, -0.15, 0.15, 0.15, 0.0, 0.0, 0.3, -0.15, -0.15, 0.15, 0.0, 0.0, 0.3, -0.15, 0.15, 0.15, -0.3, 0.0, 0.0, -0.15, 0.15, -0.15, -0.3, 0.0, 0.0, -0.15, -0.15, -0.15, -0.3, 0.0, 0.0, -0.15, -0.15, -0.15, -0.3, 0.0, 0.0, -0.15, -0.15, 0.15, -0.3, 0.0, 0.0, -0.15, 0.15, 0.15, -0.3, 0.0, 0.0, 0.15, 0.15, 0.15, 0.3, 0.0, 0.0, 0.15, 0.15, -0.15, 0.3, 0.0, 0.0,"
for z in range(len(str4)):
    str1 = str1.replace(" ", "")

list3 = str4.split(",")
print(list3)
# adding f to end of each string in list
list4 = [item + 'f' for item in list3]
print(list4)

# remove quotes for copying directly:
str2 = str(list4)



for i in range(len(str2)):
     str2 = str2.replace("'", "")
     str2 = str2.replace('"', "")
print(str2)
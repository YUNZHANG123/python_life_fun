# Question:create a file and write a sentence on it using python
# content: "My name is Sophia and is 17 years old!"
# Purpose: practise the Python IO
# Sophia  20190914

# open the file
f_xu = open("xu.txt", "w")
print ("file name: ", f_xu.name)

# the content that will write in the document
f_xu.write ("My name is %s and is %d years old!" % ('Sophia', 17) )
# close the file
f_xu.close()

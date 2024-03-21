#/// Introduction to List////

marks = [3, 4, 5, "prasad", True, 12, 13, 14, 15,"karan", 23, 24, 45, 56, 57, 67, 78, 789]
print(marks)
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5])      # give Error  

print(marks[-3])                 #
print(marks[len(marks)-3])        #    All these give same output ,,we can write any of this..
print(marks[2])                   #
print(marks[5-3])                 #


if "prasad" in marks:
    print("yes")
else:
    print("no")

if 10 in marks:
    print("yes")
else:
    print("no")

if "sad" in "prasad":             #Same thing applies for string as well !
    print("yes")

print(marks)
print(marks[:])
print(marks[0:len(marks)])
print(marks[:8])
print(marks[1:8:3])                 #here 3rd value work as a gap (it also called jump index)
print(marks[1:6:2])

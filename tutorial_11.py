# /////Strings///////


name = "prasad"
apple = '''hi 
karan
how are you
i am fine
'''
sample = '''i am a good boy
whats about you
what are you doing

'''

print("Hello," +name)
print(apple)
print(name[0])    # p
print(name[1])     # locate that letter value     # r
print(name[2])      # a
print(name[3])       # s
print(name[4])        # a
print(name[5])          # d
# print(name[6])     # throws an error

print("Lets use a for loop\n")
for character in name :
    print(character)

for character in apple:
    print(character)

for character in sample:
     print(character)

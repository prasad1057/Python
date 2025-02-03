# ////  for loop with else loop ////



# for i in range(5):
#     print(i)
# else:
#     print("Sorry no i")

# for i in  []:
#     print(i)
# else:
#     print("Sorry no i")

# for i in range(6):
#     print(i)
#     if(i==4):
#         break                             #here for loop successfully completed therefore else dosent execute(break is used to break ot stop the loop)

# else:                                    #here else  dosent execute
#     ("Sorry no i")


i = 0
while i < 6:
    print(i)
    i = i + 1
    if(i == 4):
        break

else:
    print("Sorry no i")

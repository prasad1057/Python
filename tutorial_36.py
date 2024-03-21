# ////  Exception Handling ////


# a = input("Enter the number :")
# print(f"Multiplication table of {a} is : ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {int(i)} = {int(a) * i}")
# except:
#     print("Inavlid Input !")


a = input("Enter the number:")
print(f"Multiplication of table {a} is :")
try:
    for i in range(1,10):
        print(f"{int(a)} X {i} = {int(a) * i}")
        # if(i == 5):
        #     print("Half of table")
        #     continue
         
except:
    print("Something Wrong")
# # ////Functions////
# # when we create a  function then there is  " def " keyword is used


# a = 2
# b = 2
# gmean = (a*b)/(a+b)
# print("gmean is = ",gmean)


def calculateGmean (a , b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a , b):
    calculateGmean(a,b)
    if(a > b):
        print("First Number Is Greater")
    else:
         print("Second Number Is Greater or equal\n")

def isLesser(a , b):
    pass                    # when pass is used means go to next operation without doing this function but we will use later whenever is required  

a = 8
b = 10
isGreater(a,b)

c = 4
d = 3
isGreater(c,d)



# def isFruits(fruits):
#     for i in fruits:
#         print(i)
#         for j in i:
#             print(j)

# fruits = ["Mango", "Banana", "Kiwi"]
# isFruits(fruits)


# def isSum(price1, price2, price3):
#     add = price1 + price2 + price3
#     print(add)

# def isCheck(price1, price2, price3):
#     if(price1 == price2 == price3):
#         print("All prices are equals....")
#         if(price1 > price2):
#             print("Price1 is greater..")
#         else:
#             print("price2 is greater..")
#         if(price2 > price3):
#             print("price2 is greater..")
#         else:
#             print("price3 is greater..")
#     else:
#         print("All values are different..")
    

# price1 = 1000
# price2 = 2000
# price3 = 1500
# isSum(price1,price2,price3)
# isCheck(price1, price2, price3)







#/////// IfElse Conditional Statement///////


# Conditional Operator
#  >, <, <=, >=, ==, !=


num = int(input("Enter the value of num : "))
if(num < 0):
    print("Number is negative..")
elif(num == 0):
    print("Number is zero..")
elif(num == 999):
    print("Number is special..")
else:
    print("Number is positive..")

print("I am sad now.....")




num = 18
if(num < 0):
    print("Number is negative..")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1 to 10")
    elif(num > 10 and num <=20):
        print("Number is btween 10 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

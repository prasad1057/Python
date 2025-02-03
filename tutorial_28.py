# //// f string ///


letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Prasad"
# print(letter.format(name, country))
print(f"Hey my name is {name} and i am from {country}")
print(f"Hey my name is {{name}} and i am from {{country}}")


# string = "your name is {} and you are from {}"
# name = "karan"
# country = "England"
# # print(string.format(name,country))
# print(f"your name is {name} and you are from {country}")
# print(f"your name is {{name}} and you are from {{country}})



# apple = "you are in {} and you will get {} after compeltion of this.."
# std = "10th"
# cer = "certificate"
# print(apple.format(std,cer))
# print(f"you are in {std} and you will get {cer} after completion of this..")
# print(f"you are in {{std}} and you will get {{cer}} after completion of this..)

price = 12.09999
txt = f"For only {price:.2f} dollars!"                 # .2f --> it gives two numbers after the point of any number
print(txt)

value = 45.9453
txt = f"For only {value:.2f} cent!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))

print(f"{21 * 21}")


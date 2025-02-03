# /// Kaun banega Crorepati ///


questions = [
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
["Which language was used to create FB ?", "Python", "French", "JavaScript", "Php", "None", 4],
]

levels = [100,200,300,500,1000,2000,4000,8000,16000,32000]
money = 0

for i in range(0, len(questions)):
    que = questions [i]
    print(f"Questions for Rs.{levels[i]}")
    print(f"a. {que[1]}      b. {que[2]}")
    print(f"c. {que[3]}      d. {que[4]}")
    reply = int(input("ENter your answer (1-4) or 0 to quit"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == que[-1]):
        print(f"Correct answer , you have woon Rs. {levels[i]}")
        if(i == 4):
            money = 100
        elif(i ==9):
            money = 32000
        elif(i == 14):
            money = 100000
    else:
        print("Wrong Answer!!")
        break
print("Your take home money is {money}")

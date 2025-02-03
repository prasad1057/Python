# ////Break and Continue Statement///


# --- break = skip the loop
#  --- continue = skip the iteration


# for i in range(12):
#     if(i == 10):
#        print("how are u")
#        break
#     print("5 X", i + 1, "=", 5 * (i + 1))

# print("looop ko chodkar nikal jao....")


# for i in range(12):
#     if(i == 10):
#        print("skip the iteration")
#        continue
#     print("5 X", i , "=", 5 * i)

for i in range(10):
    if(i == 4):
        print("Skip the loop")
        break
    print( 10 * i)
    

for i in range(10):
    if(i == 4):
        print("Skip the iteration")
        continue
    print( 10 * i)


  

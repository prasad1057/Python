# //// Dictonaries In Python ////

# left_side = key
# right_side = value




# dic = {
#     "prasad": "Human Being",
#     "spoon": "object"
# }
# print(dic["prasad"])

# dic2 = {
#     "bolero" : "car",
#     "yamaha" : "bike",
#     "apple" : "fruit",
#     "rose" : "flower",
#     "lenovo" : "laptop"
# }
# print(dic2["apple"])
# print(dic2["rose"])

# dic3 = {
#     11 : "prasad",
#     567 : "karan", 
#     133: "om",
#     44 : "durvesh", 
#     100 : "vishal"
# }
# print(dic3[133])

# info ={"name":"karan","age":"20","eligible":True}
# print(info)
# print(info["name"])
# print(info.get("name"))
# print(info["age"])
# print(info.get("age"))
# print(info["eligible"])
# print(info.get("eligible"))

# # print(info.get("name2"))                     #when there is no related key in this , then it gives None answer(here name2 is not present)
# # print(info["name2"])                         #but here it directly throw an error


# info = {"name":"mango","color":"yellow","season":"summer","char":"fruit"}
# print(info)
# print(info["name"])
# print(info.get("name"))
# print(info["color"])
# print(info.get("color"))
# print(info["season"])
# print(info.get("season"))
# print(info["char"])
# print(info.get("char"))
    
# info = {"name":"karan","age":"20","eligible":"True"}
# print(info)
# print(info.keys())
# # print(info.values())

# for key in info.keys():
#     # print(info[key])
#     print(f"The value corresponding to the key {key} is {info[key]}")

info = {"name":"karan","age":"20","eligible":"True"}
print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {info[key]}")
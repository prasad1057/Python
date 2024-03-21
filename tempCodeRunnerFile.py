","age":"20","eligible":True}
print(info)
print(info["name"])
print(info.get("name"))
print(info["age"])
print(info.get("age"))
print(info["eligible"])
print(info.get("eligible"))

# print(info.get("name2"))                     #when there is no related key in this , then it gives None answer(here name2 is not present)
# print(info["name2"])    
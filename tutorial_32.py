# /// Set Methods ////


# intersection 
# intersection_update
# union 
# differnece

# disjoint                               #disjoint means fully two diffenent sets 
# issuperset
# issubset
# add
# remove / discard
# pop ()
# del





# s1 = {1,2,5,6}
# s2 = {3,6,7}
# # print(s1,s2)
# print(s1.union(s2))            #union = all elements
# print(s1.intersection(s2))
# # s1.update(s2)
# print(s1,s2)


# cities = {"alibag", "pen", "panvel", "thane", "satara", }
# cities2 = {"kolhapur", "alibag", "sangli", "pen"}

# print(cities,cities2)
# print(cities.intersection(cities2))
# print(cities.union(cities2))
# print(cities2.union(cities))
# cities.update(cities2)
# print(cities,cities2)
# print(cities)

# cities3 = cities.union(cities2)
# cities3 = cities.intersection(cities2)
# cities3 = cities.intersection_update(cities2)
# cities3 = cities.difference(cities2)
# print(cities3)


# cities = {"alibag", "pen", "panvel", "satara"}
# cities2 = {"alibag", "thane", "kolhapur", "nashik", "pen"}
# print(cities.isdisjoint(cities2))           #disjoint means fully two diffenent sets 

# cities = {"alibag", "pen", "panvel", "thane"}
# cities2 = {"pen", "thane"}
# print(cities.issuperset(cities2))
# cities3 = {"nashik", "satara"}
# print(cities.issuperset(cities3))

# cities = {"alibag", "pen", "panvel", "thane", "nashik", "satara", "kolhapur"}
# cities2 = {"pen", "thane"}
# print(cities2.issubset(cities))
# cities3 = {"nashik", "satara"}
# print(cities3.issubset(cities))

# cities = {"alibag", "pen", "panvel", "thane"}
# cities.add("solapur")
# print(cities)

# cities = {"alibag", "pen", "panvel", "thane"}
# cities.remove("pen")
# print(cities)

# cities = {"alibag", "pen", "panvel", "thane"}
# item = cities.pop()
# print(cities)
# print(item)

# cities = {"alibag", "pen", "panvel", "thane"}
# del cities
# print(cities)



games = {"kabaddi", "kho-kho", "cricket", "football", "vollyball", "hockey"}
print(games)

games = {"kabaddi", "kho-kho", "cricket", "football", "vollyball", "hockey"}
games2 = {"football", "kabaddi", "chess", "carrrom"}
print(games.isdisjoint(games2)) 

games = {"kabaddi", "kho-kho", "cricket", "football", "vollyball", "hockey"}
games2 = {"football", "cricket"}
print(games.issuperset(games2))

games = {"kabaddi", "kho-kho", "cricket", "football", "vollyball", "hockey"}
games2 = {"football", "cricket"}
print(games2.issubset(games))


games2 = {"football", "cricket"}
print(games2)
games2.add("basketball")
print(games2)

games2 = {"football", "cricket"}
item = games2.pop()
print(games2)
print(item)

games2 = {"football", "cricket", "basketball"}
games2.remove("basketball")
print(games2)

# games2 = {"football", "cricket"}
# del games2
# print(games2)

# dictionary
sports = {
    "cricket": "virat kohli",
    "football": "Ronaldo",
    "kabbaddi": "pawan sehrawath"
}
print(sports)
print(sports["cricket"])

print("add the famous volleyball player")
sports["volleyball"] = "Ivan Zaytsev"
print(sports)

sports["kabbaddi"] = "naveen express"
print(sports)                           #update the kabbaddi new famous player

sports.pop("football")
print(sports)

# dictionary methods
print(sports.keys())
print(sports.values())
print(sports.items())

item1 = {
    "name": "milk",
    "litre": 2,
    "price": 48
}

item2 = {
    "name": "water",
    "litre": 5,
    "price": 120
}

print(f"totoa price {item1["price"] + item2["price"]}")



#g.get(val) is used to get value accurate to key it has 2 tyoes dict[key] and dict.get[key]

hello={
    "name":"DOFFY",
    "anime":"One Piece",
    "bounty":9000000,
    22:"age"
}

print(hello["bounty"]) #1 type dict[key]

# print(hello["fruit"]) #1 type dict[key] but if the key does not exits it shows error and code stops
#print("End of code")

print(hello.get("fruit")) #2 type dict.get(key) but if the key does not exits it does not shows error and codes continues on
print("End of code")
#Dictionary are muttable means we can update it
#Dictionary uses Key value Pair i.e key:value pairs

hello={
    "name":"DOFFY",
    "anime":"One Piece",
    "bounty":9000000,
    22:"age"
}

hello["bounty"]=10000000
print(type(hello))
print(hello)
print(hello["bounty"])
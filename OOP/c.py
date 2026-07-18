info=[
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

dict={}

for name,course in info:
    if(dict.get(name)== None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
    
print(dict)
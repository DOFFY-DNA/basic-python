info=[
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

students=set()

for tup in info:
    if(tup[1]=="English"):
        students.add(tup[0]) #courses where 1 is the index number of course and 0 is name of person

print(students)
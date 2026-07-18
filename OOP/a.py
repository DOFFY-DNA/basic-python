info=[
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

courses_set=set()

for tup in info:
    courses_set.add(tup[1]) #courses where 1 is the index number of course and 0 is name of person

print(courses_set)
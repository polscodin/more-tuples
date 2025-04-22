# 

all_records = []

num_of_groups = 3

for i in range(num_of_groups):
    name        =    input("what is the name of the group?")
    people      =    input("how many people were there?")
    venue       =    input("where did the event taking place?")
    date        =    input("what was the date?(dd-mm-yyyy)")
    placement   =    input("what was their placement?")
    all_data    =    (name,people,venue,date,placement)
    all_records.append(all_data)
for i in all_records:
    print(i)

    
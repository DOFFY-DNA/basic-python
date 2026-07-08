#Continue is Used TO skip current Itreation...

i=1
while(i<=10):
    if(i % 3 == 0):
        i+=1
        continue

    print(i)
    i+=1

print("Outside the loop")
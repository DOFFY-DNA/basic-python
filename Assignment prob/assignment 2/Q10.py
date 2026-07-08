num=int(input("Enter The Number :"))

sec=int(50)

if(sec==num):
    print("You Have guessed Correct")
elif(sec<num):
    print("The Number guessed is Too High")
elif(sec>num):
    print("The Number guessed is Too Low")

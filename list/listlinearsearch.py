nums=[1,20,50,70,80,69]

x=70
idx=0

for val in nums:
    if(val==x):
        print(f"{x} found at idx={idx}") #This is String Interpolation
        break
    idx +=1
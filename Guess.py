import random
counter=1
MAX_NO_OF_ATTEMPTS=6
print("*************Start the game*************")
num = random.randrange(0,100)

while counter<=MAX_NO_OF_ATTEMPTS:
    num1 = int(input("Please enter any number between 0-100: "))
    if(num1==num):
        print("Congrats!!!You guessed it right in ",counter,"attempts!!!")
        break
    if(num1>num):
        print("Answer is less than your entered value !")
        counter=counter+1
    else:
        print("Answer is greater than your entered value !")
        counter=counter+1
        
        
else:
    print("Hard Luck!Try again")  
print("Finished!!")

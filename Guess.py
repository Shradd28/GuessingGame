import random
counter=1
MAX_NO_OF_ATTEMPTS=6
print("\t*************Start the game*************")
num = random.randrange(0,100)

while counter<=MAX_NO_OF_ATTEMPTS:
    num1 = int(input("Please enter any number between 0-100: "))
    if(num1==num):
        print("\t-----Congrats!!!You guessed it right in ",counter,"attempts!!!-----")
        break
    if(num1>num):
        print("\t-----Answer is less than your entered value-----")
        counter=counter+1
    else:
        print("\t-----Answer is greater than your entered value-----")
        counter=counter+1
        
        
else:
    print("\t-----Hard Luck!Try again-----")  
print("\t-----Finished!!-----")

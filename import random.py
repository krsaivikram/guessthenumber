import random
print("Number guessing game")

range=random.randint(1,9)
chance=0
while chance<3:
    enter=int(input("enter the number"))
    if enter==range:
        print("congratulations!")
        break
    elif enter<range:
        print("you chose a number less than it",enter)
    else:
        print("you chose a number greater then it",enter)
    chance+=1
if not chance<3:
    print("you lose, the number is ",range)                
    


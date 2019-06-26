import random


number = random.randint(1,200)
coinflip = random.randint(0,1)
result = 'heads' if coinflip == 0 else 'tails'
guess = 0


choice = input("Select 1 for higher/lower \nSelect 2 for heads/tails \nchoice: ")

if choice == '1':
    while guess != number:
        guess = int(input("enter a guess between 1 - 200\n"))
        if guess > number:
            print("lower\n")
        elif guess < number:
            print("higher\n")
        elif guess == number:
            print("congratulations you've found the number")

elif choice == '2':
    print(result)



    
        
        
    
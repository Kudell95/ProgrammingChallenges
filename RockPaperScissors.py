import random

def main():
    option_list = {'rock': 1, 'paper': 2, 'scissors': 3, 'scissor': 3, '1':1, '2': 2, '3':3}
    userIn = input('make your guess: ')
    userVal = option_list[userIn]
    computer = random.randint(1,3)
    print("user value: ", userVal)
    print("computer value", computer)

    if computer % 3 + 1 == userVal:
        print("you win")
    elif userVal % 3 + 1 == computer:
        print('you lose')
    else:
        print('draw')


main()
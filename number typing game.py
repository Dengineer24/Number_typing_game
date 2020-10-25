import sys
import time
import random

start = input('''Press [ENTER] to start the game or type "Exit" to end game.
 > ''')
if start.lower() == "exit":
    print('Exiting game...')
    time.sleep(1)
    sys.exit()
else:
    print('''directions: 
    You will see a list of random numbers in ().
    Type the numbers out on the screen, type it out faster then the opponent to win.
    EACH WRONG ANSWER ADDS 1 SECOND''')
    input('Player 1: Press [ENTER] to start timer:')
while True:
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    num3 = random.randint(0,100)
    num4 = random.randint(0,100)
    num5 = random.randint(0,100)
    t0 = time.time()
    try:
        there_choice1 = input(f'({num1}) type in the number (int only): ')
        if int(there_choice1) == num1:
            print('Correct!')
            wrong1 = 0
        else:
            print('wrong!')
            wrong1 = 1
        there_choice2 = ""
        there_choice2 = input(f'({num2}) type in the number (int only): ')
        if int(there_choice2) == num2:
            print('Correct!')
            wrong2 = 0
        else:
            print('wrong!')
            wrong2 = 1
        there_choice3 = ""
        there_choice3 = input(f'({num3}) type in the number (int only): ')
        if int(there_choice3) == num3:
            print('Correct!')
            wrong3 = 0
        else:
            print('wrong!')
            wrong3 = 1
        there_choice4 = ""
        there_choice4 = input(f'({num4}) type in the number (int only): ')
        if int(there_choice4) == num4:
            print('Correct!')
            wrong4 = 0
        else:
            print('wrong!')
            wrong4 = 1
        there_choice5 = ""
        there_choice5 = input(f'({num5}) type in the number (int only): ')
        if int(there_choice5) == num5:
            print('Correct!')
            wrong5 = 0
        else:
            print('Wrong!')
            wrong5 = 1
        t1 = time.time()
        total = (t1-t0) + wrong1 + wrong2 + wrong3 + wrong4 + wrong5
        print(f'Player 1 took {total} seconds')
    except ValueError:
        print('''Numerical values only! 
Turn was lost.''')
        p1_lose = str('player 1 lost')
    break
input('Player 2: Press [ENTER] to start timer:')
while True:                                        # next set of random numbers for player 2
    num6 = random.randint(0,100)
    num7 = random.randint(0,100)
    num8 = random.randint(0,100)
    num9 = random.randint(0,100)
    num10 = random.randint(0,100)
    t0 = time.time()
    try:
        there_choice6 = input(f'({num6}) type in the number (int only): ')
        if int(there_choice6) == num6:
            print('Correct!')
            wrong6 = 0
        else:
            print('wrong!')
            wrong6 = 1
        there_choice7 = ""
        there_choice7 = input(f'({num7}) type in the number (int only): ')
        if int(there_choice7) == num7:
            print('Correct!')
            wrong7 = 0
        else:
            print('wrong!')
            wrong7 = 1
        there_choice8 = ""
        there_choice8 = input(f'({num8}) type in the number (int only): ')
        if int(there_choice8) == num8:
            print('Correct!')
            wrong8 = 0
        else:
            print('wrong!')
            wrong8 = 1
        there_choice9 = ""
        there_choice9 = input(f'({num9}) type in the number (int only): ')
        if int(there_choice9) == num9:
            print('Correct!')
            wrong9 = 0
        else:
            print('wrong!')
            wrong9 = 1
        there_choice10 = ""
        there_choice10 = input(f'({num10}) type in the number (int only): ')
        if int(there_choice10) == num10:
            print('Correct!')
            wrong10 = 0
        else:
            print('wrong!')
            wrong10 = 1
        t1 = time.time()
        total2 = (t1 - t0) + wrong6 + wrong7 + wrong8 + wrong9 + wrong10
        print(f'Player 2 took {total2} seconds')
    except NameError:
        print(' ')
    except ValueError:
        print('''Numerical values only!
Turn was lost.''')
        p2_lose = str('player 2 lost')
    break
try:
    winner = total2 - total
    if winner < 0:
        print("Player 2 won!")
    else:
        print('Player 1 won!')
except NameError:
    try:
        print(p1_lose)
        print(p2_lose)
    except NameError:
        print("")

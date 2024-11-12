import random

p1_name = input("What's your name: ")
p2_name = input("What's your opponent's name: ")

p1_count = 0
p2_count = 0
draw_count = 0

while True:
    input(f'{p1_name}, press enter to roll')
    player1 = random.randint(1,6)
    print(f'{p1_name} rolled: {player1}')

    input(f'{p2_name}, press enter to roll')
    player2 = random.randint(1,6)
    print(f'{p2_name} rolled: {player2}')

    if player1 > player2:
        print(f'{p1_name} won with {player1}, while {p2_name} had {player2}')
        p1_count += 1
    elif player1 < player2:
        print(f'{p2_name} won with {player2}, while {p1_name} had {player1}')
        p2_count += 1
    else:
        print(f'Draw, because {p1_name} and {p2_name} had {player1}')
        draw_count += 1

    print(f'Overall {p1_name} score is {p1_count}, overall {p2_name} score is {p2_count}, amount of draws is {draw_count}')
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
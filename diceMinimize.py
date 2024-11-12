import random
p1_name, p2_name = input("Player 1 name: "), input("Player 2 name: ")
p1_count = p2_count = draw_count = 0
while True:
    player1, player2 = random.randint(1,6), random.randint(1,6)
    print(f'{p1_name} rolled: {player1}\n{p2_name} rolled: {player2}')
    
    if player1 > player2: p1_count += 1; print(f'{p1_name} wins!')
    elif player1 < player2: p2_count += 1; print(f'{p2_name} wins!')
    else: draw_count += 1; print('Draw!')
    
    print(f'Scores - {p1_name}: {p1_count}, {p2_name}: {p2_count}, Draws: {draw_count}')
    if input("Play again? (yes/no): ").lower() != 'yes': break
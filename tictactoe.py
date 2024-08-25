# Initialize the game board
field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Initialize the current player (1 for 'x' and 0 for 'o')
current_player = 1

def draw(field):
    """Print the current state of the game board."""
    print(f"{field[0]} {field[1]} {field[2]}")
    print(f"{field[3]} {field[4]} {field[5]}")
    print(f"{field[6]} {field[7]} {field[8]}")
    print()

def endgame(field, player):
    """Declare the winner and end the game."""
    draw(field)
    print(f"Player {player.upper()} wins!")
    exit()

def check(field):
    """Check if any player has won the game."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    players = ['x', 'o']
    
    for player in players:
        for combo in winning_combinations:
            if all(field[i] == player for i in combo):
                endgame(field, player)

def get_input():
    """Get the current player's move."""
    while True:
        try:
            x = int(input(f"Player {current_player} ({'x' if current_player == 1 else 'o'}), choose a position (1-9): "))
            if 1 <= x <= 9 and field[x-1] not in ['x', 'o']:
                return x
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def switch_player():
    """Switch the current player after a move."""
    global current_player
    if current_player == 1:
        field[x-1] = 'x'
        current_player = 0
    else:
        field[x-1] = 'o'
        current_player = 1

# Draw the initial game board
draw(field)

# Main game loop
while True:
    x = get_input()
    switch_player()
    check(field)
    draw(field)

from tkinter import *
from tkinter import simpledialog, messagebox
from functools import partial 

# Initialize the main window
main = Tk()
main.geometry("250x250")
main.title("Tic Tac Toe")

# Initialize the game board and player
field = [' ' for _ in range(9)]
current_player = 1
buttons = []

def btn_click(index):
    """Handle button click events."""
    global current_player

    if field[index] == ' ':
        if current_player == 1:
            buttons[index]["text"] = 'x'
            field[index] = 'x'
            current_player = 0
        else:
            buttons[index]["text"] = 'o'
            field[index] = 'o'
            current_player = 1
        
        check_win()

def endgame(player):
    """End the game and announce the winner."""
    messagebox.showinfo("Winner", f"Player {player.upper()} wins!")
    main.quit()

def check_win():
    """Check if there is a winner or if the game is a draw."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for player in ['x', 'o']:
        for combo in winning_combinations:
            if all(field[i] == player for i in combo):
                endgame(player)

    if ' ' not in field:
        messagebox.showinfo("Draw", "It's a draw!")
        main.quit()

# Create and place buttons on the grid
frame = Frame(main)
frame.pack(fill="both")

for index in range(9):
    b = Button(frame, text=field[index], command=partial(btn_click, index), width=6, height=4)
    b.grid(row=index // 3, column=index % 3)
    buttons.append(b)

# Start the Tkinter main loop
main.mainloop()

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]
]

print(board[0][0])
print(board[1][1])
print(board[2][2])
    
current_player = "X"
moves = 0


while True:
    
    for index, row in enumerate(board):
        print("  |  ".join(row))
        
        if index < 2:
            print("---+---+---")
    
    
    row = int(input("row(1-3): "))
    column = int(input("column(1-3): "))
    
    if 0 <= row <= 2 and 0 <= column <= 2:
        ("Invalid Position! choose between 1 to 3")
    
    row -= 1
    column -= 1
    
    if board[row][column] == "":
        board[row][column] = current_player
        moves += 1
        
    else:
        print("Position already occupied")
        
    if board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break
    elif board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break
    elif board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break
    
    elif board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break  
 
    elif board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break    
    elif board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break    
    elif board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break 
    elif board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        print("\nPlayer", current_player, "Wins!")
        break
        
        if moves == 9:
            print("Its draw!!")
            break
    if current_player == "X":
        current_player = "O"
    
    else:
        current_player = "X"
    

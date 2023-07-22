#!/usr/bin/env python3
"""connect_four.py"""

# This code displays the winner of a connect four game.
# Code is modified from that given by Dr. David Biersach in connect_four.py

# Code for check_horizontal, check_vertical, and check_diagonals was aided by the
# following online resources:
# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical#:~:text=if%20len(set(input_list)),input_list%20has%20all%20identical%20elements.
# https://www.techbeamers.com/program-python-list-contains-elements/
# https://www.geeksforgeeks.org/python-test-if-all-elements-are-present-in-list/
# Code for check_winner was aided by: https://openai.com/blog/chatgpt.


# fmt: off


def check_winner(board: list[list[int]]) -> int:
    """Defines the function to check the winner of the connect four game as 
    a function of the list 'board'"""
    # Initialize the no_winner output as equal to 0
    no_winner: int = 0
    
    # Create the winner variable and initialize it at 0
    winner: int = 0
    
    # Run the check_horizontal function and set the output equal to its result.
    winner = check_horizontal(board)
    
    # If winner does not equal 0
    if winner:
        # Return the player number of the winner of the game.
        return winner
    # Runs the check_vertical code for the list 'board' and 
    # sets output equal to its result.
    winner = check_vertical(board)
    
    # If winner does not equal 0
    if winner:
        # Return the player number of the winner of the game.
        return winner
    # Runs the check_diagonals code for the list 'board' and 
    # sets output equal to its result.
    winner = check_diagonals(board)
    
    # If winner does not equal 0
    if winner:
        # Return the player number of the winner of the game.
        return winner
    # If no winner has been found, return 0
    return no_winner




def check_horizontal(board: list[list[int]]) -> int:
    """check_horizontal is a function of the list 'board' and its output 
    is equal to an integer."""
    no_winner: int = 0
    # For the rows in the connect 4 board (each item in board 
        # represented by'horizontal')
    for horizontal in board:
        # Check each indices in each row, len(horizontal)-3 makes sure 
            # that the loop runs within the boundaries of the row length
        for vertical in range(len(horizontal)-3): 
            # check_horizontal is a list equal to 4 equal, successive 
            # integers within a row
            check_horizontal: list[int] = [
                horizontal[vertical], horizontal[vertical + 1], 
                horizontal[vertical + 2], horizontal[vertical + 3]
                ]
            
            # Sees if all items in check_horizontal are equal to
              # horizontal[vertical]
            check: bool = all(item == horizontal[vertical] and item !=0 
                              for item in check_horizontal)
            # If check_horizontal is in a row
            if check:
                 # Return the first value in the row with the 
               #  connect four (winner number)
                return horizontal[vertical]
       # Return 0 if there is no horizontal winner      
    return no_winner
   

def check_vertical(board: list[list[int]]) -> int:
    """check_vertical is a function of the list 'board' and its output is 
    equal to an integer."""
    no_winner: int = 0
    # Each column value is in a range the length of board
    for vertical in range(len(board)):
        # For each row in the range of the length of board- 3 
            # (to keep the for loop in its boundaries)
        for horizontal in range(len(board) - 3):
           # List equal to 4 equal, successive items in board 
            # that have the same index.
            check_vertical: list[int] = [
                board[horizontal][vertical],
                board[horizontal+1][vertical],
                board[horizontal+2][vertical],
                board[horizontal+3][vertical]
            ]
            
            #  Checks if the item is equal to the first item in the check_vertical list 
            # and not equal to 0
            check: bool = all(item == check_vertical[0] and item != 0 
                              for item in check_vertical)
            
            if check:
                # Returns the first value in the column 
            # with the connect four (winner number)
                return check_vertical[0]
    # Returns 0 if there is no vertical winner      
    return no_winner


def check_diagonals(board: list[list[int]]) -> int:
    no_winner: int = 0
    # Checking diagonal to the right
    # For each row in the range of the length of board- 3 
        # (to keep the for loop in its boundaries)
    for horizontal in range(len(board) - 3):
         # Returns the range of the first sublist of board to get the number of 
            # columns and subtract 3 to stay within the boundaries of the board. 
            # Vertical represents the indices in the range (aka columns of board)
        for vertical in range(len(board[0]) - 3):
           
           # List of items that are diagonally across 
            # from each other in a positive slope.
            check_diagonals: list[int] = [
                board[horizontal][vertical],
                board[horizontal + 1][vertical + 1],
                board[horizontal + 2][vertical + 2],
                board[horizontal + 3][vertical + 3]
            ]
            # Checks is all elements in check_diagonals are equal to its 
                # first element and are not equal to 0
            if all(item == check_diagonals[0] and item != 0 for item in check_diagonals):
                # Returns the first value of the diagonal with the connect four
                return check_diagonals[0]
            

    # Check diagonal to the left
    for horizontal in range(len(board) - 3):
        # Range starts at 3 and ends at len(board)-3 so we can stay within the 
            # range of columns
        for vertical in range(3, len(board[0])):
            # List of items that are diagonally across from each other 
            # with a negative slope.
            check_diagonals = [
                board[horizontal][vertical],
                board[horizontal + 1][vertical - 1],
                board[horizontal + 2][vertical - 2],
                board[horizontal + 3][vertical - 3]
            ]
            #Checks is all elements in check_diagonals are equal to its first
                # element and are not equal to 0
            if all(item == check_diagonals[0] and item != 0 for item in check_diagonals):
                # Returns the first value of the diagonal with the connect four
                return check_diagonals[0]
            
# Returns 0 if there is no diagonal winner 
    return no_winner





def print_winner(board: list[list[int]]) -> None:
    """Defines the function to print the winner of connect 4"""
    # Unpacking the board list and passing it through a 
    # print function with separate lines
    # print every row 
    print(*board, sep="\n")
    
    # Return the value of check_winner
    winner: int = check_winner(board)
    
    # If winner does not equal 0 and satisfies one of the check function above
    if winner:
        
        print(f"Winner is Player {winner}")
        print()
    else:
        # Winner either does equal 0 or does not satisfy the above functions
        print("No winner")
        print()


def main() -> None:
    """Defines an entry point for the function"""
    # Creating the game boards

    # Creating board 1 and calling the print winner function 
    # to see if there is a winner
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)
    
    # Creating board 2 and calling the print winner function 
    # to see if there is a winner
    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)
   
    # Creating board 3 and calling the print winner function 
    # to see if there is a winner
    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 0, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)
    

if __name__ == "__main__":
    """Calls the main function """
    main()

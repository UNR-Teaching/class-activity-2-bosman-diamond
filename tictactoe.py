""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['.' for _ in range(3)] for _ in range(3)]
        self.size = 3
        self.winner = 'None'

	
    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player
        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square
        :return: ????
        """
        if self.board[row][column] != '.':
            raise Exception('Coordinate not available!')
        if row < self.size and column < self.size and row >= 0 and column >= 0:
            self.board[row][column] = player
            print("Player", player, " placed at column ", column, " row ", row)
        else:
            print('Coordinate out of bounds!')
		

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """


        """
        check all rows
        """
        
       

        for row in range(2):
            if row != 0 and collision == False:
                print(current_val)

            collision = False

            for col in range(1):
                current_val = self.board[row][col]
                if current_val != self.board[row][col + 1]:
                    collision = true

        if collision == False:
            print(current_val)

        
        """
        check all columns
        """
        
        collision = False
        for row in range(1):
            if row != 0 and collision == False:
                print(current_val)
            collision = False

            for col in range(2):
                current_val = self.board[row][col]
                if current_val != self.board[row + 1][col]:
                    collision = True

        if collision == False:
            print(current_val)

        if collision == True:
            return "no"
        
	    

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        valid_coords = (1, 2, 3)

        while not self.has_winner():
            move = input("Give your move (r, c, player)")
            move = move.split(',')
            for i, value in enumerate(move):
                temp_value = value.strip()
                move[i] = temp_value

            for value in move:
                if not value.isalnum():
                    print("Value must be alphanumeric")
                    break

            if len(move) != 3:
                print("Please give three values")
                continue
            '''if not int(move[0]) not in valid_coords or int(move[1]) not in valid_coords:
            print('Coordinates must be integers from 0-2')
            continue'''
            move[0] = int(move[0])
            move[1] = int(move[1])
            self.mark_square(move[0], move[1], move[2])

        return self.has_winner()
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))

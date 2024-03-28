# # user is 'O'
# # computer is 'x'
#
# # mat_ij = [
# #     [(0, 0), (0, 1), (0, 2),],
# #     [(1, 0), (1, 1), (1, 2),],
# #     [(2, 0), (2, 1), (2, 2),]
# # ]
# #
# # board = mat_ij
# # for row in board:
# #     for element in row:
# #         print('example1: ', element)
#
# # ## 3x3 Matrix below
# # board = [[0, 1, 2],
# #         [3, 4, 5],
# #         [6, 7, 8]]
# #
# # def convert_int_to_ij(number):
# #     i = number // 3
# #     j = number % 3
# #     return (i, j)
# #
# # print(convert_int_to_ij(6))
#
# ## 3x3 Matrix below
# # board = [[1, 2, 3],
# #         [4, 5, 6],
# #         [7, 8, 9]]
# #
# # board[0][0] = 'X'
# # board[1][1] = 'O'
# # # [print(a) for a in board]
# # div = '_'
# # for i in board:
# #         print(*i, sep='|')
# #
# # # create a function that displays the board after each player has had a turn
# # for i in board:
# #         print(*i, sep='|')
# # create a function that takes input, such a number from the grid as the place they want
# # to put their x. Then display that by showing the rendered version replacing the number with the x
# # start app
# # show board
# # prompt for user input
# # check that is valid
# # apply user input
# # check for win condition on state change
# # show updated board
# # random cpu choice
# # check that it is valid
# # check for win condition on state change
# # show updated board
import random

class TicTacToe:

    def __init__(self):
        self.board = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
        self.x_player = []
        self.comp_player = []

    def prompt_usr(self):
        self.displayBoard()  # To prompt the user, we first want to show them the board
        prompt = int(input("Where do you want to put your 'X'?: "))
        # while True:
        if prompt in range(9):  # check that input is valid, i.e. valid number in grid
            # apply user input to update board
            self.convert_int_to_ij(prompt)

    # helper function to convert int to (i, j)
    def convert_int_to_ij(self, number):
        self.i = number // 3
        self.j = number % 3
        return self.updateBoard(self.i, self.j)

    def updateBoard(self, val1, val2):
        # if True:
        hu = [val1, val2]
        if hu not in self.comp_player:
            self.x_player.append([val1, val2])
            self.board[val1][val2] = 'X'
        else:
            self.prompt_usr()
        print("Human list:", self.x_player)
        return self.winCondition('human')

    def cpu_move(self):
        # Generate random input to run through the converter based on list values not 'X'
        y = random.sample(range(0, 3), 2)
        if y not in self.x_player and y not in self.comp_player:
            self.comp_player.append(y)
            val1 = y[0]
            val2 = y[1]
            self.board[val1][val2] = 'O'
        else:
            self.cpu_move()
        print("CPU list:", self.comp_player)
        return self.winCondition('cpu')

    def winCondition(self, player=None):
        if player == 'human':
            if self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
                self.displayBoard()
                print("You Win!")
            elif self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
                self.displayBoard()
                print("You Win!")
            else:
                return self.cpu_move()

        elif player == 'cpu':
            if self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            elif self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
                self.displayBoard()
                print("Computer Wins!")
            else:
                return self.prompt_usr()


    def displayBoard(self):
        for grid in self.board:
            print(*grid, sep='|')
        return self.board


ttt = TicTacToe()
# # ttt.displayBoard()
ttt.prompt_usr()
# ttt.convert_int_to_ij(1)


# mat_ij = [
#     [(0, 0), (0, 1), (0, 2)],
#     [(1, 0), (1, 1), (1, 2)],
#     [(2, 0), (2, 1), (2, 2)]
# ]
# mat_ij[val1][val2] = ('X')
# print(mat_ij[val1][val2])
#
# board = mat_ij
# for row in board:
#     for element in row:
#         print('example1: ', element)

#                 # example: board[0][0] = 'X'
#                 a = self.board[0][0]
#                 b = self.board[0][1]
#                 c = self.board[0][2]
#                 d = self.board[1][0]
#                 e = self.board[1][1]
#                 f = self.board[1][2]
#                 g = self.board[2][0]
#                 h = self.board[2][1]
#                 j = self.board[2][2]

# for _ in self.x_player:
#     k = _[0]
#     m = _[1]
#     if self.board[k][m] == 'X':
#         print("yay!")
#     else:
#         print("Wah!")
# return self.prompt_usr()
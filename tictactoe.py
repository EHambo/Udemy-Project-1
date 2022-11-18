

import random

def display_board(board):
    print('\n'*20) #clears the board
    boardvar=f'    {board.get(1)}|{board.get(2)}|{board.get(3)}\n\
    {board.get(4)}|{board.get(5)}|{board.get(6)}\n\
    {board.get(7)}|{board.get(8)}|{board.get(9)}'
    print(boardvar)

def player_input():

    player1=None

    while player1 not in ['X','O']:
        player1 = input("Please pick a marker 'X' or 'O'")

        if player1 not in ['X','O']:
            print("Invalid Choice. Please Choose Again!")
    return player1

def place_marker(board, marker, position):

    board[int(position)] = marker
    return board

def win_check(board, mark):

    winner = False

    if (board[1] == mark and board[2] == mark and board[3] == mark) or \
       (board[4] == mark and board[5] == mark and board[6] == mark) or \
       (board[7] == mark and board[8] == mark and board[9] == mark) or \
       (board[1] == mark and board[4] == mark and board[7] == mark) or \
       (board[2] == mark and board[5] == mark and board[8] == mark) or \
       (board[3] == mark and board[6] == mark and board[9] == mark) or \
       (board[1] == mark and board[5] == mark and board[9] == mark) or \
       (board[3] == mark and board[5] == mark and board[7] == mark):
        #print('winner!')
        winner = True
        winner = True
    return winner

def choose_first():

    #if even, True maybe make this player 1?
    starting_player=random.randint(1, 10)
    return  starting_player % 2 == 0

def space_check(board, position):
    #is the space empty?
    return board[position] == ''

def full_board_check(board):
    full_check = False
    if '_' not in board.values():
        full_check = True
    return full_check

def player_choice(board):
    #Asks user choice, confirms choice is valid, checks if spot taken,
    #returns the position they chose.

    inputval=None
    empty_ = True
    while inputval not in range(1,10) or empty_ == False:
        try:
            inputval = int(input('Enter the position you want to play (1-9).'))
            empty_ = space_check(testboard, inputval)
            if empty_ == False:
                print('Spot already taken, Choose again.')
        except:
            print('Invalid Input. Choose a number between (1 and 9)')
    return inputval

def replay():

    again_= None
    playagain = True
    while again_ not in ['Y','N']:
        again_ = input("Would you like to play Again? \n \
        Yes: 'Y' No: 'N' ")

        if again_ not in ['Y','N']:
            print("Invalid Choice. Please Choose Again!")
    if again_ == 'N':
        playagain = False
    return playagain

#-----------------------------Start of program----------------------------------------
def main():

    print('Welcome to Tic Tac Toe!\n')

    playagain_ = True

    while playagain_ is True: #outer loop to allow user to replay

        testboard = {1 :'_', 2 : '_',3 :'_', 4 : '_',5 :'_', 6 : '_',7 :'_', \
        8 : '_', 9 : '_'}
        firstpl = None
        secondpl = None
        firstpl_piece = ''
        secondpl_piece = ''
        mark_ = 'z'
        playagain_ = True

        #------------------------------------------Logic to Choose player.
        if choose_first() == True:
            firstpl = 1
            secondpl= 2
        else:
            firstpl = 2
            secondpl= 1

        print(f'Player {firstpl} goes 1st\n')
        choice_ = player_input()
        print(f'Player {firstpl} goes 1st and chooses {choice_}.\n')

        firstpl_piece = choice_
        if choice_ == 'X':
            secondpl_piece = 'O'
        else:
            secondpl_piece = 'X'

        termination1 = False
        termination2 = False
        while True:
                    #--------------------------------------------Game Begins
            termination1 = full_board_check(testboard)
            if termination1 == True:
                print('Game ends in a Draw!')
                break
                        ############### Player 1 ###############
            mark_ = firstpl_piece
            print(f'Player {firstpl} choose a position. You are letter: {firstpl_piece}')
            testboard = place_marker(testboard,firstpl_piece,player_choice(testboard))
            termination1 = full_board_check(testboard)
            if termination1 == True:
                print('Game ends in a Draw!')
                break

            display_board(testboard)

            termination2 = win_check(testboard, mark_)

            if termination2 == True:
                print(f'Player {firstpl} Wins! ')
                break
                        ############### Player 2 ###############
            mark_ = secondpl_piece
            print(f'Player {secondpl} choose a position. You are letter:{secondpl_piece}')
            testboard = place_marker(testboard,secondpl_piece,player_choice(testboard))
            termination1 = full_board_check(testboard)
            if termination1 == True:
                print('Game ends in a Draw!')
                break
            display_board(testboard)

            termination2 = win_check(testboard, mark_)
            if termination2 == True:
                print(f'Player {secondpl} Wins! ')
                break

        playagain_=replay()

main()

#a project for later could be migrate this to connect four.
#some junk code if i want to remove hardcoded win check.
#this is useful for connect four but probably not needed for this application
'''
def win_check(board, mark):

    winner = False
    if board[1] or board[2] or board[3] == mark:
        if board[1] and board[2] or board[3] == mark:
            winner = True
        elif board[mark] and board[mark+3] and board[mark+6]:
            winner = True
    elif board[4] or board[7] == mark:
        if board[mark] and board[mark+1] and board[mark+2] == mark:
            winner = True
    elif board[1] or board[3] == mark:
        if board[mark] and board[mark+4] and mark[mark+8]
'''

'''
Tic-Tac-Toe: activity
Author: Karebwa.Tebano
'''

play_board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' ',}

create_board = []

for i in play_board:
    create_board.append(i)
    
def display_board(board):
    print(board['1'] +'|'+ board['2'] +'|' + board['3'])
    print('-----')
    print(board['4'] +'|'+ board['5'] +'|'+ board['6'])
    print('-----')
    print(board['7'] +'|'+ board['8'] +'|'+ board['9'])

def main():
    
    player_1 = 'x'
    player_2 = 0


    for i in range(10):
        display_board(play_board)
        print( f'{player_1} ' 'make a move!')
        
        init_move = input()
        
        if play_board[init_move] == ' ':
            play_board[init_move] = player_1
            player_2 += 1
        
        else:
            print('alredy taken choose another number.')
            continue
        
        if player_2 >= 5:
            if play_board['1'] == play_board['2'] == play_board['3'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
            elif play_board['4'] == play_board['5'] == play_board['6'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                
                break
            elif play_board['7'] == play_board['8'] == play_board['9'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
            elif play_board['2'] == play_board['5'] == play_board['8'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
            elif play_board['1'] == play_board['4'] == play_board['7'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
            elif play_board['3'] == play_board['6'] == play_board['9'] != '':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
            elif play_board['1'] == play_board['5'] == play_board['9'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
            elif play_board['7'] == play_board['5'] == play_board['3'] != ' ':
                display_board(play_board)
                print('Good game')
                print(f'{player_1} wins')
                break
        if player_2 == 9:
            print('Good game')
            print('It is a tie!')
        if player_1 == 'x':
            player_1 ='o'
        else:
            player_1 = 'x'
            
    start_over = input('Do you wish to play again?(y/n)')
    if start_over.upper() == 'y':
        for i in create_board:
            play_board[i] = ''
        
         
            
if __name__=='__main__':
    main()
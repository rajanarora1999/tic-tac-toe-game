import os
def display_board(board):
    print(" ",board[0], " | ",board[1]," | ",board[2])
    print("-----------------")
    print(" ",board[3], " | ",board[4]," | ",board[5])
    print("-----------------")
    print(" ",board[6], " | ",board[7]," | ",board[8])
def win(board,choice):
        if board[0]==board[1] and board[1]==board[2] and (choice==1 or choice==2 or choice==3):
            return True
        elif board[3]==board[4] and board[4]==board[5] and (choice==4 or choice==5 or choice==6):
            return True
        elif board[6]==board[7] and board[7]==board[8] and (choice==7 or choice==8 or choice==9):
            return True
        elif board[0]==board[3] and board[3]==board[6] and (choice==1 or choice==4 or choice==7) :
            return True
        elif board[1]==board[4] and board[4]==board[7] and (choice==2 or choice==5 or choice==8) :
            return True
        elif board[2]==board[5] and board[5]==board[8] and (choice==3 or choice==6 or choice==9) :
            return True
        elif board[0]==board[4] and board[4]==board[8] and (choice==1 or choice==5 or choice==9):
            return True
        elif board[2]==board[4] and board[4]==board[6] and (choice==3 or choice==5 or choice==7):
            return True
        else :
            return False
if __name__=='__main__' :
    print("Hi welcome to tic tac toe!")
    while True :
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        p1=input("Enter the name of player 1 = ")
        p2=input("Enter the name of player 2 = ")
        i=0
        display_board(board)
        while True :
            if i%2==0:
                print(p1,end=' ')
                print("enter your choice(1-9)=",end=' ')
                choice=int(input())
                board[choice-1]='X'
                os.system('cls' if os.name == 'nt' else 'clear')
                display_board(board)
                if win(board,choice) :
                    print(p1, "wins")
                    break
            else :
                print(p2,end=' ')
                print("enter your choice(1-9)=",end=' ')
                choice=int(input())
                board[choice-1]='O'
                os.system('cls' if os.name == 'nt' else 'clear')
                display_board(board)
                if win(board,choice) :
                    print(p2, "wins")
                    break
            i+=1
        
        rest=input('restart game(y/n)=')
        os.system('cls' if os.name == 'nt' else 'clear')
        if rest=='n' :
            break
    print('Thanks for playing the game')
#!/usr/bin/env python
# coding: utf-8

# In[4]:


from IPython.display import clear_output
from random import randint
import time

def display_board(board):
    # Clears the board
    clear_output()
    # Prints Current Board Layout
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])
   
    
    
def position_choice_1(board,name):
    choice = 'Wrong'
    # Variables
    # Initial non-digit choice
    choice = 'Not Digit'
    # Acceptable range
    acceptable_values = range(1,10)
    # Initial range condition
    within_range = False
    # Initial taken condition
    Taken = True


    while choice.isdigit() == False or within_range == False or Taken==True:
    
        choice = input(f"{name}, Please select the position you want to make your placement at (1-9): ")
        
        # Digit Check
        if choice.isdigit() == False:
            print('Sorry, that is not a digit!\nPlease Try Again :)')
            
        # Range Check
        if choice.isdigit()==True:
            if int(choice) in acceptable_values:
                within_range=True
            else:
                print('Sorry, that number is not within the acceptable range (1-9)!\nPlease Try Again :)')
                within_range = False # Not Necessary, but helps with readability
                
        # Taken Check
        if choice.isdigit()==True:
            if int(choice) in acceptable_values:
                if Taken==True:
                    if board[int(choice)]=='X' or board[int(choice)]=='O':
                        print('That position has already been taken!\nPlease Try Again :)')
                        Taken = True
                    else:
                        Taken = False
                
    return int(choice)

def position_choice_2(board,name):
    choice = 'Wrong'
    # Variables
    # Initial non-digit choice
    choice = 'Not Digit'
    # Acceptable range
    acceptable_values = range(1,10)
    # Initial range condition
    within_range = False
    # Initial taken condition
    Taken = True


    while choice.isdigit() == False or within_range == False or Taken == True:
    
        choice = input(f"{name}, Please select the position you want to make your placement at (1-9): ")
        
        # Digit Check
        if choice.isdigit() == False:
            print('Sorry, that is not a digit!\nPlease Try Again :)')
            
        # Range Check
        if choice.isdigit()==True:
            if int(choice) in acceptable_values:
                within_range=True
            else:
                print('Sorry, that number is not within the acceptable range (1-9)!\nPlease Try Again :)')
                within_range = False # Not Necessary, but helps with readability
                
        # Taken Check
        if choice.isdigit()==True:
            if int(choice) in acceptable_values:
                if Taken==True:
                    if board[int(choice)]=='X' or board[int(choice)]=='O':
                        print('That position has already been taken!\nPlease Try Again :)')
                        Taken = True
                    else:
                        Taken = False
                
    return int(choice)

    
def player_order(name1,name2):
    
    # Random number generator
    randomnumber = randint(0,100)
    # Initial player guesses
    number1 = 'Guess'
    number2 = 'Guess'
    # Acceptable range
    acceptable_values = range(0,101)
    # Initial range condition
    initial_range1 = False
    initial_range2 = False

    
    while number1.isdigit() == False or initial_range1 == False:
        
        number1 = input(f"{name1}, Please select your guess (0-100): ")
        
        # Digit Check
        if number1.isdigit() == False:
            print('Sorry, that is not a digit!\nPlease Try Again :)')
            
        # Range Check
        if number1.isdigit()== True:
            if int(number1) in acceptable_values:
                initial_range1 = True
            else:
                print('Sorry, that number is not within the acceptable range (0-100)!\nPlease Try Again :)')
                initial_range1 = False # Not Necessary, but helps with readability
                
    # Initial taken condition
    Taken = True

    while number2.isdigit() == False or initial_range2 == False:# or Taken==True:
        
        number2 = input(f"{name2}, Please select your guess (0-100): ")
        
        # Digit Check
        if number2.isdigit() == False:
            print('Sorry, that is not a digit!\nPlease Try Again :)')
            
        # Range Check
        if number2.isdigit()== True:
            if int(number2) in acceptable_values:
                initial_range2 = True
            else:
                print('Sorry, that number is not within the acceptable range (0-100)!\nPlease Try Again :)')
                initial_range2 = False # Not Necessary, but helps with readability
                
        #if number2.isdigit() == True:
            #if number2 == number1:
                #Taken == True
                #print(f'{name1} has already selected that number!\nPlease Try Again :)')
            #else:
                #Taken == False
            
    if abs(randomnumber-int(number1))<abs(randomnumber-int(number2)):
        outcome = [f'{name1}',f'{name2}']
    else:
        outcome = [f'{name2}',f'{name1}']

    print(f'The random number was {randomnumber}.')  
    return outcome
    
        
        
def win_condition(board,mark):
    
    # All 8 possible win conditons
    if ((board[1]== mark and board[2]== mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or 
    (board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[1]==mark and board[4]==mark and board[7]==mark) or 
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or 
    (board[1]==mark and board[5]==mark and board[9]==mark) or 
    (board[7]==mark and board[5]==mark and board[3]==mark)):
        return 'win'
    
    # Board full condition
    elif (board[1]!=' ' and 
    board[2]!=' ' and
    board[3]!=' ' and
    board[4]!=' ' and
    board[5]!=' ' and
    board[6]!=' ' and
    board[7]!=' ' and
    board[8]!=' ' and
    board[9]!=' '):
        return "cat's scratch"
    else:
        pass
    
    
def play_again():
    choice = 'Wrong'
    
    while choice not in ['Yes','No']:
        choice = input("Would you like to restart the game (Yes or No)? ")
        
        if choice not in ['Yes','No']:
            print("Sorry, invalid choice!\nPlease choose say Yes or No!")
    if choice == 'Yes':
        return True
    else:
        return False
          
def Tic_Tac_Toe():
    # Clears output if starting a new game
    clear_output()
    # Tells users about game and decides who goes first and who goes second
    print("Welcome to Tic-Tac-Toe!\nBefore I begin, can you both introduce yourself to me?")
    print('')
    time.sleep(.5)
    name1 = input("What is the first name? ")
    name2 = input("What is the second name? ")
    print('')
    print(f'Hi {name1} and {name2}, I hope you are both ready to play.\n\nBefore we begin, we need to decide who will go first with a number guessing game!')
    print('')
    outcome = player_order(name1,name2)
    
    win = outcome[0]
    lose = outcome[1]
          
          
    print(f"{win} is 'X' and {lose} is 'O'.\nTake a look at the placement positions before making a choice.")
    time.sleep(.5)
    print('')
    # Shows board positions
  
    print('1'+'|'+'2'+'|'+'3')
    print('-|-|-')
    print('4'+'|'+'5'+'|'+'6')
    print('-|-|-')
    print('7'+'|'+'8'+'|'+'9')


    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
          
    while True:
        
        player1_placement = position_choice_1(board,win)
        board[player1_placement] = 'X'
        display_board(board)
        game_on = win_condition(board,'X')
        if game_on == 'win':
            print(f'{win} has won the game. Congratulations!')
            break
        elif game_on == "cat's scratch":
            print("Cat's Scratch. Neither player won.")
            break
            
            
        player2_placement = position_choice_2(board,lose)
        board[player2_placement] = 'O'
        display_board(board)
        game_on = win_condition(board,'O')
        if game_on == 'win':
            print(f'{lose} has won the game. Congratulations!')
            break
        elif game_on == "cat's scratch":
            print("Cat's Scratch. Neither player won.")
            break
            
    playon = play_again()
    if playon:
        Tic_Tac_Toe()
    else:
        print('Thank you for playing. Please come again!')
        pass       


# In[ ]:





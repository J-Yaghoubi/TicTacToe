
import sys
from pynput import keyboard
from funcs import functionality as fn
import settings as se


class TicTacToe:

    class Meta:
        """
            This meta class use as a database for live data
        """

        position = 'Main'
        counter = 0
        game_process = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        win_algo = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        player_one = True

        p_one_name = 'Player One'
        p_two_name = 'Player Two'

        numeric_key = 0

    def __init__(self) -> None:
        self.animate_logo()
        self.show_menu()

    @classmethod
    def animate_logo(cls):
        fn.animate_logo() 

    @classmethod
    def show_menu(cls):
        # Reset old Game
        cls.Meta.game_process = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
       
        cls.Meta.position = 'Main'
        fn.show_menu(cls.Meta.counter)
        cls.scan_input()
        
    @classmethod
    def enter_menu(cls, selected: int):
        if   selected == 0: cls.ask_name()
        elif selected == 1: cls.show_score()
        elif selected == 2: cls.show_settings()
        elif selected == 3: cls.show_about()
        elif selected == 4: exit()

    @classmethod
    def ask_name(cls):

        fn.show_logo()
        cls.Meta.position = 'AskName'
        
        # while not cls.Meta.p_one_name:
        #     cls.Meta.p_one_name = input('\nEnter Player One Name: ')
        #     cls.Meta.p_two_name = input('\nEnter Player TWo Name: ')

        cls.show_board()

    @classmethod
    def show_board(cls):
        cls.Meta.position = 'Board'
        fn.show_board(cls.Meta.game_process)
        print(se.HELP_COLOR + se.START_MARGIN + f'*{cls.Meta.p_one_name}: X  {cls.Meta.p_two_name}: O  Esc: BackToMain\n')
        cls.scan_input()     

    @classmethod
    def show_score(cls):
        cls.Meta.position = 'Score'
        fn.show_setting()
        cls.scan_input()

    @classmethod
    def show_settings(cls):
        cls.Meta.position = 'Settings'
        fn.show_setting()
        cls.scan_input()

    @classmethod
    def show_about(cls):
        cls.Meta.position = 'About'
        fn.show_about()
        cls.scan_input()

    @classmethod
    def save_and_check(cls, num: int):
        """
            Save User selection and check if there is a winner or the game has be ended without any winner   
        """

        end = False

        # Save player select
        cls.Meta.game_process[num] = 'X' if cls.Meta.player_one else 'O'
   
        # Search for winner
        for i in range(len(cls.Meta.win_algo)):
            if cls.Meta.game_process[cls.Meta.win_algo[i][0]] == cls.Meta.game_process[cls.Meta.win_algo[i][1]] == cls.Meta.game_process[cls.Meta.win_algo[i][2]] == cls.Meta.game_process[num]: 
                cls.Meta.position = 'Win'
                end = True
                fn.show_win('Player One') if cls.Meta.player_one else fn.show_win('Player Two')

        # if board is full without winner
        if not '.' in cls.Meta.game_process:
            cls.Meta.position = 'Win'
            end = True
            fn.show_win('No One')             
             
        # if game is in process then: Toggle player and Update the Board
        if not end:
            cls.Meta.player_one = not cls.Meta.player_one  
            cls.show_board()
        
    @classmethod
    def scan_input(cls):
        """
            after giving valid request from user, we break the While loop and stop keyboard listener,
            then we go to new location depends on user selection
        """

        with keyboard.Events() as events:
            for event in events:
                event = events.get(1.0)
               
                # Main-Menu Scan
                if  cls.Meta.position == 'Main':

                    if event.key == keyboard.Key.up and cls.Meta.counter > 0:
                        cls.Meta.counter-=1

                    elif event.key == keyboard.Key.down and cls.Meta.counter < 4:
                        cls.Meta.counter+=1  

                    elif event.key == keyboard.Key.esc:
                        sys.exit()

                    elif event.key == keyboard.Key.enter:  
                        break                   

                    # Refresh menu
                    cls.show_menu()   
                
                # About Scan
                elif cls.Meta.position == 'About' or cls.Meta.position == 'AskName' or cls.Meta.position == 'Settings' or cls.Meta.position == 'Score':
                    if event.key == keyboard.Key.esc:
                        break                        
                
                # Board Scan
                elif cls.Meta.position == 'Board':               
                    if event.key == keyboard.Key.esc:
                        cls.show_menu() 

                    elif event.key == keyboard.KeyCode(char= '1') and cls.Meta.game_process[0] == '.':
                        cls.Meta.numeric_key = 0
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '2') and cls.Meta.game_process[1] == '.':
                        cls.Meta.numeric_key = 1
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '3') and cls.Meta.game_process[2] == '.':
                        cls.Meta.numeric_key = 2
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '4') and cls.Meta.game_process[3] == '.':
                        cls.Meta.numeric_key = 3
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '5') and cls.Meta.game_process[4] == '.':
                        cls.Meta.numeric_key = 4
                        break
                   
                    elif event.key == keyboard.KeyCode(char= '6') and cls.Meta.game_process[5] == '.':
                        cls.Meta.numeric_key = 5
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '7') and cls.Meta.game_process[6] == '.':
                        cls.Meta.numeric_key = 6
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '8') and cls.Meta.game_process[7] == '.':
                        cls.Meta.numeric_key = 7
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '9') and cls.Meta.game_process[8] == '.':
                        cls.Meta.numeric_key = 8
                        break

                # Win Scan
                elif cls.Meta.position == 'Win':
                    if event.key == keyboard.Key.esc:
                        break                      


        if cls.Meta.position == 'Main':         
            cls.enter_menu(cls.Meta.counter) 
        elif cls.Meta.position == 'About' or cls.Meta.position == 'AskName' or cls.Meta.position == 'Settings' or cls.Meta.position == 'Score' or cls.Meta.position == 'Win':
            cls.show_menu() 
        elif cls.Meta.position == 'Board':
            cls.save_and_check(cls.Meta.numeric_key)            


game = TicTacToe()



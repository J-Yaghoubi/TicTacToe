

from pynput import keyboard
from funcs import functionality as fn
import settings as se


class TicTacToe:

    class Meta:

        position = 'Main'
        counter = 0
        game_process = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        win_algo = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'), ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]
        player_one = True

        p_one_name = 'Player One'
        p_two_name = 'Player Two'


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
    def enter_menu(cls, selected):
        if   selected == 0: cls.ask_name()
        elif selected == 1: cls.show_score()
        elif selected == 2: cls.show_settings()
        elif selected == 3: cls.show_about()
        elif selected == 4: exit()

    @classmethod
    def ask_name(cls):

        fn.show_logo()

        cls.Meta.position = 'AskName'
        
        # a = None
        # b = None

        # while not a:
        #     a = input('\nEnter Player One Name: ')
        #     b = input('\nEnter Player TWo Name: ')

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
    def save_and_check(cls, num):
        
        # Save player select
        cls.Meta.game_process[num] = 'X' if cls.Meta.player_one else 'O'

        # Check for wining pattern
        p_one_temp_list = []
        p_two_temp_list = []

        if cls.Meta.player_one:     
            p_one_temp_list = "".join(['P' if i == 'X' else '.' for i in cls.Meta.game_process])    
        else:
            p_two_temp_list = "".join(['P' if i == 'O' else '.' for i in cls.Meta.game_process])   

        if p_one_temp_list in cls.Meta.win_algo:
            cls.Meta.position = 'Win'
            fn.show_win('Player One')
        elif p_two_temp_list in cls.Meta.win_algo:
            cls.Meta.position = 'Win'
            fn.show_win('Player One')
       
        else:    
            # Toggle player
            cls.Meta.player_one = not cls.Meta.player_one  
            # Update Board
            cls.show_board()
        
    @classmethod
    def scan_input(cls):

        with keyboard.Events() as events:
            for event in events:
                event = events.get(1.0)
               
                # MainMenu Scan
                if  cls.Meta.position == 'Main':

                    if event.key == keyboard.Key.up and cls.Meta.counter > 0:
                        cls.Meta.counter-=1

                    elif event.key == keyboard.Key.down and cls.Meta.counter < 4:
                        cls.Meta.counter+=1  

                    elif event.key == keyboard.Key.esc:
                        exit()

                    elif event.key == keyboard.Key.enter:   
                        cls.enter_menu(cls.Meta.counter)
                        break 

                    # Refresh menu
                    cls.show_menu()   
                
                # About Scan
                elif cls.Meta.position == 'About' or cls.Meta.position == 'AskName' or cls.Meta.position == 'Settings' or cls.Meta.position == 'Score':
                    if event.key == keyboard.Key.esc:
                        cls.show_menu() 
                        break
                
                # Board Scan
                elif cls.Meta.position == 'Board':               
                    if event.key == keyboard.Key.esc:
                        cls.show_menu() 
                        break

                    elif event.key == keyboard.KeyCode(char= '1') and cls.Meta.game_process [0] == '.':
                        cls.save_and_check(0)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '2') and cls.Meta.game_process [1] == '.':
                        cls.save_and_check(1)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '3') and cls.Meta.game_process [2] == '.':
                        cls.save_and_check(2)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '4') and cls.Meta.game_process [3] == '.':
                        cls.save_and_check(3)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '5') and cls.Meta.game_process [4] == '.':
                        cls.save_and_check(4)
                        break
                   
                    elif event.key == keyboard.KeyCode(char= '6') and cls.Meta.game_process [5] == '.':
                        cls.save_and_check(5)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '7') and cls.Meta.game_process [6] == '.':
                        cls.save_and_check(6)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '8') and cls.Meta.game_process [7] == '.':
                        cls.save_and_check(7)
                        break
                    
                    elif event.key == keyboard.KeyCode(char= '9') and cls.Meta.game_process [8] == '.':
                        cls.save_and_check(8)
                        break

                # Win Scan
                elif cls.Meta.position == 'Win':
                    if event.key == keyboard.Key.esc:
                        cls.show_menu() 
                        break

                




game = TicTacToe()



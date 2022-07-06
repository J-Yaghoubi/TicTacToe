
import settings as se
import visual as vs
import utility
import time

class functionality:
    """
       We defined the responsibility of game section here and used them in Main.py
    """

    def animate_logo():
        for i in range(10,-1,-1):
            utility.clear_screen()
            print(se.LOGO_COLOR + vs.LOGO_F)            
            print('\n' * i)
            print(se.LOGO_COLOR  + vs.LOGO_M) 
            print('\n' * i) 
            print(se.LOGO_COLOR  + vs.LOGO_L)   
            time.sleep(0.1)  


    def show_logo():
        utility.clear_screen()
        print('\n\n' + vs.dash_line)
        print(se.LOGO_COLOR  + vs.LOGO_FULL) 
        print('\n') 


    def show_menu(val):
        functionality.show_logo()

        selected = ['[*' if i == val else '[ ' for i in range(len(vs.main_menu))]
        [print(se.MENU_COLOR + se.MARGIN + selected[i] + vs.main_menu[i]) for i in range(len(vs.main_menu))]

        print('\n\n' + vs.dash_line)
        print(vs.main_menu_help)


    def animate_dice(starter):
        for i in range(len(vs.LOADING)):
            functionality.show_logo()
            print(se.LOGO_COLOR + '\n\n\n')
            print('Rolling Dice...'.center(66))
            print(se.BOARD_COLOR + vs.LOADING[i].center(66))    
            print('\n\n\n\n' + vs.dash_line) 
            print(vs.dice_help)          
            time.sleep(0.5)  

        functionality.show_logo()
        print(se.BOARD_COLOR + '\n\n\n')
        print(f'{starter} will start the game'.center(66))
        print('\n\n\n\n\n' + vs.dash_line)
        print(vs.dice_help)     
        time.sleep(3)


    def show_board(process: list):
        functionality.show_logo()

        board = ['| ' + process[i] if process[i] != '.' else '| ' + str(i+1) for i in range(9)]

        print(se.BOARD_COLOR + (se.BOARD_MARGIN) + '+-----------+')
        for i in range(0,9,3):
            print(se.BOARD_COLOR + se.BOARD_MARGIN + ' '.join(board[i:i+3]) + ' |')
            print(se.BOARD_COLOR + se.BOARD_MARGIN + '+-----------+')

        print('\n\n' + vs.dash_line)


    def show_win(winner):
        functionality.show_logo()
        print('\n\n\n')
        print(f'{winner} is Winner'.center(66))
        print('\n\n\n\n\n\n' + vs.dash_line)  
        print(vs.about_help)  


    def show_setting():
        utility.clear_screen()
        print('\n\n' + vs.dash_line + '\n\n')
        print(vs.COMING)
        print('\n' + vs.dash_line)  
        print(vs.about_help)  


    def show_about():
        utility.clear_screen()
        print('\n\n\n' + vs.dash_line + '\n\n\n\n')
        print(vs.ABOUT)
        print('\n' + vs.dash_line)  
        print(vs.about_help)  


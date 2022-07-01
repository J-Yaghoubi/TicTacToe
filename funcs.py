
import settings as se
import visual as vs
import utility
import time


def animate_logo():
    for i in range(10,-1,-1):
        utility.clear_screen()
        print('\u001b[32m' + vs.LOGO_F)            
        print('\n' * i)
        print('\u001b[32m' + vs.LOGO_M) 
        print('\n' * i) 
        print('\u001b[32m' + vs.LOGO_L)   
        time.sleep(0.1)  


def show_logo():
    utility.clear_screen()
    print('\n\n' + vs.dash_line)
    print('\u001b[32m' + vs.LOGO_FULL) 
    print('\n') 


def show_menu(val):
    selected = ['[*' if i == val else '[ ' for i in range(len(vs.main_menu))]
    [print(se.MENU_COLOR + se.MARGIN + selected[i] + vs.main_menu[i]) for i in range(len(vs.main_menu))]
    print('\n\n' + vs.dash_line)
    print(vs.main_menu_help)


def show_board():
    print(se.BOARD_COLOR + se.BOARD_MARGIN + '+---------------+')
    for i in range(0,9,3):
        print(se.BOARD_COLOR + se.BOARD_MARGIN + ' '.join(vs.BOARD[i:i+3]))
        print(se.BOARD_COLOR + se.BOARD_MARGIN + '+---------------+')
    print('\n\n' + vs.dash_line)
    print(vs.main_menu_help)


def show_about():
    utility.clear_screen()
    print(vs.ABOUT)    
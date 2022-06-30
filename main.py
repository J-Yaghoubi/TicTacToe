
import settings as se
import menu as mu
import utility
import time

class TicTacToe:

    def animate_logo(self):
        for i in range(0,7):
            utility.clear_screen()
            time.sleep(0.3)
            print('\n\n\n\n\n\n')
            print('\u001b[32m' + mu.LOGO) 
            

    def show_logo(self):
        utility.clear_screen()
        print('\n\n' + mu.dash_line)
        print('\u001b[32m' + mu.LOGO) 
        print('\n') 


    def show_menu(self, input_key : int):
        selected = ['[*' if i == input_key else '[ ' for i in range(len(mu.main_menu))]
        [print(se.MENU_COLOR + se.MARGIN + selected[i] + mu.main_menu[i]) for i in range(len(mu.main_menu))]
        print('\n\n' + mu.dash_line)
        print(mu.main_menu_help)


    def show_board(self):
        print(se.BOARD_COLOR + se.BOARD_MARGIN + '+---------------+')
        for i in range(0,9,3):
            print(se.BOARD_COLOR + se.BOARD_MARGIN + ' '.join(mu.BOARD[i:i+3]))
            print(se.BOARD_COLOR + se.BOARD_MARGIN + '+---------------+')
        print('\n\n' + mu.dash_line)
        print(mu.main_menu_help)



game = TicTacToe()
game.animate_logo()
game.show_logo()
game.show_board()



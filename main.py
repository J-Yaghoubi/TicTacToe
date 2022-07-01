
from pynput import keyboard
import funcs


class TicTacToe:

    class Meta:
        menu_explorer = 'Main'
        counter = 0

    def __init__(self) -> None:
        self.animate_logo()
        self.show_logo()
        self.show_menu()
        self.scan_input()

    def animate_logo(self):
        funcs.animate_logo()
    
    def show_logo(self):
        funcs.show_logo()

    @classmethod
    def show_menu(cls):
        funcs.show_menu(cls.Meta.counter)

    @staticmethod
    def enter_menu(selected):
        if   selected == 0: funcs.show_board()
        elif selected == 1: funcs.show_about()
        elif selected == 2: funcs.show_about()
        elif selected == 3: funcs.show_about()
        elif selected == 4: exit()


    def scan_input(self):

        with keyboard.Events() as events:
            for event in events:
                event = events.get(1.0)

                if  self.__class__.Meta.menu_explorer == 'Main':

                    # Read Key
                    if event.key == keyboard.Key.up and self.__class__.Meta.counter > 0:
                        self.__class__.Meta.counter-=1

                    elif event.key == keyboard.Key.down and self.__class__.Meta.counter < 4:
                        self.__class__.Meta.counter+=1  

                    elif event.key == keyboard.Key.enter:   
                        self.__class__.enter_menu(self.__class__.Meta.counter)
                        break 

                    # Refresh menu
                    self.show_logo()
                    self.show_menu()   

                elif self.__class__.menu_explorer == 'Start':
                    pass

                else:
                    pass



game= TicTacToe()



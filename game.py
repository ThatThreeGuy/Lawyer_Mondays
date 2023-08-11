from bases import *
from main_menu import *
from settings import *
from courtroom import *
from cutscenes import *
from point_and_click import *

game = menu_screen()

if game:
    #starting_cutscene()
    first_point_and_click(inventory_button)
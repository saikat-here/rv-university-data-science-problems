
import pygame as gui
import time
import sys
from pygame.locals import *

bgcolour = (255, 255, 255)  # defining background colour
line_color = (0, 0, 0) # defining line colour
line_color_green = (0, 153, 51)

o_x = "X" # defining game symbon-1
o_o = "O" # defining game symbon-2
click_symbol = o_x # defining the start symbol

height = 400 # defining the height of the game window
width = 400 #defining the width of the game window


win = False
win_symbol = ""

click_count = 0
window = gui.display.set_mode((width + 6, height + 106), 0, 32)
gui.display.set_caption("Tic Tac Toe Game")

r = [[0]*3 for i in range(3)] # defining game symbol holder

gui.init()

def start_the_game_window():
    """ Initializes the game window """
    gui.display.update()
    window.fill(bgcolour)

    # drawing horizontal lines
    gui.draw.line(window, line_color, (width / 3, 0), (width / 3, height), 2)
    gui.draw.line(window, line_color, (width / 3 * 2, 0), (width / 3 *2 , height), 2)

    # drawing vertical lines
    gui.draw.line(window, line_color, (0, height / 3), (width, height / 3), 2)
    gui.draw.line(window, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 2)

    # drawing end of the board line
    gui.draw.line(window, line_color, (0, height), (width, height), 10)

def get_clicked_cell():
    """ Calculates the  row and column of the clicked location """
    row = None
    col = None
    x,y = gui.mouse.get_pos() # getting clicked position

    # The width is devided in 3 columns. If its clicked on the 1/3 of the width then its the first column.
    if x < width /3:
        row = 1
    elif x < width / 3 * 2 :
        row = 2
    elif x < width:
        row = 3


    if y < height / 3:
        col = 1
    elif y < height / 3 * 2:
        col = 2
    elif y < height:
        col = 3

    return col, row

def get_print_location(row, col):
    """ Calculating the print location of the symbol depending on the row and column value"""

    if row == 1:
        x = (width / 3) / 2
    elif row == 2:
        x= width /2
    elif row == 3:
        x = ((width / 3) * 2) + ( width / 6)


    if col ==1:
        y = (height / 3) / 2
    elif col == 2:
        y = height /2
    elif col == 3:
        y = height / 6 * 5

    return x,y

def print_symbol(symbol, row, col):
    """ Printing the game symbol on correct location """
    font = gui.font.SysFont("Arial", 70)
    text = font.render(symbol, True, line_color)

    x,y = get_print_location(row, col)

    centerTitle = text.get_rect(center=(y, x))
    window.blit(text, centerTitle)

    #window.blit(text,(y , x ))
    gui.display.update()

def add_symbol_to_board(row, col, symbol):
    """ Adding the symbol of board for calculations"""
    global r, click_count

    if r[row-1][col-1] == 0:
        r[row-1][col-1] = symbol
        print_symbol(symbol, row, col)

        click_count += 1
        if click_count == 9:
            print_msg(f"There is no winner")
            reset_game()

def check_winer():
    """ Checking the game winer """
    global win
    global win_symbol
    # Checking rows for winers
    for i in range(3):
        if r[i].count(o_x) ==3 or r[i].count(o_o) == 3:
            gui.draw.line(window, line_color_green, (0, height/6 *((i*2)+1) ), (width, height/6 *((i*2)+1)), 2)
            win = True
            win_symbol = r[i][0]
            return

    # Checking columns for winer
    for i in range(3):

        if [r[0][i],r[1][i],r[2][i]].count(o_o)==3 or [r[0][i],r[1][i],r[2][i]].count(o_x)==3:
            gui.draw.line(window, line_color_green, ( width / 6 * ((i*2)+1), 0), (width / 6 * ((i*2)+1), height), 2)
            win = True
            win_symbol = r[0][i]
            return

    # checking diagonal matches
    if [r[0][0],r[1][1],r[2][2]].count(o_x)==3 or [r[0][0],r[1][1],r[2][2]].count(o_o)==3:
        gui.draw.line(window, line_color_green, (0, 0), (width , height), 2)
        win = True
        win_symbol = r[0][0]
        return

    # checking diagonal matches
    if [r[0][2],r[1][1],r[2][0]].count(o_x)==3 or [r[0][2],r[1][1],r[2][0]].count(o_o)==3:
        gui.draw.line(window, line_color_red, (0, height), (width, 0), 2)
        win = True
        win_symbol = r[0][2]
        return

def print_msg(msg):
    """ Printing the message on the message board ( bottom of the game window ) """
    global win_symbol
    font = gui.font.SysFont("Arial", 30)
    text = font.render(msg, True, line_color)

    centerTitle = text.get_rect(center=((width/2),height+50))
    window.blit(text, centerTitle)

    gui.display.update()

def reset_game():
    """ Reseting game variables after win or no-win"""
    time.sleep(3)
    global  win, win_symbol, r, click_symbol, o_x, click_count
    win = False
    win_symbol = ""
    r = [[0] * 3 for i in range(3)]
    start_the_game_window()
    click_symbol = o_o
    click_count = 0


def process_input():
    """ Control method for this game """
    global click_symbol
    row = None
    col = None

    row, col = get_clicked_cell()
    symbol_to_print= None
    global click_count

    if row != None and col != None:

        add_symbol_to_board(row, col, click_symbol)
        check_winer()
        if win:
            print_msg(f"{win_symbol} is the winner")
            reset_game()

        click_symbol = o_o if click_symbol == o_x else o_x


# startin the game window
start_the_game_window()

while True:
    for event in gui.event.get():

        if event.type == gui.QUIT:
            gui.quit()
            sys.exit()
        elif event.type == gui.MOUSEBUTTONDOWN:
            process_input()


    gui.display.update()

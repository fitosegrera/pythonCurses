#!/usr/bin/env python

from unicurses import *

WIDTH = 30
HEIGHT = 10
startx = 0
starty = 0
choices = ["Simulation", "Motor Controll", "Exit"]
n_choices = len(choices)
highlight = 1
choice = 0
c = 0

def print_in_middle(win, starty, startx, width, string):
    if (win == None): win = stdscr
    y, x = getyx(win)
    if (startx != 0): x = startx
    if (starty != 0): y = starty
    if (width == 0): width = 80
    length = len(string)
    temp = (width - length) / 2
    x = startx + int(temp)
    mvaddstr(y, x, string)

def intro():
	noecho()
	stdscr = initscr()
	start_color()
	init_pair(1, COLOR_WHITE, COLOR_BLUE)
	bkgd(COLOR_PAIR(1))
	border()
	contents = {
		"title": "it from bit",
		"subtitle": "simulation & motor_controll",
		"author": "fito_segrera 2015",
		"website": "http://fii.to",
		"continue": "<press any key>"
	}
	LINES, COLS = getmaxyx(stdscr)
	print_in_middle(stdscr, int(LINES / 2) - 2, int(COLS / 2) - (len(contents["title"]))/2, len(contents["title"]), contents["title"])
	print_in_middle(stdscr, int(LINES / 2) - 1, int(COLS / 2) - (len(contents["subtitle"]))/2, len(contents["subtitle"]), contents["subtitle"])
	print_in_middle(stdscr, int(LINES / 2), int(COLS / 2) - (len(contents["author"]))/2, len(contents["author"]), contents["author"])
	print_in_middle(stdscr, int(LINES / 2) + 1, int(COLS / 2) - (len(contents["website"]))/2, len(contents["website"]), contents["website"])
	print_in_middle(stdscr, int(LINES / 2) + 4, int(COLS / 2) - (len(contents["continue"]))/2, len(contents["continue"]), contents["continue"])
	getch()

def menu(menu_win, highlight):
    x = 2
    y = 2
    border()
    box(menu_win, 0, 0)
    for i in range(0, n_choices):
        if (highlight == i + 1):
            wattron(menu_win, A_REVERSE)
            mvwaddstr(menu_win, y, x, choices[i])
            wattroff(menu_win, A_REVERSE)
        else:
            mvwaddstr(menu_win, y, x, choices[i])
        y += 1
    wrefresh(menu_win)

def main():
	global highlight, choice, startx, starty
	if (has_colors() == False):
	    endwin()
	    print("Your terminal does not support color!")
	    exit(1)

	intro()
	clear()
	stdscr = initscr()
	noecho()
	cbreak()
	curs_set(0)
	LINES, COLS = getmaxyx(stdscr)
	startx = int(COLS/2 - WIDTH/2)
	starty = int(LINES/2 - HEIGHT/2)
	# startx = int((80 - WIDTH) / 2)
	# starty = int((24 - HEIGHT) / 2)
	menu_win = newwin(HEIGHT, WIDTH, starty, startx)
	keypad(menu_win, True)
	mvaddstr(1, 1, "Use arrow keys to go up and down, press ENTER to select a choice")
	mvaddstr(2, 1, "Number of LINES: " + str(LINES))
	mvaddstr(3, 1, "Number of COLS: " + str(COLS))
	mvaddstr(4, 1, "Memu pos Y: " + str(starty))
	mvaddstr(5, 1, "Menu pos X: " + str(startx))
	refresh()
	menu(menu_win, highlight)
	while True:
	    c = wgetch(menu_win)
	    if c == KEY_UP:
	        if highlight == 1:
	            highlight == n_choices
	        else:
	            highlight -= 1
	    elif c == KEY_DOWN:
	        if highlight == n_choices:
	            highlight = 1
	        else:
	            highlight += 1
	    elif c == 10:   # ENTER is pressed
	        choice = highlight
	        mvaddstr(LINES - 3, 1, str.format("You chose choice {0} with choice string {1}", choice, choices[choice-1]))
	        clrtoeol()
	        refresh()
	    else:
	        mvaddstr(LINES - 2, 1, str.format("Character pressed is = {0}", c))
	        clrtoeol()
	        refresh()
	    menu(menu_win, highlight)
	    if choice == 3:
	        break

	refresh()
	endwin()

if __name__ == "__main__":
	main()

import curses
from curses import wrapper
import curses

def power_on(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speedy Typing!")
    stdscr.addstr("\n\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getkey()
    
def display_screen(stdscr, qn, user, wpm = 0):
    stdscr.addstr("Type the following: \n")
    stdscr.addstr(qn, curses.color_pair(3))
    for i, char in enumerate(user):
        if char == qn[i]:
            stdscr.addstr(1, i, char, curses.color_pair(2))
        else:
            stdscr.addstr(1, i, char, curses.color_pair(1))
    
    
def typing_screen(stdscr):
    qn_text = "The quick brown fox jumps over the lazy dog."
    user_text = []

    while True:
        stdscr.clear()
        display_screen(stdscr, qn_text, user_text)

        key = stdscr.getkey()

        if key == "\n":
            break
        elif key in ("BACKSPACE", "\b", "\x7f"):
            if user_text:
                user_text.pop()
        else:
            user_text.append(key)
            

def main(stdscr):
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    power_on(stdscr)
    typing_screen(stdscr)
    
wrapper(main)
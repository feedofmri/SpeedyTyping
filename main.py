import curses
from curses import wrapper

def power_on(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speedy Typing!")
    stdscr.addstr("\n\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getkey()
    
def typing_screen(stdscr):
    qn_text = "The quick brown fox jumps over the lazy dog."
    user_text = []
    
    while True:
        stdscr.clear()
        stdscr.addstr("Type the following: ")
        stdscr.addstr(qn_text, curses.color_pair(3))
        stdscr.addstr("\n\nYour text: ")
        for i in user_text:
            stdscr.addstr(i, curses.color_pair(2))
        stdscr.refresh()
        
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
        elif key in ("BACKSPACE", "\b", "\x7f"):
            if user_text:
                user_text.pop()
        else:
            user_text.append(key)
            

def main(stdscr):
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    power_on(stdscr)
    typing_screen(stdscr)
    
wrapper(main)
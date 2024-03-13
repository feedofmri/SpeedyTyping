import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.addstr("How are you?", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()
    
wrapper(main)
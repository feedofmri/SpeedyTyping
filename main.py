import curses
form curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("How are you?")
    stdscr.refresh()
    stdscr.getkey()
    
wrapper(main)
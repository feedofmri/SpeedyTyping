import curses
from curses import wrapper
import curses
import time

def power_on(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speedy Typing!")
    stdscr.addstr("\n\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getkey()
    
def display_screen(stdscr, qn, user, wpm = 0):
    stdscr.addstr("Type the following: \n\n")
    stdscr.addstr(qn, curses.color_pair(3))
    stdscr.addstr(4, 0, f"WPM: {wpm}")
    
    for i, char in enumerate(user):
        if char == qn[i]:
            stdscr.addstr(2, i, char, curses.color_pair(2))
        else:
            stdscr.addstr(2, i, char, curses.color_pair(1))
    
    
def typing_screen(stdscr):
    qn_text = "The quick brown fox jumps over the lazy dog."
    user_text = []

    stdscr.nodelay(True)
    start_time = time.time()
    wpm = 0
    while True:
        
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round(len(user_text) / 5 / (elapsed_time / 60))
        
        stdscr.clear()
        display_screen(stdscr, qn_text, user_text, wpm)

        try:
            key = stdscr.getkey()
        except:
            continue

        if key == "\n":
            break
        elif key in ("BACKSPACE", "\b", "\x7f"):
            if user_text:
                user_text.pop()
        elif len(user_text) < len(qn_text):
            user_text.append(key)
            

def main(stdscr):
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    power_on(stdscr)
    typing_screen(stdscr)
    
wrapper(main)
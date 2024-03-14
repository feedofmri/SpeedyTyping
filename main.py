import curses
from curses import wrapper
import curses
import time
import random

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
    qn_list = [
        "The Quick Brown Fox: The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet, making it a useful typing exercise.",
        "Seashells by the Seashore: She sells seashells by the seashore. Try typing this tongue twister without stumbling!",
        "Woodchuck Chucking Wood: How much wood would a woodchuck chuck if a woodchuck could chuck wood? A playful phrase to test your typing accuracy.",
        "Peter Piper Picked: Peter Piper picked a peck of pickled peppers. Say that five times fast!",
        "Sally Sells Sea Shells: Sally sells sea shells down by the sea shore. A classic alliteration to improve your typing flow."
        "Betty Botter’s Butter: Betty Botter bought some butter, but she said the butter’s bitter. A challenging one!",
        "Slippery Snails Sliding: Six slippery snails slid slowly seaward. Type it smoothly!",
        "Unique New York: Unique New York, you know you need unique New York. A tricky tongue twister for accuracy.",
        "Red Lorry, Yellow Lorry: Red lorry, yellow lorry, red lorry, yellow lorry. Can you keep up?",
        "Fuzzy Wuzzy Bear: Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. A fun rhyme to type.",
        "Clam Cram in Clean Cream Can: How can a clam cram in a clean cream can? A delightful challenge!",
        "Black Bugs Bleed: Black bugs bleed black blood. Say it five times while typing!",
        "I Scream for Ice Cream: I scream, you scream, we all scream for ice cream! A tasty typing exercise.",
        "Proper Copper Coffee Pot: A proper copper coffee pot. Try saying it fast!",
        "Toy Boat, Toy Boat: Toy boat, toy boat, toy boat. A tricky one for speed.",
        "Irish Wristwatch, Swiss Wristwatch: Irish wristwatch, Swiss wristwatch. Keep those wrists nimble!",
        "Three Free Throws: Three free throws. Type it accurately.",
        "Greek Grapes: Greek grapes. Simple yet effective.",
        "Freshly Fried Flying Fish: Freshly fried flying fish. A mouthful to type!",
        "Silent Sliding Snails: Six slippery snails slid silently. Perfect your rhythm."]
    
    qn_text = random.choice(qn_list)
    user_text = []

    stdscr.nodelay(True)
    start_time = time.time()
    wpm = 0
    while True:
        
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round(len(user_text) / 5 / (elapsed_time / 60))
        
        stdscr.clear()
        display_screen(stdscr, qn_text, user_text, wpm)
        
        if user_text == list(qn_text):
            stdscr.nodelay(False)
            break	

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
    while True:
        typing_screen(stdscr)
        stdscr.addstr(6, 0, "Press 'q' to quit or any other key to continue...")
        nkey = stdscr.getkey()
        if nkey == "q":
            break
        else:
            continue
    
wrapper(main)
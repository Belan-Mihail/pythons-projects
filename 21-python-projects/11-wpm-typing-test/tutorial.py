import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


# def main(stdscr):
#     # 1 = id, add front and background color
#     curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
#     stdscr.clear()
#     # use curses.init_pair with id 1 to follow text, 1 = 1 line down in terminal, 5 = 5 spaces on the line
#     stdscr.addstr(1, 5, 'Hello world', curses.color_pair(1))
#     # this text will overwrite previous text
#     stdscr.addstr(1, 0, 'Hello world', curses.color_pair(1))
#     stdscr.refresh()
#     # key pressed by the user
#     key = stdscr.getkey()
#     print(key)

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    # display speed of typing below the text
    stdscr.addstr(1, 0, f'WPM: {wpm}')

    # looking throug the current_text
    # enumerate give as index and value for each itteration
    for i, letter in enumerate(current):
        correct_letter = target[i]
        color = curses.color_pair(1)
        if letter != correct_letter:
            color = curses.color_pair(2)
        # print current text over the target_text by index and value.
        stdscr.addstr(0, i, letter, color)


def wpm_test(stdscr):
    target_text = 'Hello world this is some text for this app'
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()

    while True:
        # if time.time() - start_time we use 1 to preven dividing by 0
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) 


        stdscr.clear()
        display_text(stdscr, target_text, current_text)

        stdscr.refresh()

        # get key that pressed by user
        key = stdscr.getkey()

        # ord(key) numeric represent any key on the keyboard. 27 == esc
        if ord(key) == 27:
            break
        #  check backspace key to delete last element
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        
        # we can add current letter only inside len of target text and not more
        elif len(current_text) < len(target_text):
            # add key to current_text
            current_text.append(key)

        

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)

# 4:37:50
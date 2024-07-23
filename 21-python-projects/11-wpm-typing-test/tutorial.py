import curses
from curses import wrapper

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

def wpm_test(stdscr):
    target_text = 'Hello world this is some text for this app'
    current_text = []
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()

    while True:
        # get key that pressed by user
        key = stdscr.getkey()

        # ord(key) numeric represent any key on the keyboard. 27 == esc
        if ord(key) == 27:
            break

        # add key to current_text
        current_text.append(key)

        stdscr.clear()
        stdscr.addstr(target_text)

        # looking throug the current_text
        for letter in current_text:
            # print current text
            stdscr.addstr(letter, curses.color_pair(1))

        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)

# 4:37:50
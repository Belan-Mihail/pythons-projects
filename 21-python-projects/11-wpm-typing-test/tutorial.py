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

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)


wrapper(main)

# 4:23:39
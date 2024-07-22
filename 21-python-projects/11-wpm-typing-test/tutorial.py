import curses
from curses import wrapper

def main(stdscr):
    # 1 = id, add front and background color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    stdscr.clear()
    # use curses.init_pair with id 1 to follow text
    stdscr.addstr('Hello world', curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
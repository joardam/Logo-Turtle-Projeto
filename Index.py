import time
import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(1)

    pad = curses.newpad(100,100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67+j)
            pad.addstr(char, GREEN_AND_BLACK )

    for i in range(100):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh( 0 , 0 , 5 , i , 10, 25+i)
        time.sleep(0.2)
    stdscr.getch()

wrapper(main)
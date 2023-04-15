import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.box('|','-')
    stdscr.refresh()


    # Apertar "q" para sair
    while True: 
        key = stdscr.getch()
        if key == ord('q'): 
            break

wrapper(main)






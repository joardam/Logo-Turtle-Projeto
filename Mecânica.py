import curses
from curses import wrapper

def main(stdscr):
    curses.curs_set(0) # Oculta o cursor do terminal
    stdscr.clear()
    stdscr.box('|','-')
    stdscr.refresh()


    # Apertar "q" para sair
    while True: 
        key = stdscr.getch()
        if key == ord('q'): 
            break

wrapper(main)






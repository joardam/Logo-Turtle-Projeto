import curses
from curses import wrapper

def main(stdscr):
    curses.curs_set(0) # Oculta o cursor do terminal
    stdscr.clear()
    stdscr.box('|','-')
    stdscr.refresh()

    while True: # Loop infinito
        key = stdscr.getch()
        if key == ord('q'): # Sai do loop se o usuário pressionar a tecla 'q'
            break

wrapper(main)






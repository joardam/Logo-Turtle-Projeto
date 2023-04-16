import curses

menu = ['Comandos', 'Novo jogo', 'Sair']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx 
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP or key == ord('w') or key == ord('W') and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN or key == ord('s') or key == ord('S') and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"Você selecionou {}".format(menu[current_row_idx]))
            stdscr.refresh()
            # Exit
            if current_row_idx == len(menu)-1:
                stdscr.addstr(3,0,"Até logo!")
                stdscr.getch()
                break
            elif current_row_idx == len(menu)-2:
                continue
            #Comandos
            elif current_row_idx == len(menu)-3:
                stdscr.addstr(2,0,"Tecla W = cima")
                stdscr.addstr(3,0,"Tecla A = esquerda")
                stdscr.addstr(4,0,"Tecla S = baixo")
                stdscr.addstr(5,0,"Tecla D = direita")
                stdscr.getch()
                break
        
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()
curses.wrapper(main)
import curses
from Logo_turtle import main as logo_main
from turtle_imput import main as imput_main

menu = ['Comandos', 'Modo teclado','Modo texto', 'Sair']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.border()
    stdscr.addstr((h//2)-4, (w//2)-9,"L O G O  T U R T L E")

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

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP or key == ord('w') or key == ord('W') and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN or key == ord('s') or key == ord('S') and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"Você selecionou {}".format(menu[current_row_idx]))
            stdscr.refresh()
            # Saída
            if current_row_idx == len(menu)-1:
                stdscr.addstr(3,0,"Até logo!")
                stdscr.getch()
                break
            #Modo texto
            elif current_row_idx == len(menu)-2:
                stdscr.addstr(3,0,"Iniciando o jogo...")
                stdscr.addstr(5,0,"Pressione Enter")
                stdscr.getch()
                imput_main(stdscr)
                break
            #Modo teclado
            elif current_row_idx == len(menu)-3:
                stdscr.addstr(3,0,"Iniciando o jogo...")
                stdscr.addstr(5,0,"Pressione Enter")
                stdscr.getch()
                logo_main(stdscr)
                break
            #Comandos
            elif current_row_idx == len(menu)-4:
                stdscr.addstr(2,0,"MODO TECLADO:")
                stdscr.addstr(4,0,"Tecla W = Cima")
                stdscr.addstr(5,0,"Tecla A = Esquerda")
                stdscr.addstr(6,0,"Tecla S = Baixo")
                stdscr.addstr(7,0,"Tecla D = Direita")
                stdscr.addstr(8,0,"Barra de espaço = Para de desenhar")
                stdscr.addstr(10,0,"Diagonais:")
                stdscr.addstr(11,0,"Tecla E = Cima-direita")
                stdscr.addstr(12,0,"Tecla Q = Cima-esquerda")
                stdscr.addstr(13,0,"Tecla C = Baixo-direita")
                stdscr.addstr(14,0,"Tecla Z = Baixo-esquerda")

                stdscr.addstr(16,0,"MODO TEXTO:")
                stdscr.addstr(17,0,"ex. 'up 3' (qualquer comando + valor)")
                stdscr.addstr(19,0,"up = Cima")
                stdscr.addstr(20,0,"dw = Baixo")
                stdscr.addstr(21,0,"rt = Direita")
                stdscr.addstr(22,0,"lt = Esquerda")
                stdscr.addstr(24,0,"Desenhos:")
                stdscr.addstr(25,0,"sq = Quadrado")
                stdscr.addstr(26,0,"tg = Triângulo")
                stdscr.addstr(27,0,"dm = Diamante")
                stdscr.addstr(28,0,"ci = Círculo")
                stdscr.addstr(30,0,"Ferramentas:")
                stdscr.addstr(31,0,"pu = Para de desenhar/ Volta a desenhar")
                stdscr.addstr(32,0,"cl = Limpa os desenhos")
                stdscr.addstr(33,0,"ex = Sair")
                stdscr.getch()

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()
curses.wrapper(main)

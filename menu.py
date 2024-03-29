import curses


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
                from turtle_imput import main as imput_main
                break
            #Modo teclado
            elif current_row_idx == len(menu)-3:
                stdscr.addstr(3,0,"Iniciando o jogo...")
                stdscr.addstr(5,0,"Pressione Enter")
                stdscr.getch()
                from Logo_turtle import main as logo_main
                break
            #Comandos
            elif current_row_idx == len(menu)-4:
                stdscr.addstr(2,0,"MODO TECLADO:")
                stdscr.addstr(4,0,"Tecla W = Cima")
                stdscr.addstr(4,19,"Tecla A = Esquerda")
                stdscr.addstr(5,0,"Tecla S = Baixo")
                stdscr.addstr(5,19,"Tecla D = Direita")
                stdscr.addstr(6,0,"Barra de espaço = Para de desenhar")
                stdscr.addstr(7,0,"Diagonais:")
                stdscr.addstr(8,0,"Tecla E = Cima-direita")
                stdscr.addstr(8,26,"Tecla Q = Cima-esquerda")
                stdscr.addstr(9,0,"Tecla C = Baixo-direita")
                stdscr.addstr(9,26,"Tecla Z = Baixo-esquerda")

                stdscr.addstr(11,0,"MODO TEXTO:")
                stdscr.addstr(12,0,"ex. 'up 3' (qualquer comando + valor)")
                stdscr.addstr(13,0,"up = Cima")
                stdscr.addstr(13,16,"dw = Baixo")
                stdscr.addstr(14,0,"rt = Direita")
                stdscr.addstr(14,16,"lt = Esquerda")
                stdscr.addstr(16,0,"Desenhos:")
                stdscr.addstr(17,0,"sq = Quadrado")
                stdscr.addstr(17,16,"tg = Triângulo")
                stdscr.addstr(18,0,"dm = Diamante")
                stdscr.addstr(18,16,"ci = Círculo")
                stdscr.addstr(20,0,"Ferramentas:")
                stdscr.addstr(21,0,"pc = Para de desenhar/ Volta a desenhar")
                stdscr.addstr(22,0,"cl = Limpa os desenhos")
                stdscr.addstr(23,0,"ex = Sair")
                stdscr.addstr(26,0,"Pressione ENTER para voltar ao Menu Principal")
                stdscr.getch()

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()
curses.wrapper(main)

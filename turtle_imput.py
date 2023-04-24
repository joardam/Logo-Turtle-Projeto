import curses
from movement import move
import figures


def main(stdscr):
    curses.curs_set(1)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh - 3, sw, 0, 0)
    w.border()

    # Window de comando
    prompt = curses.newwin(3, sw, sh - 3, 0)
    prompt.border()
    prompt.addstr(1, 1, " Comandos: ")
    prompt.refresh()
    
    # Turtle no centro
    turtle = [(sh // 2) - 3, sw // 2]
    w.addch(turtle[0], turtle[1], '@')
    w.refresh()

    # Pen down
    pen_down = True
    
    while True:
    
        prompt.move(1, 11)
        prompt.clrtoeol()  # limpa o imput
        prompt.refresh()
        curses.echo()
        command = prompt.getstr().decode().strip()
        curses.noecho()

        if not command:
            continue  
        else:
            try:
                cmd, value = command.split()
                value = int(value)
                
            except ValueError as e:
                if "not enough values to unpack" in str(e):
                    cmd = command
                    #Verifica se o comando não precisa de número
                    if cmd in ['pc', 'cl' ,'sq', 'tg', 'dm', 'ci', 'ex']: 
                        pass
                    else:
                        continue
                else:
                    continue
        # Verifica se o comando é válido
        if cmd not in ['up', 'dw', 'rt', 'lt', 'pc', 'pd' , 'cl', 'sq', 'tg', 'dm', 'ci' , 'ex']:
            continue

        # Posição atual
        new_turtle = [turtle[0], turtle[1]]
        # Comandos
        
        #Pen change
        if cmd == 'pc':
            pen_down = not pen_down
       
        if cmd in ['up', 'dw', 'rt', 'lt'] :
            traceback = move(new_turtle , w , cmd , value , pen_down)
        
        if cmd in ['sq', 'tg', 'dm', 'ci']:
            traceback = figures.drawfigure(cmd,new_turtle,w)

        #Sair
        elif cmd == "ex":
            break

        else:
            continue

        # Movimentação dentro da tela
        if new_turtle[0] < 0 or new_turtle[0] >= sh - 3 or new_turtle[1] < 0 or new_turtle[1] >= sw:
            break

        # Desenho
        if pen_down:
            w.addch(turtle[0], turtle[1], traceback)
        else:
            w.addch(turtle[0], turtle[1], ' ')

        # Nova posição
        w.addch(new_turtle[0], new_turtle[1], '@')
        w.refresh()
        turtle = new_turtle

        prompt.clear()
        prompt.border()
        prompt.addstr(1, 1, " Comandos: ")
        prompt.refresh()

curses.wrapper(main)
import curses

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
        # get the user input and parse it
        prompt.move(1, 11)
        prompt.clrtoeol()  # clear the input line
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
            except ValueError:
                continue

        # Verifica se o comando é válido
        if cmd not in ['up', 'down', 'right', 'left', 'penup', 'quadrado', 'limpar']:
            continue

        # Posição atual
        new_turtle = [turtle[0], turtle[1]]
        
        # Comandos
        if cmd == "up":
            for i in range(value):
                new_turtle[0] -= value
                traceback = '|'
                w.addch(new_turtle[0], new_turtle[1], traceback)
        elif cmd == "down":
            for i in range(value):
                new_turtle[0] += 1
                traceback = '|'
                w.addch(new_turtle[0], new_turtle[1], traceback)
        elif cmd == "left":
            for i in range(value):
                new_turtle[1] -= 1
                traceback = '-'
                w.addch(new_turtle[0], new_turtle[1], traceback)
        elif cmd == "right":
            for i in range (value):
                new_turtle[1] += 1
                traceback = '-'
                w.addch(new_turtle[0], new_turtle[1], traceback)
        #Quadrado
        elif cmd == "quadrado":
            for i in range(0, 12):
                new_turtle[1] += 1
                traceback = '-'
                w.addch(new_turtle[0], new_turtle[1], traceback)
            for i in range(0, 6):
                new_turtle[0] += 1
                traceback = '|'
                w.addch(new_turtle[0], new_turtle[1], traceback)
            for i in range(0, 12):
                new_turtle[1] -= 1
                traceback = '-'
                w.addch(new_turtle[0], new_turtle[1], traceback)
            for i in range(0, 6):
                new_turtle[0] -= 1
                traceback = '|'
                w.addch(new_turtle[0], new_turtle[1], traceback)
        #Limpar tela
        elif cmd == "limpar":
            w.clear()
            w.border()
            w.refresh()
        #Pen up
        elif cmd == "penup":
            pen_down = not pen_down
            continue
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

        # refresh prompt window
        prompt.clear()
        prompt.border()
        prompt.addstr(1, 1, " Comandos: ")
        prompt.refresh()
            
curses.wrapper(main)


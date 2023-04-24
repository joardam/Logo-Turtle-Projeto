import curses

def move(newturtle, window ,direction, steps , penstatus):
    
    for i in range(steps):
        if direction == 'up' or direction == 'dw':
            if penstatus:
                trace = '|'
            else:
                trace = ' '

            if direction == 'up' :
                newturtle[0] -= 1
            else:
                newturtle[1] += 1
           
        elif direction == 'lt' or direction == 'rt':
            if penstatus:
                trace = '-'
            else:
                trace = ' '
            
            if direction == 'lt':
                newturtle[1] -= 1
            else:
                newturtle[1] += 1

        window.addch(newturtle[0], newturtle[1], trace)
    
    return trace
        

    

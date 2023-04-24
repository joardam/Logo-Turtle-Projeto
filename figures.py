import curses

def drawsquare(newturtle,window):
    for i in range(0, 12):
        newturtle[1] += 1
        trace = '-'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 6):
        newturtle[0] += 1
        trace = '|'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 12):
        newturtle[1] -= 1
        trace = '-'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 6):
        newturtle[0] -= 1
        trace = '|'
        window.addch(newturtle[0], newturtle[1], trace)
    
    return trace
    

def drawtriangle(newturtle,window):
    for i in range(0, 6):
        newturtle[0] -= 1
        newturtle[1] += 1
        trace = '/'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 7):
        newturtle[0] += 1
        newturtle[1] += 1
        trace = '\\'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 14):
        newturtle[1] -= 1
        trace = '-'
        window.addch(newturtle[0], newturtle[1], trace)
    
    return trace
    


def drawdiamond(newturtle,window):
    for i in range(0, 6):
        newturtle[0] -= 1
        newturtle[1] += 1
        trace = '/'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 6):
        newturtle[0] += 1
        newturtle[1] += 1
        trace = '\\'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 6):
        newturtle[0] += 1
        newturtle[1] -= 1
        trace = '/'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 6):
        newturtle[0] -= 1
        newturtle[1] -= 1
        trace = '\\'
        window.addch(newturtle[0], newturtle[1], trace)
    
    return trace
    

    
def drawcircle(newturtle, window):
    for i in range(0, 7):
        newturtle[1] += 1  
        trace = '-'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 2):
        newturtle[0] += 1  
        newturtle[1] += 1
        trace = '\\'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 2):
        newturtle[0] += 1  
        trace = '|'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 2):
        newturtle[0] += 1
        newturtle[1] -= 1   
        trace = '/'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 7):
        newturtle[1] -= 1   
        trace = '-'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 2):
        newturtle[0] -= 1
        newturtle[1] -= 1
        trace = '\\'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 2):
        newturtle[0] -= 1
        trace = '|'
        window.addch(newturtle[0], newturtle[1], trace)
    for i in range(0, 2):
        newturtle[0] -= 1
        newturtle[1] += 1
        trace = '/'
        window.addch(newturtle[0], newturtle[1], trace)
    
    return trace


def drawfigure(type, newturtle, window):
    if type == "sq":
       trace = drawsquare(newturtle, window)
    elif type == "tg":
        trace = drawtriangle(newturtle, window)
    elif type == "dm":
        trace = drawdiamond(newturtle, window)
    elif type == "ci":
        trace = drawcircle(newturtle, window)
    
    return trace
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#globale Variablen

WIDTH = 300
HEIGHT = 200
ball_radius = 50
BALL_RADIUS_INCREMENT = 3

# Handler für Keydown-Event
def keydown(key):
    global ball_radius
    
    # Füge hier Code hinzu, um den Ballradius zu verändern
    

# Handler zum Zeichen auf der Canvas
def draw(canvas):
    # Hinweis: Falls der Radius negativ wird, wird das Programm sich mit einem Fehler beenden
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Erzeuge ein Frame und registriere die Handler
frame = simplegui.create_frame("Dynamic Radius", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Starte die Frame-Animation
frame.start()





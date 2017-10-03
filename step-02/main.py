WIDTH=640
HEIGHT=320

''' declarations '''
frog = Actor("frog1")
frog.pos = (320,HEIGHT + frog.height )


''' game loop '''
# Event Handling


# Run Handling
def update():
    frog.y -= 5
    if frog.y < 0:
        frog.y = HEIGHT + frog.height


# Update the display
def draw():
    screen.fill((0,230,255))
    frog.draw()
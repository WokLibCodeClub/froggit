from random import randint

WIDTH=640
HEIGHT=320

''' declarations '''
frog = Actor("frog1")
frog.pos = (0, -500)
frog.frame = 1

def frog_hop():
    if frog.frame < 7:  
          frog.frame += 0.5 
    else:
          frog.frame = 1
    frog.image = "frog" + str(int(frog.frame))
  


''' game loop '''
def frog_reset():
    x = randint(0 + frog.width // 2, WIDTH - frog.width // 2)
    y = randint(HEIGHT + frog.height // 2, HEIGHT * 2)
    frog.pos = (x,y)


# Run Handling

def update():
    frog_hop()
    frog.y -= 5
    if frog.y < 0:
        frog_reset()


# Update the display
def draw():
    screen.fill((0,230,255))
    frog.draw()
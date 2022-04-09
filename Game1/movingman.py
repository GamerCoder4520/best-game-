WIDTH = 500
HEIGHT = 500
alien = Actor('yellow')
alien.pos = (300,50)
box = Rect((20, 20), (100, 100))
def draw():
    screen.clear()
    screen.draw.filled_rect(box,"blue")
    alien.draw()
def update():
    if keyboard.right:
        alien.x = alien.x + 10
    elif keyboard.left:
        alien.x = alien.x - 10
    elif keyboard.up:
        alien.y = alien.y - 10
    elif keyboard.down:
        alien.y = alien.y + 10
    #box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
    if alien.colliderect(box):
        print("hit")


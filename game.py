import tkinter as tk
import random
from PIL import ImageTk, Image

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

pac_queue = []
dot_queue = []

class Pacman:
    def __init__(self, canvas):
        self.x = 100
        self.y = 100
        self.turning_side = 0 # 0 = right, 1 = down, 2 = left, 3 = up
        self.draw(canvas)

    def draw(self, canvas):
        if len(pac_queue) != 0:
            canvas.delete(pac_queue[0]) # delete pacman from the canvas
            pac_queue.pop()
        
        # using image on canvas
        if self.turning_side == 0:
            image = Image.open("pac_img_right.jpg")
        elif self.turning_side == 1:
            image = Image.open("pac_img_down.jpg")
        elif self.turning_side == 2:
            image = Image.open("pac_img_left.jpg")
        elif self.turning_side == 3:
            image = Image.open("pac_img_up.jpg")
        image = image.resize((100,100), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)
        x = canvas.create_image(self.x, self.y, image=my_img)
        canvas.image = my_img # append to canvas so the picture is persistent

        # in case of using circle instead of image
        #size = 30
        #x = canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill='yellow')
        
        pac_queue.append(x)
    
    def moveLeft(self, event, canvas):
        self.x -= 5
        self.turning_side = 2
        self.draw(canvas)
    
    def moveRight(self, event, canvas):
        self.x += 5
        self.turning_side = 0
        self.draw(canvas)

    def moveUp(self, event, canvas):
        self.y -= 5
        self.turning_side = 3
        self.draw(canvas)

    def moveDown(self, event, canvas):
        self.y += 5
        self.turning_side = 1
        self.draw(canvas)

class Dot:
    def __init__(self, canvas):
        # random position
        self.x = random.randrange(WINDOW_WIDTH)
        self.y = random.randrange(WINDOW_HEIGHT)
        self.draw(canvas)

    # draw a dot on canvas
    def draw(self, canvas):
        size = 5
        x = canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill='white')
        dot_queue.append(x)
    
    # reassign random position
    def changePos(self):
        self.x = random.randrange(WINDOW_WIDTH)
        self.y = random.randrange(WINDOW_HEIGHT)

# check if pacman is on top of dot or not
def check(pacman, dot, canvas, window):
    if pacman.x - 30 <= dot.x <= pacman.x + 30\
        and pacman.y - 30 <= dot.y <= pacman.y + 30:
        canvas.delete(dot_queue[0]) # delete dot from the canvas
        dot_queue.pop()
        dot.changePos()
        dot.draw(canvas)
    window.after(100, check, pacman, dot, canvas, window) # use check() every 100 milliseconds


def main():
    window = tk.Tk()
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black') # Canvas widget is for drawing
    canvas.pack() # pack() organize, aka update, widgets onto canvas

    pacman = Pacman(canvas)
    window.bind("<KeyPress-Left>", lambda event: pacman.moveLeft(event, canvas)) # need to pass event, otherwise won't work
    window.bind("<KeyPress-Right>", lambda event: pacman.moveRight(event, canvas))
    window.bind("<KeyPress-Up>", lambda event: pacman.moveUp(event, canvas))
    window.bind("<KeyPress-Down>", lambda event: pacman.moveDown(event, canvas))
    
    dot = Dot(canvas)
    
    window.after(100, check, pacman, dot, canvas, window) # call check() to check dot&pacman after 100 milliseconds
    window.mainloop() # tk.mainloop() -> keep looping until there's an update

main()
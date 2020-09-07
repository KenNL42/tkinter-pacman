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
        self.draw(canvas)

    def draw(self, canvas):
        #print(self.x)
        size = 30
        if len(pac_queue) != 0:
            canvas.delete(pac_queue[0])
            pac_queue.pop()
        
        #pic = ImageTk.PhotoImage(Image.open("pac_img.jpg"))
        image = Image.open("pac_img2.jpg")
        image = image.resize((100,100), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)
        x = canvas.create_image(self.x, self.y, image=my_img)
        canvas.image = my_img

        #x = canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill='yellow')
        
        pac_queue.append(x)
    
    def moveLeft(self, event, canvas):
        self.x -= 5
        self.draw(canvas)
    
    def moveRight(self, event, canvas):
        self.x += 5
        self.draw(canvas)

    def moveUp(self, event, canvas):
        self.y -= 5
        self.draw(canvas)

    def moveDown(self, event, canvas):
        self.y += 5
        self.draw(canvas)

class Dot:
    def __init__(self, canvas):
        self.x = random.randrange(WINDOW_WIDTH)
        self.y = random.randrange(WINDOW_HEIGHT)
        self.draw(canvas)

    
    def draw(self, canvas):
        size = 5
        x = canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill='white')
        dot_queue.append(x)
    
    def changePos(self):
        self.x = random.randrange(WINDOW_WIDTH)
        self.y = random.randrange(WINDOW_HEIGHT)

'''    def check(self, canvas, pacman, window):
        print('is checking')
        if pacman.x - 30 <= self.x <= pacman.x + 30\
            and pacman.y - 30 <= self.y <= pacman.y + 30:
            canvas.delete(dot_queue[0])
            dot_queue.pop()
            #new_dot = Dot(canvas)
            self = Dot(canvas)
            #window.after(100, lambda event: self.check(lambda event: pacman, dot, canvas, window, window))
            window.after(100, self.check, canvas, pacman, window)
'''
def check(pacman, dot, canvas, window):
    if pacman.x - 30 <= dot.x <= pacman.x + 30\
        and pacman.y - 30 <= dot.y <= pacman.y + 30:
        canvas.delete(dot_queue[0])
        dot_queue.pop()
        dot.changePos()
        dot.draw(canvas)
        
        #window.after(100, lambda event: self.check(lambda event: pacman, dot, canvas, window, window))
        #window.after(100, dot.check, canvas, pacman, window)
    window.after(100, check, pacman, dot, canvas, window)


def main():

    
    window = tk.Tk()
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black') # Canvas widget is for drawing
    canvas.pack() # pack() organize, aka update, widgets onto canvas

    pacman = Pacman(canvas)
    window.bind("<KeyPress-Left>", lambda event: pacman.moveLeft(event, canvas), add="+")
    window.bind("<KeyPress-Right>", lambda event: pacman.moveRight(event, canvas), add="+")
    window.bind("<KeyPress-Up>", lambda event: pacman.moveUp(event, canvas), add="+")
    window.bind("<KeyPress-Down>", lambda event: pacman.moveDown(event, canvas), add="+")
    
    dot = Dot(canvas)
    
    window.after(100, check, pacman, dot, canvas, window)
    
    #window.bind("<KeyPress-Left>", check(pacman, dot, canvas, window), add="+")
    #window.bind("<KeyPress-Right>", check(pacman, dot, canvas, window), add="+")
    #window.bind("<KeyPress-Up>", check(pacman, dot, canvas, window), add="+")
    #window.bind("<KeyPress-Down>", check(pacman, dot, canvas, window), add="+")
    
    #canvas.pack()
    window.mainloop() # tk.mainloop() -> keep looping until there's an update


main()
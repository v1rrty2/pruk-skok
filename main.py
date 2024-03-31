import tkinter as tk
import time
import random
root = tk.Tk()
root.title("Прыг-скок")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = tk.Canvas(root,width=1500,height=1000,bd=0,highlightthickness=0)
canvas.pack()
root.update()
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas =canvas
        self.paddle = paddle
        self.id = canvas.create_oval(30,30,75,75,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-2,-1,1,2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # возвращаем метку о том, что мы успешно коснулись
                return True
        # возвращаем False — касания не было
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.y = -2
        if self.hit_paddle(pos) == True:
            self.x = -2
        if pos[0] <= 0:
            self.x= 2
        if pos[2] >= self.canvas_width:
            self.x = -2
class Paddle:
    def __init__(self,canvas,color):
        self.canvas =canvas
        self.id = canvas.create_rectangle(0,0,400,40,fill=color)
        self.canvas.move(self.id,500,700)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        pass
    def turn_right(self,event):
        self.x = 2
    def turn_left(self,event):
        self.x = -2
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
paddle = Paddle(canvas,"black")
ball = Ball(canvas,paddle,"red")
while True:
    ball.draw()
    paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)


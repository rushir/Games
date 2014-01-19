##Snake
from livewires import games, color
games.init(screen_width=1000, screen_height=500, fps=50)
class tail(games.Sprite):
    tail=games.load_image("tail.png")
    def __init__(self, x, y):
        super(tail, self).__init__(image=tail.tail, x=x, y=y)
class sect(games.Sprite):
    pic=games.load_image("vert.png", transparent=False)
    def __init__(self, x, y):
        super(sect, self).__init__(image=sect.pic, x=x, y=y)
class one(games.Sprite):
    pic=games.load_image("C1.png")
    def __init__(self, x, y):
        super(one, self).__init__(image=one.pic, x=x, y=y)
class two(games.Sprite):
    pic=games.load_image("C2.png")
    def __init__(self, x, y):
        super(two, self).__init__(image=two.pic, x=x, y=y)
class three(games.Sprite):
    pic=games.load_image("C3.png")
    def __init__(self, x, y):
        super(three, self).__init__(image=three.pic, x=x, y=y)
class four(games.Sprite):
    pic=games.load_image("C4.png")
    def __init__(self, x, y):
        super(four, self).__init__(image=four.pic, x=x, y=y)
class snake(games.Sprite):
    """Player's controllable snake"""
    head=games.load_image("head.png")
    def __init__(self, x, y):
        """Creates class"""
        super(snake, self).__init__(image=snake.head, x=x, y=y)
        self.mid=sect(self.x, self.y+20)
        self.tail=tail(self.x, self.mid.y+20)
        self.tail.angle=180
        games.screen.add(self.mid)
        games.screen.add(self.tail)
    def update(self):
        """moves snake"""
        move()
    def move(self):
        """moves snake"""
        if self.head.angle==0:
            self.hy=self.head.y
            self.head.y+=20
hiss=snake(500, 250)
games.screen.add(hiss)
games.screen.mainloop()
        

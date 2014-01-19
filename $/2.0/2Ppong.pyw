##UniPong
from  livewires import games, color
import random
games.music.load("pacmanfever.mp3")
games.init(screen_width=1000, screen_height=500, fps=50)
class leftpaddle(games.Sprite):
    """Paddle on the left that bounces the ball off"""
    pic=games.load_image("vertical.png", transparent=False)
    def __init__(self):
        """Creates paddle and a score counter"""
        super(leftpaddle, self).__init__(image=leftpaddle.pic, y=games.screen.height/2, left=5)
        self.points=games.Text(value=0, size=50, color=color.blue, top=5, left=20)
        games.screen.add(self.points)
    def update(self):
        """Checks for user input"""
        if games.keyboard.is_pressed(games.K_UP):
            self.y-=3
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y+=3
        if self.top<0:
            self.top=0
        if self.bottom>games.screen.height:
            self.bottom=games.screen.height
        self.findbounce()
    def findbounce(self):
        """Bounces the ball if they touch"""
        for ball in self.overlapping_sprites:
            self.points.value+=5
            self.points.left=20
            if ball.bottom==self.top or ball.top==self.bottom:
                ball.sidebounce()
            else:
                ball.bounce()
class rightpaddle(games.Sprite):
    """Paddle on the right that bounces the ball off"""
    pic=games.load_image("redvertical.png", transparent=False)
    def __init__(self):
        """Creates paddle and score counter"""
        super(rightpaddle, self).__init__(image=rightpaddle.pic, y=games.screen.height/2, right=games.screen.width-5)
        self.points=games.Text(value=0, size=50, color=color.red, top=5, right=games.screen.width-20)
        games.screen.add(self.points)
    def update(self):
        """Checks for user input"""
        if games.keyboard.is_pressed(games.K_KP8):
            self.y-=3
        if games.keyboard.is_pressed(games.K_KP2):
            self.y+=3
        if self.top<0:
            self.top=0
        if self.bottom>games.screen.height:
            self.bottom=games.screen.height
        self.findbounce()
    def findbounce(self):
        """Bounces the ball if touching"""
        for ball in self.overlapping_sprites:
            self.points.value+=5
            self.points.right=games.screen.width-20
            if ball.bottom==self.top or ball.top==self.bottom:
                ball.sidebounce()
            else:
                ball.bounce()
class ball(games.Sprite):
    """Ball that bounces around and ends the game if it hits either end"""
    pic=games.load_image("ball.png")
    speed=3
    ydirection=random.choice([speed*-1, speed])
    xdirection=random.choice([speed*-1, speed])
    sy=random.randint(10, games.screen.height-10)
    sx=random.randint(250, 750)
    def __init__(self, x=sx, y=sy):
        """Creates ball"""
        super(ball, self).__init__(image=ball.pic, x=x, y=y, dx=ball.xdirection, dy=ball.ydirection)
    def update(self):
        """Bounces off sides and ends game if it hits the end"""
        if self.top<0 or self.bottom>games.screen.height:
            self.dy=-self.dy
        if self.left<0:
            self.P2gameover()
            self.destroy()
        if self.right>games.screen.width:
            self.P1gameover()
            self.destroy()
    def bounce(self):
        """Reverses x velocity"""
        self.dx=-self.dx
    def sidebounce(self):
        """Reverses y velocity"""
        self.dy=-self.dy
    def P1gameover(self):
        """Ends the game"""
        GameOver=games.Message(value="GAME OVER", size=100, color=color.blue, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit)
        games.screen.add(GameOver)
    def P2gameover(self):
        """Ends the game"""
        GameOver=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit)
        games.screen.add(GameOver)
background=games.load_image("background.png", transparent=False)
games.screen.background=background
P1=leftpaddle()
games.screen.add(P1)
P2=rightpaddle()
games.screen.add(P2)
Ball=ball()
games.screen.add(Ball)
games.mouse.is_visible=False
games.screen.event_grab=False
games.music.play(-1)
games.screen.mainloop()

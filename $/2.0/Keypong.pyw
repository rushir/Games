##UniPong
from  livewires import games, color
import random
games.init(screen_width=1000, screen_height=500, fps=50)
class paddle(games.Sprite):
    """Paddle that will bounce the ball off of it and is controlled by the user"""
    pic=games.load_image("paddle.png", transparent=False)
    def __init__(self):
        """Creates the paddle and adds a point counter"""
        super(paddle, self).__init__(image=paddle.pic, x=games.screen.width/2, bottom=games.screen.height-5)
        self.points=games.Text(value=0, size=50, color=color.white, top=5, right=games.screen.width-5)
        games.screen.add(self.points)
    def update(self):
        """Checks for user input"""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x-=5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x+=5
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
        self.findbounce()
    def findbounce(self):
        """Repels the ball if they touch"""
        for ball in self.overlapping_sprites:
            self.points.value+=5
            self.points.right=games.screen.width-5
            if ball.bottom==self.top or ball.top==self.bottom:
                ball.sidebounce()
            else:
                ball.bounce()
class ball(games.Sprite):
    """Ball that bounces around the screen and ends the game if it hits the bottom"""
    pic=games.load_image("ball.png")
    speed=2
    direction=random.choice([speed*-1, speed])
    sx=random.randint(1, games.screen.width-1)
    sy=random.randint(1, games.screen.height/2)
    def __init__(self, x=sx, y=sy):
        """creates the ball"""
        super(ball, self).__init__(image=ball.pic, x=x, y=y, dx=ball.speed, dy=ball.speed)
    def update(self):
        """Makes the ball bounce off walls and triggers gameover() if it hits the bottom"""
        if self.left<0 or self.right>games.screen.width:
            self.dx=-self.dx
        if self.top<0:
            self.dy=-self.dy
        if self.bottom>games.screen.height:
            self.gameover()
            self.destroy()
    def bounce(self):
        """Reverses the ball's y velocity"""
        self.dy=-self.dy
    def sidebounce(self):
        """reverses the ball's x velocity"""
        self.dx=-self.dx
    def gameover(self):
        """Ends the game"""
        GameOver=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit)
        games.screen.add(GameOver)
background=games.load_image("background.png", transparent=False)
games.screen.background=background
Paddle=paddle()
games.screen.add(Paddle)
Ball=ball()
games.screen.add(Ball)
games.mouse.is_visible=False
games.screen.event_grab=True
games.screen.mainloop()

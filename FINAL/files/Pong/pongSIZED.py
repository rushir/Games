from livewires import games, color
import os
games.init(screen_width=1200, screen_height=700, fps=100)
games.music.load(os.getcwd()+"\\files\\"+"\\Pong\\"+"Thunder.mp3")
games.music.play(-1)
class pong2(games.Sprite):
    """making the pong ball sprite."""
    bball=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"bball.png")
    bball2=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"bball2.png")
    bball3=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"bball3.png")
    bball4=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"bball4.png")
    zeus=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"zeus.png")
    bballs=[bball, bball2, bball3, bball4, zeus]
    def __init__(self, x, y, dx, dy):
        """declaring the moving of the pong ball(s)"""
        super(pong2, self).__init__(image=pong2.bball, x=x, y=y, dx=dx, dy=dy)
        self.dx1=self.dx
        self.dy1=self.dy
        self.dx, self.dy=0, 0
        self.count=1
        self.picture=0
    def update(self):
        """updating the movment of the ball and counting your points"""
        if self.count:
            if self.count>=games.screen.fps*1.5:
                self.dx=self.dx1
                self.dy=self.dy1
                self.count=None
        if self.left<0:
            self.sidebounce()
        if self.right>games.screen.width:
            self.sidebounce()
        if self.top<0:
            self.vertbounce()
        if self.bottom>games.screen.height:
            self.die()
        if self.count:
            self.count+=1
    def sidebounce(self):
        """declaring the ball bouncing sideways"""
        self.dx=-self.dx
    def vertbounce(self):
        """declaring the ball bouncing up and down"""
        self.dy=-self.dy
    def die(self):
        """This def makes the game quit after a certain amount of time"""
        GrimReaper=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=1*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
        games.screen.add(GrimReaper)
    def ballchange(self):
        """changing of balls based on level"""
        self.picture+=1
        self.image=pong2.bballs[self.picture]
        if self.image==pong2.zeus:
            wow=games.Message(value="YOU NEED TO GET A LIFE!!!", size=75, color=color.white, left=5, top=5, lifetime=10*games.screen.fps, after_death=None, is_collideable=False)
            games.screen.add(wow)
class paddle(games.Sprite):
    """importing the paddle image"""
    paddle2=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"paddle.png")
    
    def __init__(self, x, y):
        """moving of the paddle"""
        super(paddle, self).__init__(image=paddle.paddle2, x=x, y=y)
        self.points=games.Text(value=0, size=50, color=color.white, top=5, right=games.screen.width-5)
        games.screen.add(self.points)
    def update(self):
        """updating the paddle with your arrow key hits"""
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x-=5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x+=5
        self.checkball()
        self.points.right=games.screen.width-5
    def checkball(self):
        """this is the def that makes the ball count 10 points everytime it touchs the paddle"""
        for ball in self.overlapping_sprites:
            ball.vertbounce()
            self.points.value+=10
            if self.points.value==500:
                ball.ballchange()
            elif self.points.value==2000:
                ball.ballchange()
            elif self.points.value==4500:
                ball.ballchange()
            elif self.points.value==10000:
                ball.ballchange()


back=games.load_image(os.getcwd()+"\\files\\"+"\\Pong\\"+"Pbackground.png")
games.screen.background=back
p=paddle(600, 675)
ball=pong2(600, 400, 5, 5)
games.screen.add(p)
games.screen.add(ball)
games.screen.mainloop()

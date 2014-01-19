##Brixx
from livewires import games, color
import math
games.init(screen_width=1000, screen_height=500, fps=50)
back=games.load_image("back.png", transparent=False)
games.screen.background=back
class brixA(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image("brixA.png", transparent=False)
    def __init__(self, x, y, game):
        """Creates brix"""
        super(brixA, self).__init__(x=x, y=y, image=brixA.pic)
        self.hits=1
        self.game=game
        self.game.total+=1
    def update(self):
        """Bounces ball off and dies if hit"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
            self.die()
    def die(self):
        """Loses a hit, if all hits are gone it is destroyed"""
        self.hits-=1
        if self.hits<=0:
            self.destroy()
            self.game.total-=1
class brixB(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image("brixB.png", transparent=False)
    def __init__(self, x, y, game):
        """Creates brix"""
        super(brixB, self).__init__(x=x, y=y, image=brixB.pic)
        self.hits=2
        self.game=game
        self.game.total+=1
    def update(self):
        """Bounces ball off and dies if hit"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
            self.die()
    def die(self):
        """Loses a hit, if all hits are gone it is destroyed"""
        self.hits-=1
        if self.hits<=0:
            self.destroy()
            self.game.total-=1
class brixC(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image("brixC.png", transparent=False)
    def __init__(self, x, y, game):
        """Creates brix"""
        super(brixC, self).__init__(x=x, y=y, image=brixC.pic)
        self.hits=3
        self.game=game
        self.game.total+=1
    def update(self):
        """Bounces ball off and dies if hit"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
            self.die()
    def die(self):
        """Loses a hit, if all hits are gone it is destroyed"""
        self.hits-=1
        if self.hits<=0:
            self.destroy()
            self.game.total-=1
class brixD(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image("brixD.png", transparent=False)
    def __init__(self, x, y, game):
        """Creates brix"""
        super(brixD, self).__init__(x=x, y=y, image=brixD.pic)
        self.hits=4
        self.game=game
        self.game.total+=1
    def update(self):
        """Bounces ball off and dies if hit"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
            self.die()
    def die(self):
        """Loses a hit, if all hits are gone it is destroyed"""
        self.hits-=1
        if self.hits<=0:
            self.destroy()
            self.game.total-=1
class brixE(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image("brixE.png", transparent=False)
    def __init__(self, x, y, game):
        """Creates brix"""
        super(brixE, self).__init__(x=x, y=y, image=brixE.pic)
        self.hits=5
        self.game=game
        self.game.total+=1
    def update(self):
        """Bounces ball off and dies if hit"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
            self.die()
    def die(self):
        """Loses a hit, if all hits are gone it is destroyed"""
        self.hits-=1
        if self.hits<=0:
            self.destroy()
            self.game.total-=1
class brixF(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image("brixF.png", transparent=False)
    def __init__(self, x, y, game):
        """Creates brix"""
        super(brixF, self).__init__(x=x, y=y, image=brixF.pic)
        self.hits=10
        self.game=game
        self.game.total+=1
    def update(self):
        """Bounces ball off and dies if hit"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
            self.die()
    def die(self):
        """Loses a hit, if all hits are gone it is destroyed"""
        self.hits-=1
        if self.hits<=0:
            self.destroy()
            self.game.total-=1
class ball(games.Sprite):
    """Ball that bounces off objects"""
    pic=games.load_image("b1.png")
    def __init__(self, x, y, dx, dy):
        """Creates ball"""
        super (ball, self).__init__(x=x, y=y, dx=dx, dy=dy, image=ball.pic)
        self.permx=dx
        self.d=1
    def update(self):
        """bounces off sides"""
        if self.left<0 or self.right>games.screen.width:
            self.sidebounce()
        if self.top<=0:
            self.top=1
            self.vertbounce()
        if self.dx>0:
            self.d=2
        if self.dx<0:
            self.d=1
    def sidebounce(self):
        """Reverses x velocity"""
        self.dx=-self.dx
        self.d+=1
    def vertbounce(self):
        """reverses y velocity"""
        self.dy=-self.dy
    def leftbounce(self):
        """Bounces leftwards"""
        self.dy=-self.dy
        if not self.dx<=-10:
            self.dx-=4
    def rightbounce(self):
        """Bounces rightwards"""
        self.dy=-self.dy
        if not self.dx>=10:
            self.dx+=4
class p1(games.Sprite):
    """Player controlled paddle"""
    pic=games.load_image("p1.png", transparent=False)
    def __init__(self, y):
        """Creates paddle"""
        super(p1, self).__init__(x=games.screen.width/2, y=y, image=p1.pic)
    def update(self):
        """gets user input"""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x-=8
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x+=8
        self.checkball()
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
    def checkball(self):
        """Bounces a ball in one of three directions, depending on where it hits"""
        for ball in self.overlapping_sprites:
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
class game(games.Sprite):
    pic=games.load_image("blank.png")
    def __init__(self):
        super(game, self).__init__(image=game.pic, x=-1, y=-1, is_collideable=False)
        self.total=0
        self.makebrix()
    def makebrix(self):
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=5, game=self)
            games.screen.add(bf)
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=15, game=self)
            games.screen.add(bf)
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=25, game=self)
            games.screen.add(bf)
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=35, game=self)
            games.screen.add(bf)
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=45, game=self)
            games.screen.add(bf)
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=55, game=self)
            games.screen.add(bf)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=65, game=self)
            games.screen.add(be)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=75, game=self)
            games.screen.add(be)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=85, game=self)
            games.screen.add(be)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=95, game=self)
            games.screen.add(be)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=105, game=self)
            games.screen.add(be)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=115, game=self)
            games.screen.add(be)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=125, game=self)
            games.screen.add(bd)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=135, game=self)
            games.screen.add(bd)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=145, game=self)
            games.screen.add(bd)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=155, game=self)
            games.screen.add(bd)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=165, game=self)
            games.screen.add(bd)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=175, game=self)
            games.screen.add(bd)
player=p1(490)
b=ball(500, 250, 6, 5)
control=game()
games.screen.add(control)
games.screen.add(player)
games.screen.add(b)
games.screen.mainloop()

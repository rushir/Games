##Brixx
from livewires import games, color
import math
import os
games.init(screen_width=1000, screen_height=500, fps=50)
back=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"back.png", transparent=False)
games.screen.background=back
class brixA(games.Sprite):
    """Block that dissapears if hit once"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"brixA.png", transparent=False)
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
    """Block that dissapears if hit twice"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"brixB.png", transparent=False)
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
    """Block that dissapears if hit thrice"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"brixC.png", transparent=False)
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
    """Block that dissapears if hit four times"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"brixD.png", transparent=False)
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
    """Block that dissapears if hit 5 times"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"brixE.png", transparent=False)
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
    """Block that dissapears if hit 10 times"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"brixF.png", transparent=False)
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
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"b1.png")
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
        if self.top>games.screen.height:
            loser=games.Message(value="GAME OVER", color=color.red, size=100, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False, x=games.screen.width/2, y=games.screen.height/2)
            games.screen.add(loser)
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
        if self.dx!=-5:
            self.dx-=2
    def rightbounce(self):
        """Bounces rightwards"""
        self.dy=-self.dy
        if self.dx!=5:
            self.dx+=2
class p1(games.Sprite):
    """Player controlled paddle"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"p1.png", transparent=False)
    def __init__(self, y):
        """Creates paddle"""
        super(p1, self).__init__(x=games.screen.width/2, y=y, image=p1.pic)
    def update(self):
        """gets user input"""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x-=4.5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x+=4.5
        self.checkball()
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
    def checkball(self):
        """Bounces a ball in one of three directions, depending on where it hits"""
        for ball in self.overlapping_sprites:
            ball.bottom=self.top
            if math.fabs(ball.x-self.x)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.x)<math.fabs(ball.x-self.right):
                ball.vertbounce()
            if math.fabs(ball.x-self.left)<math.fabs(ball.x-self.x) and math.fabs(ball.x-self.left)<math.fabs(ball.x-self.right):
                ball.leftbounce()
            if math.fabs(ball.x-self.right)<math.fabs(ball.x-self.left) and math.fabs(ball.x-self.right)<math.fabs(ball.x-self.x):
                ball.rightbounce()
class game(games.Sprite):
    """Class that controls the game"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Brixx\\"+"blank.png")
    def __init__(self):
        """Creates class, makes brixx"""
        super(game, self).__init__(image=game.pic, x=-1, y=-1, is_collideable=False)
        self.total=0
        self.makebrix()
    def update(self):
        """Checks if all brixx are gone"""
        if self.total==0:
            WINNING=games.Message(value="YOU WON", color=color.red, size=100, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False, x=games.screen.width/2, y=games.screen.height/2)
            games.screen.add(WINNING)
    def makebrix(self):
        """Creates brixx"""
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=25, game=self)
            games.screen.add(bf)
        for f in range(0, 10):
            xv=50+(100*f)
            bf=brixF(x=xv, y=75, game=self)
            games.screen.add(bf)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=125, game=self)
            games.screen.add(be)
        for e in range(0, 10):
            xv=50+(100*e)
            be=brixE(x=xv, y=175, game=self)
            games.screen.add(be)
        for d in range(0, 10):
            xv=50+(100*d)
            bd=brixD(x=xv, y=225, game=self)
            games.screen.add(bd)
        for c in range(0, 10):
            xv=50+(100*c)
            bc=brixC(x=xv, y=275, game=self)
            games.screen.add(bc)
        for b in range(0, 10):
            xv=50+(100*b)
            bb=brixB(x=xv, y=325, game=self)
            games.screen.add(bb)
        for a in range(0, 10):
            xv=50+(100*a)
            ba=brixA(x=xv, y=375, game=self)
            games.screen.add(ba)
player=p1(490)
b=ball(500, 425, 1, 3)
control=game()
games.screen.add(control)
games.screen.add(player)
games.screen.add(b)
games.screen.mainloop()

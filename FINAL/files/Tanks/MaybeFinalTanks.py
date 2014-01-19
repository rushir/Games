##TANKS
from livewires import games, color
import math
import random
import os
games.init(screen_width=1000, screen_height=500, fps=50)
background=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"Tbackground.png", transparent=False)
games.screen.background=background
games.music.load(os.getcwd()+"\\files\\"+"\\Tanks\\"+"eyeofthetiger.mp3")
games.music.play(-1)
class tankone(games.Sprite):
    """Player one's tank"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"tank1.png")
    def __init__(self, x, y):
        """Creates tank and sets up variables"""
        super(tankone, self).__init__(image=tankone.pic, x=x, y=y)
        self.shottime=0
    def update(self):
        """Checks for player input and moves tank accordingly"""
        self.shottime+=1
        if games.keyboard.is_pressed(games.K_UP):
            self.angle=00
            self.y-=3
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle=90
            self.x+=3
        if games.keyboard.is_pressed(games.K_DOWN):
            self.angle=180
            self.y+=3
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle=270
            self.x-=3
        if games.keyboard.is_pressed(games.K_SPACE) and self.shottime>=125:
            if self.angle==0:
                S1=shot(self.x, self.top, self.angle)
                games.screen.add(S1)
            if self.angle==90:
                S2=shot(self.right, self.y, self.angle)
                games.screen.add(S2)
            if self.angle==180:
                S3=shot(self.x, self.bottom, self.angle)
                games.screen.add(S3)
            if self.angle==270:
                S4=shot(self.left, self.y, self.angle)
                games.screen.add(S4)
            self.shottime=0
        if self.left<=0:
            self.left=0
        if self.top<=0:
            self.top=0
        if self.right>=games.screen.width:
            self.right=games.screen.width
        if self.bottom>=games.screen.height:
            self.bottom=games.screen.height
    def die(self):
        """Destroys tank and adds end message"""
        GameOver=games.Message(value="PLAYER TWO WON", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
        games.screen.add(GameOver)
        self.destroy()
    def midleft(self):
        """Makes tank not go through wall"""
        self.right=483
    def midup(self):
        """Makes tank not go through wall"""
        self.bottom=49
    def midright(self):
        """Makes tank not go through wall"""
        self.left=516
    def middown(self):
        """Makes tank not go through wall"""
        self.top=450
    def leftdown(self):
        """Makes tank not go through wall"""
        self.top=271
    def leftup(self):
        """Makes tank not go through wall"""
        self.bottom=238
    def leftleft(self):
        """Makes tank not go through wall"""
        self.right=294
    def leftright(self):
        """Makes tank not go through wall"""
        pass
    def rightdown(self):
        """Makes tank not go through wall"""
        self.top=271
    def rightup(self):
        """Makes tank not go through wall"""
        self.bottom=238
    def rightright(self):
        """Makes tank not go through wall"""
        pass
    def rightleft(self):
        """Makes tank not go through wall"""
        self.left=695
class tanktwo(games.Sprite):
    """Player two's tank"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"tank2.png")
    def __init__(self, x, y):
        """creates the tank and sets up variables"""
        super(tanktwo, self).__init__(image=tanktwo.pic, x=x, y=y)
        self.shottime=0
    def update(self):
        """Checks for player input"""
        self.shottime+=1
        if games.keyboard.is_pressed(games.K_KP8):
            self.angle=00
            self.y-=3
        if games.keyboard.is_pressed(games.K_KP6):
            self.angle=90
            self.x+=3
        if games.keyboard.is_pressed(games.K_KP5):
            self.angle=180
            self.y+=3
        if games.keyboard.is_pressed(games.K_KP4):
            self.angle=270
            self.x-=3
        if games.keyboard.is_pressed(games.K_KP0) and self.shottime>=125:
            if self.angle==0:
                S5=shot(self.x, self.top, self.angle)
                games.screen.add(S5)
            if self.angle==90:
                S6=shot(self.right, self.y, self.angle)
                games.screen.add(S6)
            if self.angle==180:
                S7=shot(self.x, self.bottom, self.angle)
                games.screen.add(S7)
            if self.angle==270:
                S8=shot(self.left, self.y, self.angle)
                games.screen.add(S8)
            self.shottime=0
        if self.left<=0:
            self.left=0
        if self.top<=0:
            self.top=0
        if self.right>=games.screen.width:
            self.right=games.screen.width
        if self.bottom>=games.screen.height:
            self.bottom=games.screen.height
    def die(self):
        """Destroys tank and adds end message"""
        GameOver=games.Message(value="PLAYER ONE WON", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
        games.screen.add(GameOver)
        self.destroy()
    def midleft(self):
        """Makes tank not able to run into wall"""
        self.right=483
    def midup(self):
        """Makes tank not able to run into wall"""
        self.bottom=49
    def midright(self):
        """Makes tank not able to run into wall"""
        self.left=516
    def middown(self):
        """Makes tank not able to run into wall"""
        self.top=450
    def leftdown(self):
        """Makes tank not able to run into wall"""
        self.top=271
    def leftup(self):
        """Makes tank not able to run into wall"""
        self.bottom=238
    def leftleft(self):
        """Makes tank not able to run into wall"""
        self.right=304
    def leftright(self):
        """Makes tank not able to run into wall"""
        pass
    def rightdown(self):
        """Makes tank not able to run into wall"""
        self.top=271
    def rightup(self):
        """Makes tank not able to run into wall"""
        self.bottom=238
    def rightright(self):
        """Makes tank not able to run into wall"""
        self.left=695
    def rightleft(self):
        """Makes tank not able to run into wall"""
        self.left=695
class shot(games.Sprite):
    """Bullet that bounces off walls and kills tanks"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"shot.png")
    def __init__(self, x, y, angle):
        """Creates bullet"""
        if angle==90:
            super(shot, self).__init__(image=shot.pic, left=x, y=y, dx=4)
            self.angle=angle
        if angle==00:
            super(shot, self).__init__(image=shot.pic, x=x, bottom=y, dy=-4)
            self.angle=angle
        if angle==180:
            super(shot, self).__init__(image=shot.pic, x=x, top=y, dy=4)
            self.angle=angle
        if angle==270:
            super(shot, self).__init__(image=shot.pic, right=x, y=y, dx=-4)
            self.angle=angle
        self.age=0
    def update(self):
        """moves according to angle"""
        if self.angle==00:
            self.y-=4
        if self.angle==90:
            self.x+=4
        if self.angle==180:
            self.y+=4
        if self.angle==270:
            self.x-=4
        for thing in self.overlapping_sprites:
            try:
                thing.die()
                self.destroy()
            except:
                self.leftbounce()
        if self.right>games.screen.width or self.left<0 or self.top<=0 or self.bottom>=games.screen.height:
            self.destroy()
    def die(self):
        """Destroys bullet"""
        self.destroy()
    def rightbounce(self):
        """Bounces off wall"""
        self.dx, self.dy=0, 0
        self.angle=90
    def leftbounce(self):
        """Bounces off wall"""
        self.dx, self.dy=0, 0
        self.angle=270
    def upbounce(self):
        """Bounces off wall"""
        self.dx, self.dy=0, 0
        self.angle=0
    def downbounce(self):
        """Bounces off wall"""
        self.dx, self.dy=0, 0
        self.angle=180
class midwall(games.Sprite):
    """Wall in the middle of the screen"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"vertwall.png", transparent=False)
    def __init__(self, x, y):
        """Creates wall"""
        super(midwall, self).__init__(image=midwall.pic, x=x, y=y)
    def update(self):
        """Checks for tanks and bullets and acts appropriately"""
        for tank in self.overlapping_sprites:
            if math.fabs(tank.left-self.right)<math.fabs(tank.right-self.left) and math.fabs(tank.left-self.right)<math.fabs(tank.top-self.bottom) and math.fabs(tank.left-self.right)<math.fabs(tank.bottom-self.top): 
                try:
                    tank.rightbounce()
                except:
                    #tank.left=self.right
                    tank.midright()
            elif math.fabs(tank.right-self.left)<math.fabs(tank.left-self.right) and math.fabs(tank.right-self.left)<math.fabs(tank.top-self.bottom) and math.fabs(tank.right-self.left)<math.fabs(tank.bottom-self.top):
                try:
                    tank.leftbounce()
                except:
                    #tank.right=self.left
                    tank.midleft()
            if math.fabs(tank.top-self.bottom)<math.fabs(tank.bottom-self.top) and math.fabs(tank.top-self.bottom)<math.fabs(tank.right-self.left) and math.fabs(tank.top-self.bottom)<math.fabs(tank.left-self.right):
                try:
                    tank.downbounce()
                except:
                    #tank.top=self.bottom
                    tank.middown()
            elif math.fabs(tank.bottom-self.top)<math.fabs(tank.top-self.bottom) and math.fabs(tank.bottom-self.top)<math.fabs(tank.right-self.left) and math.fabs(tank.bottom-self.top)<math.fabs(tank.left-self.right):
                try:
                    tank.upbounce()
                except:
                    #tank.bottom=self.top
                    tank.midup()
    def leftleft(self):
        """Avoids glitches"""
        pass
class leftwall(games.Sprite):
    """Wall on the left"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"leftwall.png", transparent=False)
    def __init__(self, x, y, mid):
        """Creates wall and assigns variables"""
        super(leftwall, self).__init__(image=leftwall.pic, left=x, y=y)
        self.mid=mid
    def update(self):
        """Bounces bullets and stops tanks if they overlap"""
        for tank in self.overlapping_sprites:
            if math.fabs(tank.left-self.right)<math.fabs(tank.right-self.left) and math.fabs(tank.left-self.right)<math.fabs(tank.top-self.bottom) and math.fabs(tank.left-self.right)<math.fabs(tank.bottom-self.top): 
                try:
                    tank.rightbounce()
                except:
                    #tank.left=self.right
                    tank.leftright()
            elif math.fabs(tank.right-self.left)<math.fabs(tank.left-self.right) and math.fabs(tank.right-self.left)<math.fabs(tank.top-self.bottom) and math.fabs(tank.right-self.left)<math.fabs(tank.bottom-self.top):
                try:
                    tank.leftbounce()
                except:
                    #tank.right=self.left
                    tank.leftleft()
            if math.fabs(tank.top-self.bottom)<math.fabs(tank.bottom-self.top) and math.fabs(tank.top-self.bottom)<math.fabs(tank.right-self.left) and math.fabs(tank.top-self.bottom)<math.fabs(tank.left-self.right):
                try:
                    tank.downbounce()
                except:
                    #tank.top=self.bottom
                    tank.leftdown()
            elif math.fabs(tank.bottom-self.top)<math.fabs(tank.top-self.bottom) and math.fabs(tank.bottom-self.top)<math.fabs(tank.right-self.left) and math.fabs(tank.bottom-self.top)<math.fabs(tank.left-self.right):
                try:
                    tank.upbounce()
                except:
                    #tank.bottom=self.top
                    tank.leftup()
    def midright(self):
        """Avoids glitches"""
        self.right=self.mid.left
    def midleft(self):
        """Avoids glitches"""
        self.right=self.mid.left
class rightwall(games.Sprite):
    """Wall on the right"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"rightwall.png", transparent=False)
    def __init__(self, x, y, mid):
        """Creates walll and assigns variables"""
        super(rightwall, self).__init__(image=rightwall.pic, left=x, y=y)
        self.mid=mid
    def update(self):
        """Bounces overlapping bullets and stops overlapping tanks"""
        for tank in self.overlapping_sprites:
            if math.fabs(tank.right-self.left)<math.fabs(tank.left-self.right) and math.fabs(tank.right-self.left)<math.fabs(tank.top-self.bottom) and math.fabs(tank.left-self.left)<math.fabs(tank.bottom-self.top): 
                try:
                    tank.leftbounce()
                except:
                    #tank.left=self.right
                    tank.rightright()
            elif math.fabs(tank.left-self.right)<math.fabs(tank.right-self.left) and math.fabs(tank.left-self.right)<math.fabs(tank.top-self.bottom) and math.fabs(tank.left-self.right)<math.fabs(tank.bottom-self.top):
                try:
                    tank.rightbounce()
                except:
                    #tank.right=self.left
                    tank.rightleft()
            if math.fabs(tank.top-self.bottom)<math.fabs(tank.bottom-self.top) and math.fabs(tank.top-self.bottom)<math.fabs(tank.right-self.left) and math.fabs(tank.top-self.bottom)<math.fabs(tank.left-self.right):
                try:
                    tank.downbounce()
                except:
                    #tank.top=self.bottom
                    tank.rightdown()
            elif math.fabs(tank.bottom-self.top)<math.fabs(tank.top-self.bottom) and math.fabs(tank.bottom-self.top)<math.fabs(tank.right-self.left) and math.fabs(tank.bottom-self.top)<math.fabs(tank.left-self.right):
                try:
                    tank.upbounce()
                except:
                    #tank.bottom=self.top
                    tank.rightup()
    def midleft(self):
        """Avoids glitches"""
        self.left=self.mid.right
    def midright(self):
        """Avoids glitches"""
        self.left=self.mid.right
class teleporter(games.Sprite):
    """Teleporter that sets objects to a random x, y and angle"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Tanks\\"+"teleporter.png")
    def __init__(self, x, y):
        """Creates teleporter"""
        super(teleporter, self).__init__(image=teleporter.pic, x=x, y=y)
    def update(self):
        """Checks for tanks and bullets and teleports them"""
        for tank in self.overlapping_sprites:
            tank.x=random.randint(0, games.screen.width)
            tank.y=random.randint(0, games.screen.height)
            tank.angle=random.choice([0, 90, 180, 270])
##Creates all objects and kicks off the game
P1=tankone(100, 250)
P2=tanktwo(900, 250)
wall=midwall(games.screen.width/2, games.screen.height/2)
lefty=leftwall(484, games.screen.height/2+5, wall)
righty=rightwall(510, games.screen.height/2+5, wall)
t1=teleporter(x=games.screen.width/2+50, y=games.screen.height/2-50)
t2=teleporter(x=games.screen.width/2-50, y=games.screen.height/2-50)
t3=teleporter(x=games.screen.width/2-50, y=games.screen.height/2+50)
t4=teleporter(x=games.screen.width/2+50, y=games.screen.height/2+50)
games.screen.add(wall)
games.screen.add(lefty)
games.screen.add(righty)
games.screen.add(P1)
games.screen.add(P2)
games.screen.add(t1)
games.screen.add(t2)
games.screen.add(t3)
games.screen.add(t4)
games.screen.mainloop()

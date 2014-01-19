##FlitePath
from livewires import games, color
import random
games.init(screen_width=1000, screen_height=500, fps=50)
class flier(games.Sprite):
    """Player controlled object that flies through a tunnel"""
    pic=games.load_image("flier.png")
    shieldedpic=games.load_image("shielded.png")
    def __init__(self, x, y):
        """Creates flier and sets up variables"""
        super(flier, self).__init__(image=flier.pic, x=x, y=y)
        self.shielded=False
        self.invinciblecount=50
        self.points=games.Text(value=0, size=50, color=color.white, right=games.screen.width-5, top=50, is_collideable=False)
        games.screen.add(self.points)
        self.booms=3
        self.shottime=75
        self.boomtime=50
    def update(self):
        """Checks for player input"""
        if self.top<0 or self.bottom>games.screen.height:
            self.kaboom()
        if games.keyboard.is_pressed(games.K_SPACE):#games.mouse.is_pressed(1):
            self.dy-=1
        else:
            self.dy+=1
        if games.keyboard.is_pressed(games.K_RSHIFT) and self.shottime>=75:
            self.normalshot()
            self.shottime=0
        if games.keyboard.is_pressed(games.K_RETURN) and self.booms>0 and self.boomtime>=50:
            self.boomer()
            self.booms-=1
            self.boomtime=0
        if self.dy>5:
            self.dy=5
        if self.dy<-5:
            self.dy=-5
        if self.shielded:
            self.image=flier.shieldedpic
        if not self.shielded:
            self.image=flier.pic
        self.points.elevate()
        self.invinciblecount+=1
        self.points.value+=1
        self.points.right=games.screen.width-50
        self.points.elevate()
        self.shottime+=1
        self.boomtime+=1
    def normalshot(self):
        """Creates a playershot"""
        s1=playershot(self.right, self.y)
        games.screen.add(s1)
    def boomer(self):
        """creates a playerboom"""
        b1=playerboom(self.right)
        games.screen.add(b1)
    def kaboom(self):
        """Dies if unshielded, loses shield if shielded"""
        if not self.shielded and self.invinciblecount>=50:
            self.destroy()
            GameOver=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
            games.screen.add(GameOver)
        elif self.shielded:
            self.shielded=False
            self.invinciblecount=0
    def playerkaboom(self):
        """Dies"""
        self.kaboom()
class playershot(games.Sprite):
    """Shot that kills one alien"""
    pic=games.load_image("shot1.png")
    def __init__(self, x, y):
        """Creates shot"""
        super(playershot, self).__init__(image=playershot.pic, left=x, y=y)
        self.dx=1
    def update(self):
        """Kills anything in its path"""
        for thing in self.overlapping_sprites:
            try:
                thing.kaboom()
            except:
                self.destroy()
        if self.left>=games.screen.width:
            self.destroy()
class playerboom(games.Sprite):
    """Sonic boom that kills everything in its path"""
    pic=games.load_image("boom.png", transparent=False)
    def __init__(self, x):
        """Creates boom"""
        super(playerboom, self).__init__(image=playerboom.pic, left=x, y=games.screen.height/2)
        self.dx=1
    def update(self):
        """kills everything it hits"""
        for thing in self.overlapping_sprites:
            try:
                thing.kaboom()
            except:
                pass
        if self.left>games.screen.width:
            self.destroy()
class normalalien(games.Sprite):
    """Alien that shoots at the player"""
    pic=games.load_image("alien.png")
    def __init__(self, x, y):
        """Creates alien"""
        super(normalalien, self).__init__(image=normalalien.pic, x=x, y=y)
        self.dx=-2
        self.guntime=random.randint(50, 100)
    def update(self):
        """shoots if the time is right and kills player if they touch"""
        for player in self.overlapping_sprites:
            try:
                player.playerkaboom()
            except:
                pass
        if self.guntime<=0:
            self.shoot()
            self.guntime=random.randint(100, 100)
        self.guntime-=1
    def shoot(self):
        """Shoots"""
        bang=alienshot(self.left, self.y)
        games.screen.add(bang)
    def kaboom(self):
        """Dies"""
        self.destroy()
class alienshot(games.Sprite):
    """Shot from the alien"""
    pic=games.load_image("shot2.png")
    def __init__(self, x, y):
        """creates shot"""
        super(alienshot, self).__init__(image=alienshot.pic, right=x-5, y=y, dx=-4)
    def update(self):
        """Destroys player if they overlap"""
        for thing in self.overlapping_sprites:
            try:
                thing.kaboom()
            except:
                self.destroy()
        if self.right<=0:
            self.destroy()
class block(games.Sprite):
    """Wall of the canyon"""
    pic=games.load_image("block.png", transparent=False)
    def __init__(self, x, y):
        """creates block"""
        super(block, self).__init__(image=block.pic, x=x, y=y)
        self.dx=-2
    def update(self):
        """Kills player if they overlap, moves"""
        for player in self.overlapping_sprites:
            try:
                player.kaboom()
            except:
                pass
        if self.left<0:
            self.destroy()
class shield(games.Sprite):
    """Shield powerup"""
    pic=games.load_image("shield.png")
    def __init__(self, x, y):
        """Creates shield"""
        super(shield, self).__init__(image=shield.pic, x=x, y=y)
        self.dx=-2
    def update(self):
        """Makes flier shielded if touched"""
        for flite in self.overlapping_sprites:
            try:
                flite.shielded=True
                self.destroy()
            except:
                self.destroy()
        if self.right<=0:
            self.destroy()
class point(games.Sprite):
    """Point bonus powerup"""
    pic=games.load_image("plus.png")
    def __init__(self, x, y):
        """Creates powerup"""
        super(point, self).__init__(image=point.pic, x=x, y=y)
        self.dx=-2
    def update(self):
        """Adds to total score if touched"""
        for thing in self.overlapping_sprites:
            try:
                thing.points.value+=100
                self.destroy()
            except:
                self.destroy()
        if self.right<=0:
            self.destroy()
class devastation(games.Sprite):
    """Powerdown that removes points and shield"""
    pic=games.load_image("BANKRUPT.png")
    def __init__(self, x, y):
        """Creates powerdown"""
        super(devastation, self).__init__(image=devastation.pic, x=x, y=y)
        self.dx=-2
    def update(self):
        """Bankrupts flier if touched"""
        for thing in self.overlapping_sprites:
            try:
                thing.points.value=0
                if thing.shielded:
                    thing.shielded=False
                self.destroy()
            except:
                self.destroy()
        if self.right<=0:
            self.destroy()
class walls(games.Sprite):
    """Walls of the canyon"""
    pic=games.load_image("block.png")
    def __init__(self):
        """Creates walls"""
        super(walls, self).__init__(image=walls.pic, x=0, y=0, is_collideable=False)
        self.counter=100
        self.space=games.screen.height
    def update(self):
        """Creates a pair of blocks at a random height if the time is right and adds powerups at random"""
        if self.counter%100==0:
            powerchance=random.randint(1, 50)
            alienchance=random.randint(1, 20)
            powerchoice=random.choice([-1, 0, 1])
            alienchoice=random.choice([-1, 0, 1])
            h=random.randint(-50, 50)
            block1=block(games.screen.width, h)
            h2=h+self.space
            block2=block(games.screen.width, h2)
            h3=h+(self.space/2)
            games.screen.add(block1)
            games.screen.add(block2)
            if powerchance==22:
                if powerchoice==1:
                    shield1=shield(x=block1.x, y=h3)
                    games.screen.add(shield1)
                if powerchoice==0:
                    point1=point(x=block1.x, y=h3)
                    games.screen.add(point1)
                if powerchoice==-1:
                    pointkiller=devastation(x=block1.x, y=h3)
                    games.screen.add(pointkiller)
            elif alienchance==17:
                a1=normalalien(x=block1.x, y=h3)
                games.screen.add(a1)
        self.counter+=2
        if self.counter%5000==0 and self.space>100:
            self.space-=50
f=flier(games.screen.width/2, games.screen.height/2)
games.screen.add(f)
wall=walls()
games.screen.add(wall)
games.screen.mainloop()

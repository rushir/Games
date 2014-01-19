##SphereWars
from livewires import color, games
import random
import math
games.init(screen_width=1000, screen_height=500, fps=50)
background=games.load_image(os.getcwd()+"\\files\\"+"\\Spheres\\"+"background.png", transparent=False)
games.screen.background=background
class shot(games.Sprite):
    """Ball that kills turret"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Spheres\\"+"ball.png")
    buffer=50
    def __init__(self, Tx, Ty, TAngle, Tpower):
        """Creates class and sets up variable"""
        angle=TAngle*math.pi/180
        xbuffer=shot.buffer*math.sin(angle)
        ybuffer=shot.buffer*-math.cos(angle)
        x=Tx+xbuffer
        y=Ty+ybuffer
        dx=(Tpower*math.sin(angle))/2
        dy=(Tpower*-math.cos(angle))/2
        super(shot, self).__init__(image=shot.pic, x=x, y=y, dx=dx, dy=dy)
        self.gravtime=5
        self.gravcount=0
    def update(self):
        """Simulates gravity and dies if past bottom, kills turret if they touch"""
        self.gravcount+=1
        if self.gravcount==self.gravtime:
            self.dy+=1
            self.gravcount=0
        if self.top>games.screen.height:
           self.die()
        for sphere in self.overlapping_sprites:
            try:
                sphere.die()
                self.die()
            except:
                self.die()
    def die(self):
        """Destroys ball"""
        self.destroy()
class game(object):
    """Containment class"""
    def __init__(self):
        """Starts game"""
        self.newgame()
        self.turn=random.randint(1, 2)
    def newgame(self):
        """starts new game"""
        games.screen.clear()
        P1=Sphere1(x=random.randint(0, games.screen.width/2), y=games.screen.height-50, game=self)
        P2=Sphere2(x=random.randint(games.screen.width/2, games.screen.width), y=games.screen.height-50, game=self)
        games.screen.add(P1)
        games.screen.add(P2)
    def changeplayer(self):
        """Switches players"""
        if self.turn==1:
            self.turn=2
        elif self.turn==2:
            self.turn=1
class Sphere1(games.Sprite):
    """Turret"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Spheres\\"+"Sphere1.png")
    def __init__(self, x, y, game):
        """Creates class"""
        super(Sphere1, self).__init__(image=Sphere1.pic, x=x, y=y)
        self.game=game
        self.power=0
        self.anglelevel=games.Text(value=self.angle, size=20, color=color.blue, top=30, left=5)
        self.powerlevel=games.Text(value=self.power, size=20, color=color.blue, top=5, left=5)
        games.screen.add(self.anglelevel)
        games.screen.add(self.powerlevel)
    def update(self):
        """Checks for user input"""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle-=1
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle+=1
        if games.keyboard.is_pressed(games.K_UP):
            self.power+=1
        if games.keyboard.is_pressed(games.K_DOWN):
            self.power-=1
        if self.game.turn==1 and games.keyboard.is_pressed(games.K_SPACE):
            self.shoot()
        self.anglelevel.value=self.angle
        self.powerlevel.value=self.power
        self.anglelevel.left=5
        self.powerlevel.left=5
    def shoot(self):
        """fires"""
        shot1=shot(Tx=self.x, Ty=self.y, TAngle=self.angle, Tpower=self.power)
        games.screen.add(shot1)
        self.game.changeplayer()
    def die(self):
        """Ends game"""
        Loser=games.Message(value="PLAYER TWO WON", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=3*games.screen.fps, after_death=self.game.newgame())
        games.screen.add(Loser)
class Sphere2(games.Sprite):
    """Player 2's turret"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Spheres\\"+"Sphere2.png")
    def __init__(self, x, y, game):
        """Creates class"""
        super(Sphere2, self).__init__(image=Sphere2.pic, x=x, y=y)
        self.game=game
        self.power=0
        self.anglelevel=games.Text(value=self.angle, size=20, color=color.red, top=30, right=games.screen.width-5)
        self.powerlevel=games.Text(value=self.power, size=20, color=color.red, top=5, right=games.screen.width-5)
        games.screen.add(self.anglelevel)
        games.screen.add(self.powerlevel)
    def update(self):
        """Checks for user input"""
        if games.keyboard.is_pressed(games.K_KP4):
            self.angle-=1
        if games.keyboard.is_pressed(games.K_KP6):
            self.angle+=1
        if games.keyboard.is_pressed(games.K_KP8):
            self.power+=1
        if games.keyboard.is_pressed(games.K_KP5):
            self.power-=1
        if self.game.turn==2 and games.keyboard.is_pressed(games.K_KP0):
            self.shoot()
        self.anglelevel.value=self.angle
        self.powerlevel.value=self.power
        self.anglelevel.right=games.screen.width-5
        self.powerlevel.right=games.screen.width-5
    def shoot(self):
        """Fires ball"""
        shot1=shot(Tx=self.x, Ty=self.y, TAngle=self.angle, Tpower=self.power)
        games.screen.add(shot1)
        self.game.changeplayer()
    def die(self):
        """Ends game"""
        Loser=games.Message(value="PLAYER ONE WON", size=100, color=color.blue, x=games.screen.width/2, y=games.screen.height/2, lifetime=3*games.screen.fps, after_death=self.game.newgame())
        games.screen.add(Loser)
SphereWars=game()
games.screen.mainloop()

##GALAXE
from livewires import color, games
import random
games.init(screen_width=1350, screen_height=725, fps=50)
background=games.load_image("background.png", transparent=False)
games.music.load("hyperspace.mp3")
games.music.play(-1)
class spaceship(games.Sprite):
    """Player's ship class"""
    pic=games.load_image("ship.png")
    def __init__(self):
        """creates and sets up the class"""
        super(spaceship, self).__init__(image=spaceship.pic, x=games.screen.width/2, bottom=games.screen.height-5)
        self.missle_delay=125
        self.paused=False
    def update(self):
        """Checks for input from the player"""
        if games.keyboard.is_pressed(games.K_LEFT) and self.paused==False:
            self.x-=3
        if games.keyboard.is_pressed(games.K_RIGHT) and self.paused==False:
            self.x+=3
        if games.keyboard.is_pressed(games.K_SPACE) and self.missle_delay<=0 and self.paused==False:
            self.shoot()
            self.missle_delay=50
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
        self.missle_delay-=1
        if games.keyboard.is_pressed(games.K_p):
            self.togglepause()
    def shoot(self):
        """Creates a class of shipgun to shoot aliens"""
        projectile=shipgun(self.x)
        games.screen.add(projectile)
    def die(self):
        """Raises GAMEOVER and destroys Sprite"""
        self.destroy()
        GameOver=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit)
        games.screen.add(GameOver)
    def togglepause(self):
        """Makes ship immobile"""
        if self.paused:
            self.paused=False
        elif not self.paused:
            self.paused=True          
class shipgun(games.Sprite):
    """Missile that goes straight up and destroys anything it hits"""
    pic=games.load_image("shipgun.png")
    def __init__(self, shipx):
        """Sets up all the variables and creates the missile"""
        x=shipx
        bottom=games.screen.height-55
        dy=-5
        super(shipgun, self).__init__(image=shipgun.pic, x=x, bottom=bottom, dy=dy)
        self.points=games.Text(value=0, size=50, color=color.white, top=5, right=games.screen.width-5)
        self.paused=False
    def update(self):
        """Checks wheteher or not it should be destroyed and kills any aliens in its way"""
        if self.top<0:
            self.destroy()
        for alien in self.overlapping_sprites:
            try:
                alien.oblitherate()
                self.points.value+=10
                self.points.right=games.screen.width-5
                self.destroy()
            except:
                self.destroy()
        if games.keyboard.is_pressed(games.K_p):
            self.togglepause()
        self.checkpause()
    def togglepause(self):
        """Turns pause on and off"""
        if self.paused:
            self.paused=False
        elif not self.paused:
            self.paused=True
    def checkpause(self):
        """Freezes missile if game is paused"""
        if self.paused:
            self.dy=0
        elif not self.paused:
            self.dy=-5
class alien(games.Sprite):
    """Enemy that shoots at player"""
    pic=games.load_image("alien.png")
    total = 0
    def __init__(self, x, y):
        """Sets up varibles and creates alien"""
        super(alien, self).__init__(image=alien.pic, left=x, top=y)
        self.guntime=random.randint(100, 200)
        alien.total+=1
        self.paused=False
    def update(self):
        """Fires at the right time and checks if it should be dead"""
        if self.guntime==0:
            self.shoot()
            self.guntime=random.randint(100, 200)
        self.guntime-=1
        self.checkdead()
        if games.keyboard.is_pressed(games.K_p):
            self.togglepause()
    def shoot(self):
        """Creates a class of aliengun"""
        M1=aliengun(self.x, self.bottom)
        games.screen.add(M1)
    def oblitherate(self):
        """kills the alien and removes it from the fleet"""
        alien.total=alien.total-1
        self.destroy()
    def die(self):
        """Absolutely nothing, programmed in to avoid glitching"""
        pass
    def checkdead(self):
        """checks if game is over"""
        if alien.total<=1:
            Winner=games.Message(value="YOU WON", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
            Mole=games.Message(value="(THIS ALIEN HAS SURRENDERED)", size=75, color=color.red, x=games.screen.width/2, top=400, lifetime=7*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
            games.screen.add(Winner)
            games.screen.add(Mole)
    def togglepause(self):
        """Turns pause on and off"""
        if self.paused:
            self.paused=False
        elif not self.paused:
            self.paused=True
        self.checkpause()
    def checkpause(self):
        """Stops shooting if paused"""
        if self.paused:
            self.temp=self.guntime
            self.guntime=-1
        elif not self.paused:
            self.guntime=self.temp
class aliengun(games.Sprite):
    """Missile that goes straight down"""
    pic=games.load_image("aliengun.png")
    def __init__(self, alienx, alieny):
        """Creates missile"""
        x=alienx
        top=alieny+1
        dy=3
        super(aliengun, self).__init__(image=aliengun.pic, x=x, top=top, dy=dy)
        self.paused=False
    def update(self):
        """Destroys anything in the way"""
        for ship in self.overlapping_sprites:
            try:
                ship.die()
                self.destroy()
            except:
                self.destroy()
        if self.bottom>games.screen.height:
            self.destroy()
        if games.keyboard.is_pressed(games.K_p):
            self.togglepause()
        self.checkpause()
    def die(self):
        """Nothing, put in to avoid glitching"""
        pass
    def oblitherate(self):
        """Removes object from the screen"""
        self.destroy()
    def togglepause(self):
        """Turns pause on and off"""
        if self.paused:
            self.paused=False
        elif not self.paused:
            self.paused=True
    def checkpause(self):
        """Freezes if paused"""
        if self.paused:
            self.dy=0
        elif not self.paused:
            self.dy=3
class fleet(games.Sprite):
    """fleet holding all the aliens"""
    pic=games.load_image("fleet.png")
    def __init__(self):
        """Creates all the aliens"""
        x=1
        y=1
        super(fleet, self).__init__(image=fleet.pic, x=x, y=y)
        self.movewait=0
        self.direction=1
        self.a1=alien(7, 7)
        self.a2=alien(47, 7)
        self.a3=alien(87, 7)
        self.a4=alien(127, 7)
        self.a5=alien(167, 7)
        self.a6=alien(207, 7)
        self.a7=alien(247, 7)
        self.a8=alien(287, 7)
        self.a9=alien(327, 7)
        self.a10=alien(367, 7)
        self.a11=alien(407, 7)
        self.a12=alien(447, 7)
        self.a13=alien(487, 7)
        self.a14=alien(527, 7)
        self.a15=alien(567, 7)
        self.b1=alien(7, 47)
        self.b2=alien(47, 47)
        self.b3=alien(87, 47)
        self.b4=alien(127, 47)
        self.b5=alien(167, 47)
        self.b6=alien(207, 47)
        self.b7=alien(247, 47)
        self.b8=alien(287, 47)
        self.b9=alien(327, 47)
        self.b10=alien(367, 47)
        self.b11=alien(407, 47)
        self.b12=alien(447, 47)
        self.b13=alien(487, 47)
        self.b14=alien(527, 47)
        self.b15=alien(567, 47)
        self.c1=alien(7, 87)
        self.c2=alien(47, 87)
        self.c3=alien(87, 87)
        self.c4=alien(127, 87)
        self.c5=alien(167, 87)
        self.c6=alien(207, 87)
        self.c7=alien(247, 87)
        self.c8=alien(287, 87)
        self.c9=alien(327, 87)
        self.c10=alien(367, 87)
        self.c11=alien(407, 87)
        self.c12=alien(447, 87)
        self.c13=alien(487, 87)
        self.c14=alien(527, 87)
        self.c15=alien(567, 87)
        self.d1=alien(7, 127)
        self.d2=alien(47, 127)
        self.d3=alien(87, 127)
        self.d4=alien(127, 127)
        self.d5=alien(167, 127)
        self.d6=alien(207, 127)
        self.d7=alien(247, 127)
        self.d8=alien(287, 127)
        self.d9=alien(327, 127)
        self.d10=alien(367, 127)
        self.d11=alien(407, 127)
        self.d12=alien(447, 127)
        self.d13=alien(487, 127)
        self.d14=alien(527, 127)
        self.d15=alien(567, 127)
        self.e1=alien(7, 167)
        self.e2=alien(47, 167)
        self.e3=alien(87, 167)
        self.e4=alien(127, 167)
        self.e5=alien(167, 167)
        self.e6=alien(207, 167)
        self.e7=alien(247, 167)
        self.e8=alien(287, 167)
        self.e9=alien(327, 167)
        self.e10=alien(367, 167)
        self.e11=alien(407, 167)
        self.e12=alien(447, 167)
        self.e13=alien(487, 167)
        self.e14=alien(527, 167)
        self.e15=alien(567, 167)
        self.f1=alien(7, 207)
        self.f2=alien(47, 207)
        self.f3=alien(87, 207)
        self.f4=alien(127, 207)
        self.f5=alien(167, 207)
        self.f6=alien(207, 207)
        self.f7=alien(247, 207)
        self.f8=alien(287, 207)
        self.f9=alien(327, 207)
        self.f10=alien(367, 207)
        self.f11=alien(407, 207)
        self.f12=alien(447, 207)
        self.f13=alien(487, 207)
        self.f14=alien(527, 207)
        self.f15=alien(567, 207)
        self.aliens=[self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10, self.a11, self.a12, self.a13, self.a14, self.a15, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b10, self.b11, self.b12, self.b13, self.b14, self.b15, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c10, self.c11, self.c12, self.c13, self.c14, self.c15, self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.d11, self.d12, self.d13, self.d14, self.d15, self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9, self.e10, self.e11, self.e12, self.e13, self.e14, self.e15, self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12, self.f13, self.f14, self.f15]
        for alIen in self.aliens:
            games.screen.add(alIen)
        self.paused=False
    def update(self):
        """Moves aliens and checks if game is over"""
        #for aliien in self.aliens:
            #aliien.oblitherate()
        self.move()
        self.checkdoom()
    def move(self):
        """Moves all the aliens"""
        self.movewait+=1
        for alienz in self.aliens:
            if alienz.left<0:
                for al in range(0, 15):
                    self.aliens[al].y+=2
                self.direction=1
                break
            if alienz.right>games.screen.width:
                for alie in self.aliens:
                    alie.y+=2
                self.direction=0
                break
        if self.movewait>=50 and self.direction==1:
            for AL in self.aliens:
                AL.x+=15
            self.movewait=0
        if self.movewait>=50 and self.direction==0:
            for aL in self.aliens:
                aL.x-=15
            self.movewait=0
        if games.keyboard.is_pressed(games.K_p):
            self.togglepause()
    def checkdoom(self):
        """Checks if all aliens have hit the bottom and ends the game if so"""
        for AlIeN in self.aliens:
            if AlIeN.bottom>=400:
                Gameover=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=7*games.screen.fps, after_death=games.screen.quit)
                games.screen.add(Gameover)
            break
    def togglepause(self):
        """Turns pause on and off"""
        if self.paused==True:
            self.paused=False
        elif self.paused==False:
            self.paused=True
        self.checkpause()
    def checkpause(self):
        """Stops moving if paused"""
        if self.paused:
            self.temp=self.direction
            self.direction=None
            games.music.stop()
        elif not self.paused:
            self.direction=self.temp
            games.music.play(-1)

ship=spaceship()
games.screen.add(ship)
Fleet=fleet()
games.screen.add(Fleet)
games.screen.mainloop()
        
        
        

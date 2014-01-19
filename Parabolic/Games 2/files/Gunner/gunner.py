from livewires import games, color
import math
import random
import os
games.init(screen_width=1000, screen_height=500, fps=100)
back=games.load_image(os.getcwd()+"\\files\\"+"\\Gunner\\"+"background.png")
games.screen.background=back
class gunner(games.Sprite):
    """Player controlled sprite"""
    man=games.load_image(os.getcwd()+"\\files\\"+"\\Gunner\\"+"gunman.png")

    def __init__(self):
        """Creates Gunner"""
        super(gunner, self).__init__(image=gunner.man, x=games.screen.width/2, y=games.screen.height/2)
        self.timer=50
    def update(self):
        """Checks for user input"""
        self.timer-=1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle-=1
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle+=1
        if games.keyboard.is_pressed(games.K_SPACE) and self.timer<=0:
            self.shoot()
            self.timer=50
    def die(self):
        """Ends the game"""
        GrimReaper=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=3*games.screen.fps, after_death=games.screen.quit, is_collideable=False)
        games.screen.add(GrimReaper)
        self.destroy()
    def shoot(self):
        """Fires a bullet"""
        b=bullet(self.x, self.y, self.angle)
        games.screen.add(b)
class bullet(games.Sprite):
    """Object that destroys things that it touches"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Gunner\\"+"bullet.png")
    def __init__(self, Gx, Gy, Gangle):
        """Creates bullet and does math to find dx and dy"""
        angle=Gangle*math.pi/180
        xbuffer=100*math.sin(angle)
        ybuffer=100*-math.cos(angle)
        x=Gx+xbuffer
        y=Gy+ybuffer
        dx=(5*math.sin(angle))/2
        dy=(5*-math.cos(angle))/2
        super(bullet, self).__init__(image=bullet.pic, x=x, y=y, dx=dx, dy=dy, angle=Gangle)
    def update(self):
        """Destroys overlapping sprites"""
        for bullet in self.overlapping_sprites:
            try:
                bullet.death()
            except:
                pass
class Asteroid(games.Sprite):
    """Asteroid that comes in from the edge of the screeen and destroys asteroids and gunner if they overlap"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Gunner\\"+"A.png")
    def death(self):
        """Destroys asteroid"""
        self.destroy()
        
        
    def __init__(self):
        """Creates asteroid with random coordinates"""
        t=random.choice([0, 1])
        if t==0:
            super(Asteroid, self).__init__(image=Asteroid.pic, x=random.randint(0, games.screen.width), y=random.choice([0, games.screen.height]), dx=random.randint(-3, 3), dy=random.randint(-3, 3))
        if t==1:
            super(Asteroid, self).__init__(image=Asteroid.pic, y=random.randint(0, games.screen.height), x=random.choice([0, games.screen.width]), dx=random.randint(-3, 3), dy=random.randint(-3, 3))
    def update(self):
        """destroys overlapping sprites, dies if off screen"""
        if self.bottom<0:
            self.top=games.screen.height
        if self.right<0:
            self.left=games.screen.width
        if self.left>games.screen.width:
            self.right=0
        if self.top>games.screen.height:
            self.bottom=0
        for asteroid in self.overlapping_sprites:
            try:
                asteroid.die()
            except:
                pass
    def die(self):
        """Destroys asteroid"""
        self.death()
class game(games.Sprite):
    """Controls game"""
    def __init__(self):
        """Creates class, sets up variables"""
        pic=games.load_image(os.getcwd()+"\\files\\"+"\\Gunner\\"+"A.png")
        self.timer=random.randint(100, 400)
        super(game, self).__init__(image=pic, x=-50, y=-50, is_collideable=False)
    def update(self):
        """Creates asteroids"""
        self.timer-=1
        if self.timer<0:
            a=Asteroid()
            games.screen.add(a)
            self.timer=random.randint(100, 400)
    
gunman=gunner()
games.screen.add(gunman)
g=game()
games.screen.add(g)
games.screen.mainloop()

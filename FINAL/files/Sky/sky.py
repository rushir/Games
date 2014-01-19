##Skies
from livewires import games, color
import random
import os
games.init(screen_width=500, screen_height=650, fps=50)
class player(games.Sprite):
    """Player controlled sprite"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"Craft.png")
    def __init__(self, x, y):
        """Creates sprite and 3 lives"""
        super(player, self).__init__(x=x, y=y, image=player.pic)
        self.guntime=25
        self.bombtime=50
        self.sights=crosshairs(self.x, self.y)
        games.screen.add(self.sights)
        self.l1=life(20, 20, self)
        self.l2=life(50, 20, self)
        self.l3=life(80, 20, self)
        games.screen.add(self.l1)
        games.screen.add(self.l2)
        games.screen.add(self.l3)
        self.lives=[self.l1, self.l2, self.l3]
    def update(self):
        """Checks for user input"""
        self.guntime-=1
        self.bombtime-=1
        if games.keyboard.is_pressed(games.K_SPACE) and self.guntime<=0:
            self.shoot()
            self.guntime=25
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x-=2
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x+=2
        if games.keyboard.is_pressed(games.K_UP):
            self.y-=2
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y+=2
        if games.keyboard.is_pressed(games.K_RALT) and self.bombtime<=0:
            self.bombs()
            self.bombtime=50
        if games.keyboard.is_pressed(games.K_LALT) and self.bombtime<=0:
            self.bombs()
            self.bombtime=50
        if self.bottom>games.screen.height:
            self.bottom=games.screen.height
        if self.top<0:
            self.top=0
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
        self.sights.x=self.x
        self.sights.y=self.y-230
    def shoot(self):
        """Fires a shot"""
        s=shot(self.x, self.y)
        games.screen.add(s)
    def doom(self):
        """Loses a life"""
        if self.l3 in self.lives:
            self.l3.lose()
            onedown=games.Message(value="LOST A LIFE", size=50, color=color.white, x=games.screen.width/2, y=games.screen.height/2, is_collideable=False, lifetime=3*games.screen.fps, after_death=None)
            games.screen.add(onedown)
        elif self.l2 in self.lives:
            self.l2.lose()
            onedown=games.Message(value="LOST A LIFE", size=50, color=color.white, x=games.screen.width/2, y=games.screen.height/2, is_collideable=False, lifetime=3*games.screen.fps, after_death=None)
            games.screen.add(onedown)
        elif self.l1 in self.lives:
            self.l1.lose()
            onedown=games.Message(value="LOST A LIFE", size=50, color=color.white, x=games.screen.width/2, y=games.screen.height/2, is_collideable=False, lifetime=3*games.screen.fps, after_death=None)
            games.screen.add(onedown)
        else:
            dead=games.Message(value="GAME OVER", size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, is_collideable=False, lifetime=7*games.screen.fps, after_death=games.screen.quit)
            games.screen.add(dead)
            self.destroy()
    def die(self):
        """Does nothing, player shouldn't be hit with his/her own shots"""
        pass
    def bombs(self):
        """Fires a bomb"""
        b=bomb(self.x, self.y)
        games.screen.add(b)
    def explode(self):
        """Does nothing, player shouldn't be hit with his/her own bombs"""
        pass
class crosshairs(games.Sprite):
    """Crosshairs that chow where a bomb will hit"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"cross.png")
    def __init__(self, x, cy):
        """Creates class"""
        y=cy-230
        super(crosshairs, self).__init__(image=crosshairs.pic, x=x, y=y, is_collideable=False)
    def update(self):
        """Makes sprite visible"""
        self.elevate()
class life(games.Sprite):
    """Extra life"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"life.png")
    def __init__(self, x, y, craft):
        """Creates sprite"""
        super(life, self).__init__(image=life.pic, x=x, y=y, is_collideable=False)
        self.craft=craft
    def update(self):
        """Makes lifevisible"""
        self.elevate(self.craft)
    def lose(self):
        """Lose a life"""
        self.craft.lives.remove(self)
        self.destroy()
class shot(games.Sprite):
    """Player's shot that destroys enemies"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"bomb.png")
    def __init__(self, x, y):
        """Creates Sprite"""
        super(shot, self).__init__(x=x, y=y-30, image=shot.pic, dy=-4)
    def update(self):
        """destroys overlapping sprites"""
        for enemy in self.overlapping_sprites:
            enemy.die()
        if self.bottom<0:
            self.destroy()
    def explode(self):
        """Nothing, player's shots and bombs shouldn't collide"""
        pass
    def doom(self):
        """Destroys shot"""
        self.destroy()
class fire(games.Sprite):
    """Fire shown and end of game"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"flame.png", transparent=False)
    def __init__(self):
        """Creates Sprite"""
        super(fire, self).__init__(image=fire.pic, x=games.screen.width/2, top=50, is_collideable=False)
class backdrop(games.Sprite):
    """Scrolling backdrop"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"backdrop.png", transparent=False)
    def __init__(self):
        """Creates sprite"""
        super(backdrop, self).__init__(image=backdrop.pic, bottom=games.screen.height, left=0, dy=0.5, is_collideable=False)
    def update(self):
        """Stops and says the game is won if level is completed"""
        if self.top==0:
            self.dy=0
            flames=fire()
            games.screen.add(flames)
            WINNING=games.Message(value="YOU WON", size=100, color=color.blue, x=games.screen.width/2, y=games.screen.height/2, is_collideable=False, lifetime=7*games.screen.fps, after_death=games.screen.quit)
            games.screen.add(WINNING)
class bomb(games.Sprite):
    """Bomb that destroys turrets"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"shot.png")
    def __init__(self, x, y):
        """Creates sprite"""
        super(bomb, self).__init__(image=bomb.pic, x=x, y=y-30, dy=-4)
        self.life=50
    def update(self):
        """Explodes after a period of time"""
        self.life-=1
        if self.life<=0:
            self.boom()
    def die(self):
        """Nothing, shouldn't overlap with shots"""
        pass
    def doom(self):
        """Nothing, shouldn't overlap with shots"""
        pass
    def boom(self):
        """Destroys overlapping turrets"""
        for turret in self.overlapping_sprites:
            turret.explode()
        self.destroy()
class eshot(games.Sprite):
    """enemy shot"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"eshot.png")
    def __init__(self, x, y):
        """Creates sprite"""
        super(eshot, self).__init__(x=x, y=y+30, image=eshot.pic, dy=4)
    def update(self):
        """Destroys overlapping sprites"""
        for enemy in self.overlapping_sprites:
            enemy.doom()
            self.destroy()
        if self.bottom>games.screen.height:
            self.destroy()
    def explode(self):
        """Nothing, shots and bombs shouldn't overlap"""
        pass
    def die(self):
        """destroys shot"""
        self.destroy()
    def doom(self):
        """Nothing, enemy shots shouldn't collide"""
        pass
class enemy(games.Sprite):
    """Enemy sprite"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"enemy.png")
    def __init__(self):
        """Creates sprite at random coordinates"""
        s=random.choice([0, 1])
        if s==0:
            super(enemy, self).__init__(image=enemy.pic, x=0, y=random.randint(0, games.screen.height/2), dx=random.randint(1, 5), dy=random.randint(-3, 3))
        if s==1:
            super(enemy, self).__init__(image=enemy.pic, x=games.screen.width, y=random.randint(0, games.screen.height/2), dx=random.randint(-5, -1), dy=random.randint(-3, 3))
        self.time=50
    def update(self):
        """Fires at set intervals and dies if offscreen"""
        self.time-=1
        if self.time<0:
            self.shoot()
            self.time=50
        if self.left>games.screen.width or self.right<0 or self.top>games.screen.width or self.bottom<0:
            self.destroy()
    def shoot(self):
        """Fires a shot"""
        s=eshot(self.x, self.y)
        games.screen.add(s)
    def die(self):
        """destroys sprite"""
        self.destroy()
    def doom(self):
        """Nothing, enemies shouldn't be hit with their own shots"""
        pass
    def explode(self):
        """Nothing, shots and bombs shouldn't overlap"""
        pass
class game(games.Sprite):
    """Controlling class"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"bomb.png")
    def __init__(self):
        """Creates class"""
        super(game, self).__init__(image=game.pic, x=-10, y=-10, is_collideable=False)
        self.timer=random.randint(25, 150)
    def update(self):
        """Creates turret or enemy at random times"""
        self.timer-=1
        if self.timer<0:
            c=random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
            self.timer=random.randint(25, 150)
            if c==0:
                e=enemy()
                games.screen.add(e)
            elif c==1:
                t=turret()
                games.screen.add(t)
class turret(games.Sprite):
    """Ground turret"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"turret.png")
    def __init__(self):
        """Creates sprite"""
        super(turret, self).__init__(image=turret.pic, x=random.randint(0, games.screen.width), y=random.randint(0, 375))
        self.shottime=100
    def update(self):
        """Shoots at intervals"""
        self.shottime-=1
        if self.shottime<0:
            self.shoot()
            self.shottime=100
        if self.right>games.screen.width:
            self.right=games.screen.width
        if self.left<0:
            self.left=0
    def shoot(self):
        """Fires a shot"""
        s=tshot(self.x, self.y)
        games.screen.add(s)
    def die(self):
        """Nothing, turrets shouldn't be killed by aerial shots"""
        pass
    def doom(self):
        """Nothing, turrets shouldn't be killed by aerial shots"""
        pass
    def explode(self):
        """Destroys turret"""
        self.destroy()
class tshot(games.Sprite):
    """Turret shot"""
    pic=games.load_image(os.getcwd()+"\\files\\"+"\\Sky\\"+"tshot.png")
    def __init__(self, x, y):
        """Creates sprite"""
        super(tshot, self).__init__(x=x, y=y+30, image=tshot.pic, dy=4)
    def update(self):
        """Destroys player if overlapping"""
        for enemy in self.overlapping_sprites:
            enemy.doom()
            self.destroy()
        if self.bottom>games.screen.height:
            self.destroy()
    def explode(self):
        """Nothing, shots and bombs shouldn't overlap"""
        pass
    def die(self):
        """Destroys overlapping shots"""
        for enemy in self.overlapping_sprites:
            enemy.doom()
    def doom(self):
        """Nothing, enemy shots shouldn't kill turret shots"""
        pass
back=backdrop()
p=player(250, 250)
control=game()
games.screen.add(control)
games.screen.add(back)
games.screen.add(p)
games.screen.mainloop()

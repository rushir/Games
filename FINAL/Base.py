##BaseMenu
from livewires import games
import os
games.init(screen_width=1000, screen_height=500, fps=50)
back=games.load_image(os.getcwd()+"\\files\\Menu\\"+"Background.png")
games.screen.background=back
class select(games.Sprite):
    """Shows what is selected"""
    pic=games.load_image(os.getcwd()+"\\files\\Menu\\"+"select.png")
    def __init__(self, x, y):
        """creates select"""
        super(select, self).__init__(image=select.pic, x=x, y=y)
class menu(games.Sprite):
    """Interactive menu"""
    pic=games.load_image(os.getcwd()+"\\files\\Menu\\"+"blank.png")
    def __init__(self):
        """Creates menu and variables"""
        super(menu, self).__init__(image=menu.pic, x=1, y=1)
        self.galaxe=True
        self.flite=False
        self.tanks=False
        self.pong=False
        self.sphere=False
        self.brix=False
        self.gunner=False
        self.sky=False
        self.box=select(games.screen.width/2, 25)
        games.screen.add(self.box)
        self.count=0
        self.path=os.getcwd()+"\\files\\"
    def update(self):
        """Checks for user input"""
        self.count+=1
        if games.keyboard.is_pressed(games.K_DOWN) and self.count>=12.5:
            if self.galaxe:
                self.galaxe=False
                self.flite=True
            elif self.flite:
                self.flite=False
                self.tanks=True
            elif self.tanks:
                self.tanks=False
                self.pong=True
            elif self.pong:
                self.pong=False
                self.sphere=True
            elif self.sphere:
                self.sphere=False
                self.brix=True
            elif self.brix:
                self.brix=False
                self.gunner=True
            elif self.gunner:
                self.gunner=False
                self.sky=True
            elif self.sky:
                self.sky=False
                self.galaxe=True
            self.rotate()
            self.count=0
        if games.keyboard.is_pressed(games.K_UP) and self.count>=12.5:
            if self.galaxe:
                self.galaxe=False
                self.sky=True
            elif self.flite:
                self.flite=False
                self.galaxe=True
            elif self.tanks:
                self.tanks=False
                self.flite=True
            elif self.pong:
                self.pong=False
                self.tanks=True
            elif self.sphere:
                self.sphere=False
                self.pong=True
            elif self.brix:
                self.brix=False
                self.sphere=True
            elif self.gunner:
                self.gunner=False
                self.brix=True
            elif self.sky:
                self.sky=False
                self.gunner=True
            self.rotate()
            self.count=0
        if games.keyboard.is_pressed(games.K_RETURN) and self.count>=12.5:
            if self.galaxe:
                os.startfile(self.path+"\\Galaxe\\"+"GALAXEVertical.py")
            elif self.tanks:
                os.startfile(self.path+"\\Tanks\\"+"MaybeFinalTanks.py")
            elif self.flite:
                os.startfile(self.path+"\\FlitePath\\"+"Powerups.py")
            elif self.pong:
                os.startfile(self.path+"\\Pong\\"+"pongSIZED.py")
            elif self.sphere:
                os.startfile(self.path+"\\Spheres\\"+"SphereWars.py")
            elif self.brix:
                os.startfile(self.path+"\\Brixx\\"+"Brixx.py")
            elif self.gunner:
                os.startfile(self.path+"\\Gunner\\"+"gunner.py")
            elif self.sky:
                os.startfile(self.path+"\\Sky\\"+"sky.py")
            self.count=0
    def rotate(self):
        """Cycles through selections"""
        if self.galaxe:
            self.box.y=25
        elif self.flite:
            self.box.y=77
        elif self.tanks:
            self.box.y=150
        elif self.pong:
            self.box.y=212.5
        elif self.sphere:
            self.box.y=275
        elif self.brix:
            self.box.y=348
        elif self.gunner:
            self.box.y=410
        elif self.sky:
            self.box.y=475
        
base=menu()
games.screen.add(base)
games.screen.mainloop()

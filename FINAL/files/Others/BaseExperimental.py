##BaseMenu
from livewires import games
import os
games.init(screen_width=1000, screen_height=500, fps=50)
back=games.load_image("BaseGround.png")
games.screen.background=back
class select(games.Sprite):
    """Shows what is selected"""
    pic=games.load_image("select.png")
    def __init__(self, x, y):
        """creates select"""
        super(select, self).__init__(image=select.pic, x=x, y=y)
class menu(games.Sprite):
    """Interactive menu"""
    pic=games.load_image("blank.png")
    def __init__(self):
        """Creates menu and variables"""
        super(menu, self).__init__(image=menu.pic, x=1, y=1)
        self.galaxe=True
        self.tanks=False
        self.flite=False
        self.pong=False
        self.box=select(games.screen.width/2, 48)
        games.screen.add(self.box)
        self.count=0
        self.path=os.getcwd()+"\\files\\"
    def update(self):
        """Checks for user input"""
        self.count+=1
        if games.keyboard.is_pressed(games.K_DOWN) and self.count>=12.5:
            if self.galaxe:
                self.galaxe=False
                self.tanks=True
            elif self.tanks:
                self.tanks=False
                self.flite=True
            elif self.flite:
                self.flite=False
                self.pong=True
            elif self.pong:
                self.pong=False
                self.galaxe=True
            self.rotate()
            self.count=0
        if games.keyboard.is_pressed(games.K_UP) and self.count>=12.5:
            if self.galaxe:
                self.galaxe=False
                self.pong=True
            elif self.tanks:
                self.tanks=False
                self.galaxe=True
            elif self.flite:
                self.flite=False
                self.tanks=True
            elif self.pong:
                self.pong=False
                self.flite=True
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
            self.count=0
    def rotate(self):
        """Cycles through selections"""
        if self.galaxe:
            self.box.y=48
        elif self.tanks:
            self.box.y=157
        elif self.flite:
            self.box.y=268
        elif self.pong:
            self.box.y=400
base=menu()
games.screen.add(base)
games.screen.mainloop()

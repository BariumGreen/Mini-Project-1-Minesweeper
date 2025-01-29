import pygame, Game, Settings

class Start:
    def __init__(self):
        self.Image=pygame.transform.scale(pygame.image.load("Images\StartGame.png"), (430, 200))
        
    def __repr__(self):
        return True
    
    def tiler(self, destination):
        destination.blit(self.Image, (50, 220))
        
class Sett:
    def __init__(self):
        self.Image=pygame.transform.scale(pygame.image.load("Images\SettingsBox.png"), (430, 200))
            
    def __repr__(self):
        return True
        
    def tiler(self, destination):
        destination.blit(self.Image, (50, 495))
        
class Page:
    def __init__(self):
        self.screen=pygame.display.set_mode(size=(530, 770))
        pygame.display.set_caption("Minesweeper")
        self.Icon=pygame.image.load("Images\Icon.png")
        pygame.display.set_icon(self.Icon)
        self.Clock=pygame.time.Clock()
        self.screen.fill((0xba, 0xca, 0xba))    #BGColour
        self.going=True
        self.Choice=None
        
    def Start(self):
        self.Head=pygame.transform.scale(pygame.image.load("Images\Title.png"), (480, 150))
        self.screen.blit(self.Head, (25, 10))
        self.start=Start()
        self.settings=Sett()
        self.start.tiler(self.screen)
        self.settings.tiler(self.screen)
        pygame.display.flip()
        
    def Work(self):
        while self.going:
            self.Clock.tick(40)
            self.Choice=self.Events()
        pygame.quit()
        return self.Choice
            
    def Events(self):
        for click in pygame.event.get():
            if click.type==pygame.QUIT:
                pygame.quit()
                
            if click.type==pygame.MOUSEBUTTONDOWN:
                cx, cy=pygame.mouse.get_pos()
                
                if click.button==1:
                    if cx in range(50, 481) and cy in range(200, 421):
                        self.going=False
                        return 0
                        
                    elif cx in range(50, 481) and cy in range(200, 696):
                        self.going=False
                        return 1

while True:
    game=Page()
    game.Start()
    Do=game.Work()
    if Do==0:
        Game.GameStart()
    elif Do==1:
        Settings.SetStart()
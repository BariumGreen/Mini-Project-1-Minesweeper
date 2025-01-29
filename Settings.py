import os, pickle, pygame

exist=os.path.exists("Settings.dat")
if not exist:
    File=open("Settings.dat", 'wb')
    pickle.dump([0, 0, 0], File)
    File.close()

SetRead=open("Settings.dat", 'rb')
scheme, mode, Size=pickle.load(SetRead)
SetRead.close()

class Difficulty:
    def __init__(self):
        SetRead=open("Settings.dat", 'rb')
        scheme, mode, sz=pickle.load(SetRead)
        SetRead.close()
        
        self.val=sz
        print(self.val)
        self.Diff=[]
        for i in range(3):
            self.Diff.append(pygame.transform.scale(pygame.image.load(f"Images\Diff{i}.png"), (200, 200)))
            pass
        
    def __repr__(self):
        return self.val
    
    def tiler(self, destination):
        if self.val>=3:
            self.val%=3
        destination.blit(self.Diff[self.val], (50, 260))
        
class Scheme:
    def __init__(self):
        SetRead=open("Settings.dat", 'rb')
        sc, mode, Size=pickle.load(SetRead)
        SetRead.close()
        
        self.val=sc
        print(self.val)
        self.Schm=[]
        for i in range(3):
            self.Schm.append(pygame.transform.scale(pygame.image.load(f"Images\Schm{i}.png"), (200, 200)))
            pass
        self.Schm.append(pygame.transform.scale(pygame.image.load("Images\Settings.png"), (200, 200)))
        
    def __repr__(self):
        return self.val
    
    def tiler(self, destination):
        if self.val>=3:
            self.val%=3
        destination.blit(self.Schm[self.val], (280, 260))
        
class Mode:
    def __init__(self):
        SetRead=open("Settings.dat", 'rb')
        scheme, md, Size=pickle.load(SetRead)
        SetRead.close()
        
        self.val=md
        print(self.val)
        self.Mode=[]
        for i in range(2):
            self.Mode.append(pygame.transform.scale(pygame.image.load(f"Images\Mode{i}.png"), (430, 100)))
            pass
        
    def __repr__(self):
        return self.val
    
    def tiler(self, destination):
        if self.val>=2:
            self.val%=2
        destination.blit(self.Mode[self.val], (50, 490))
        
class Save:
    def __init__(self):
        self.exit=pygame.transform.scale(pygame.image.load("Images\SaveSettings.png"), (430, 100))
        
    def __repr__(self):
        return True
    
    def tiler(self, destination):
        destination.blit(self.exit, (50, 620))

class Page:
    def __init__(self):
        global scheme, mode, Size
        
        SetRead=open("Settings.dat", 'rb')
        scheme, mode, Size=pickle.load(SetRead)
        SetRead.close()
        
        self.screen=pygame.display.set_mode(size=(530, 770))
        pygame.display.set_caption("Minesweeper: Settings")
        self.Icon=pygame.image.load("Images/Settings.png")
        pygame.display.set_icon(self.Icon)
        self.Clock=pygame.time.Clock()
        self.changing=True
        self.screen.fill((0xaa, 0xda, 0xaa))    #BGColour
        
    def Start(self):
        self.Head=pygame.transform.scale(pygame.image.load("Images\SettingsBox.png"), (430, 200))
        self.screen.blit(self.Head, (50, 10))
        self.Diff=Difficulty()
        self.Schm=Scheme()
        self.Mode=Mode()
        self.exit=Save()
        
    def Work(self):
        while self.changing:
            self.Clock.tick(40)
            self.Update()
            self.Events()
        File=open("Settings.dat", 'wb')
        pickle.dump([self.Schm.val, self.Mode.val, self.Diff.val], File)
        File.close()
        pygame.quit()
        
    def Update(self):
        self.Diff.tiler(self.screen)
        self.Schm.tiler(self.screen)
        self.Mode.tiler(self.screen)
        self.exit.tiler(self.screen)
        pygame.display.flip()
        
    def Events(self):
        for click in pygame.event.get():
            if click.type==pygame.QUIT:
                pygame.quit()
                
            if click.type==pygame.MOUSEBUTTONDOWN:
                cx, cy=pygame.mouse.get_pos()
                
                if click.button==1:
                    if cx in range(50, 251) and cy in range(260, 461):
                        self.Diff.val+=1
                    elif cx in range(280, 481) and cy in range(260, 461):
                        self.Schm.val+=1
                    elif cx in range(50, 481) and cy in range(490, 591):
                        self.Mode.val+=1
                    elif cx in range(50, 481) and cy in range(620, 721):
                        File=open("Settings.dat", 'wb')
                        pickle.dump([self.Schm.val, self.Mode.val, self.Diff.val], File)
                        File.close()
                        self.changing=False
    
def SetStart():
    Set=Page()
    Set.Start()
    Set.Work()
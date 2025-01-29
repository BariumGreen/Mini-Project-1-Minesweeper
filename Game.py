import pygame
import random, time, pickle

class ModeButton:
    def __init__(self, mode=True):
        self.mode=mode
        
    def __repr__(self):
        return self.mode
    
    def tiler(self, destination):
        if self.mode:
            destination.blit(DigMode, (ROWS*30-170, 4))
        else:
            destination.blit(FlagMode, (ROWS*30-170, 4))
    
    def rev(self):
        self.mode=not self.mode

class Tile:
    def __init__(self, x, y):
        self.x, self.y = x*30, y*30
        self.val, self.image='u', Undug
        self.dug, self.flag=False, False
        
    def __repr__(self):
        return self.val
    
    def tiler(self, destination):
        if self.dug:
            destination.blit(self.image, (self.x+4, self.y+75-4))
        elif not self.dug and self.flag:
            destination.blit(FTile, (self.x+4, self.y+75-4))
        elif not self.dug and not self.flag:
            destination.blit(Undug, (self.x+4, self.y+75-4))

class Board:
    def __init__(self):
        self.Started=False
        self.playBoard=pygame.Surface((ROWS*30+8, COLS*30+79))
        self.tiles=[Tile(r, c) for r in range(ROWS) for c in range(COLS)]
        self.mode=ModeButton()
        self.mineDrop()
        self.numDrop()
        
    def tiler(self, destination):
        for i in self.tiles:
            i.tiler(self.playBoard)
        self.mode.tiler(self.playBoard)
        destination.blit(self.playBoard, (xOff-4, yOff-2))
    
    def mineDrop(self):
        self.Stiles=self.tiles.copy()
        self.Mtiles=[]
        for i in range(mno):
            m=random.choice(self.Stiles)
            self.Stiles.remove(m)
            mx, my=m.x//30, m.y//30
            self.tiles[mx*COLS+my].image=MTile
            self.tiles[mx*COLS+my].val='m'
            
    def mineCountN(self, x, y):
        count=0
        for xChk in range(-1, 2):
            for yChk in range(-1, 2):
                if (xChk, yChk)==(0, 0):
                    continue
                mx, my=x+xChk, y+yChk
                Bool=(0<=mx<ROWS) and (0<=my<COLS)
                if Bool and self.tiles[mx*COLS+my].val=='m':
                    count+=1
        return count
    
    def mineCountB(self, x, y):
        count=0
        for xChk in range(-1, 2):
            for yChk in range(-1, 2):
                if (xChk, yChk)==(0, 0):
                    continue
                mx, my=(x+xChk)%ROWS, (y+yChk)%COLS
                if self.tiles[mx*COLS+my].val=='m':
                    count+=1
        return count
    
    def numDrop(self):
        if mode==0:
            for i in self.Stiles:
                mx, my=i.x//30, i.y//30
                count=self.mineCountN(mx, my)
                self.tiles[mx*COLS+my].image=STiles[count]
                if count>0:
                    self.tiles[mx*COLS+my].val='n'
                else:
                    self.tiles[mx*COLS+my].val='b'
                    
        elif mode==1:
            for i in self.Stiles:
                mx, my=i.x//30, i.y//30
                count=self.mineCountB(mx, my)
                self.tiles[mx*COLS+my].image=STiles[count]
                if count>0:
                    self.tiles[mx*COLS+my].val='n'
                else:
                    self.tiles[mx*COLS+my].val='b'
                
    def Reassign(self, x, y):
        if mode==0:
            count=self.mineCountN(x, y)
            self.tiles[x*COLS+y].image=STiles[count]
            if count>0:
                self.tiles[x*COLS+y].val='n'
            else:
                self.tiles[x*COLS+y].val='b'
            for i in range(-1, 2):
                if x+i<0 or x+i>=ROWS:
                    continue
                for j in range(-1, 2):
                    if y+j<0 or y+j>=COLS or (x, y)==(0, 0):
                        continue
                    if self.tiles[(x+i)*COLS+y+j].val=='m':
                        continue
                    count=self.mineCountN(x+i, y+j)
                    self.tiles[(x+i)*COLS+y+j].image=STiles[count]
                    if count>0:
                        self.tiles[(x+i)*COLS+y+j].val='n'
                    else:
                        self.tiles[(x+i)*COLS+y+j].val='b'
                        
        elif mode==1:
            count=self.mineCountB(x, y)
            self.tiles[x*COLS+y].image=STiles[count]
            if count>0:
                self.tiles[x*COLS+y].val='n'
            else:
                self.tiles[x*COLS+y].val='b'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x, y)==(0, 0):
                        continue
                    if self.tiles[((x+i)%ROWS)*COLS+((y+j)%COLS)].val=='m':
                        continue
                    count=self.mineCountB((x+i)%ROWS, (y+j)%COLS)
                    self.tiles[((x+i)%ROWS)*COLS+((y+j)%ROWS)].image=STiles[count]
                    if count>0:
                        self.tiles[(x+i)*COLS+y+j].val='n'
                    else:
                        self.tiles[(x+i)*COLS+y+j].val='b'
                
    def dig(self, x, y):
        if not self.tiles[x*COLS+y].dug:
            self.tiles[x*COLS+y].dug=True
            
            if not self.Started and self.tiles[x*COLS+y].val=='m':
                self.Reassign(x, y)
            
            if self.tiles[x*COLS+y].val=='b' or not self.Started:
                self.Started=True
                for i in range(max(0, x-1), min(ROWS, x+2)):
                    for j in range(max(0, y-1), min(COLS, y+2)):
                        if self.tiles[i*COLS+j].val!='m':
                            self.dig(i, j)
                return True
            
            elif self.tiles[x*COLS+y].val=='m':
                return False
                
            elif self.tiles[x*COLS+y].val=='n':
                return True
            
        else:
            return True
        
class Page:
    def __init__(self):
        global SchemeList, schemeN, mode, size, scheme, ROWS, COLS, mno, xOff, yOff
        global MTile, FTile, STiles, Undug, DigMode, FlagMode, WinScr, LoseScr
        
        schemeList=('CL', 'GL', 'TC')

        SetRead=open("Settings.dat", 'rb')
        schemeN, mode, size=pickle.load(SetRead)
        SetRead.close()
        scheme=schemeList[schemeN]

        if size==0:
            ROWS, COLS=6, 8
            mno=8
        elif size==1:
            ROWS, COLS=10, 15
            mno=25
        elif size==2:
            ROWS, COLS=15, 20
            mno=50
        xOff, yOff=(530-ROWS*30)/2, (770-COLS*30)/2

        STiles=[]
        for i in range(9):
            STiles.append(pygame.transform.scale(pygame.image.load(f"Images\{scheme}_N{i}.png"), (30, 30)))
        MTile=pygame.transform.scale(pygame.image.load(f"Images\{scheme}_MINE.png"), (30,30))
        FTile=pygame.transform.scale(pygame.image.load(f"Images\{scheme}_FLAG.png"), (30,30))
        Undug=pygame.transform.scale(pygame.image.load(f"Images\{scheme}_RAW.png"), (30,30))
        DigMode=pygame.transform.scale(pygame.image.load("Images\DigMode.png"), (170,60))
        FlagMode=pygame.transform.scale(pygame.image.load("Images\FlagMode.png"), (170,60))
        WinScr=pygame.transform.scale(pygame.image.load("Images\WinScreen.png"), (430,330))
        LoseScr=pygame.transform.scale(pygame.image.load("Images\LoseScreen.png"), (430,330))
        
        self.screen=pygame.display.set_mode(size=(530, 770))
        pygame.display.set_caption("Minesweeper")
        self.Icon=pygame.image.load("Images/Icon.png")
        pygame.display.set_icon(self.Icon)
        self.Clock=pygame.time.Clock()
        self.screen.fill((0xaa, 0xdd, 0xaa))    #BGColour
        self.Won=False
    
    def Start(self):
        self.playGrid=Board()
    
    def Play(self):
        self.notDead=True
        while self.notDead:
            self.Clock.tick(40)     #FPS
            self.Update()
            self.Event()
        self.end()
        
    def Update(self):
        self.playGrid.tiler(self.screen)
        pygame.display.flip()
        
    def Event(self):
        for click in pygame.event.get():
            if click.type==pygame.QUIT:
                pygame.quit()
                
            if click.type==pygame.MOUSEBUTTONDOWN:
                cx, cy=pygame.mouse.get_pos()
                cx=int((cx-(xOff))/30)
                cy=int((cy-(yOff+75))/30)
                
                if cx not in range(ROWS) or cy not in range(int((-yOff)/60), COLS):
                    continue
                
                if click.button==1:
                    if -yOff/60<cy<0:
                        if self.playGrid.Started:
                            self.playGrid.mode.mode=not self.playGrid.mode.mode
                        
                    elif not self.playGrid.mode.mode and not self.playGrid.tiles[cx*COLS+cy].dug:
                        self.playGrid.tiles[cx*COLS+cy].flag=not self.playGrid.tiles[cx*COLS+cy].flag
                        
                    elif self.playGrid.mode.mode and not self.playGrid.tiles[cx*COLS+cy].flag:
                        if not self.playGrid.dig(cx, cy):
                            for i in self.playGrid.tiles:
                                i.dug=True
                            self.notDead=False
                            
            if self.Win():
                self.Won=True
                self.notDead=False
                            
    def Win(self):
        for i in self.playGrid.tiles:
            if i.val=='m':
                if i.dug:
                    return False
                continue
            if not i.dug:
                return False
        return True
    
    def end(self):
        self.Update()
        if self.Won:
            time.sleep(1)
            EndScr=WinScr
            self.screen.blit(EndScr, (50, 230))
            pygame.display.flip()
        else:
            EndScr=LoseScr
            self.screen.blit(EndScr, (50, 230))
            time.sleep(2)
            pygame.display.flip()
        self.Event()
        while True:
            for click in pygame.event.get():
                if click.type==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    return
    
def GameStart():
    Obj=Page()
    Obj.Start()
    Obj.Play()
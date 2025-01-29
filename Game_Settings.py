import pygame, pickle

schemeList=('CL', 'GL')

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
import pygame as pg
import serial
import sys
import time
from serial import SerialException

dataList=[1,2,3,4,5,6,7,8,9]
#Inicjalizuje klase kolek
class Tic(pg.sprite.Sprite):
    def __init__(self,AreaX,AreaY):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load('circle.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = AreaX
        self.rect.centery = AreaY    
    def kill(self):
        if finish is True:
            self.kill()
#Inicjalizuje klase krzyzykow
class Tac(pg.sprite.Sprite):
    def __init__(self,AreaX,AreaY):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('cross.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = AreaX
        self.rect.centery = AreaY 
class StartMenu(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('NewGame.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 225
        self.rect.centery = 230  
        
#K1=[70,80],K2=[70,230],K3=[70,370],K4=[220,80],K5=[220,230],K6=[220,380],K7=[370,80],K8=[370,230],K9=[370,380]

#Inicjalzuje kolka
#
#Inicjalizuje krzyzyki
#TacSprite = pg.sprite.RenderClear()#kontener na krzyzyki


clock = pg.time.Clock()
start=True
run=False
finish=False

newgame=pg.sprite.RenderClear()
Start=StartMenu()
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
except SerialException:
    sys.exit()

    

running=True

while running is True:
    width = 447
    height = 460
    size = (width,height)
    window=pg.display.set_mode(size)
    pg.display.set_caption('TicTacToe ')
    pg.display.flip()
    tic=pg.image.load('circle.png')
    tac = pg.image.load('cross.png')
    ch1=0
    ch2=0
    ch3=0
    ch4=0
    ch5=0
    ch6=0
    ch7=0
    ch8=0
    ch9=0
    #Licznik sprawdza, ktory gracz wykonuje ruch
    counter=0    
    background = pg.image.load('tic-tac-toe-board.png')
    screen = pg.display.get_surface()
    screen.blit(background,(0,0))
    TicDic = {}
    TacDic={}
    dimsx = [70,220,370]
    dimsy = [80,230,380]
    #K1=[70,80],K2=[70,230],K3=[70,370],K4=[220,80],K5=[220,230],K6=[220,380],K7=[370,80],K8=[370,230],K9=[370,380]
    for i in range(3):
        for j in range(3):
            a=3*i+j+1
            TicDic[a]=Tic(dimsx[i],dimsy[j])
    for i in range(3):
        for j in range(3):
            a=3*i+j+1
            TacDic[a]=Tac(dimsx[i],dimsy[j])
    #Inicjalzuje kolka
    TicSprite = pg.sprite.RenderClear()#kontener na kolka
    
    #Inicjalizuje krzyzyki
    TacSprite = pg.sprite.RenderClear()#kontener na krzyzyki
    
    pg.display.flip()
    clock = pg.time.Clock()
    start=True
    run=False
    finish=False
    
    newgame=pg.sprite.RenderClear()
    Start=StartMenu()
    clock.tick(15)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()  
            
    
    while start is True:
        counter=0
        try:
            data2=arduino.readline()[:2]
        except SerialException:
            sys.exit()
        
        
        data2=str(data2, 'utf-8') 
        if data2:
            data2=eval(data2)          
        
        newgame.add(Start)   
        newgame.update()
        newgame.clear(window, background)
        newgame.draw(window) 
        #newgame = pg.image.load('NewGame.png')
        #screen = pg.display.get_surface()
        #screen.blit(newgame,(0,0))
        pg.display.flip()
    
                    
        if data2==5:
            run = True
            start=False
            data=0
            screen.blit(background,(0,0))         
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()  
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_5:
                    run = True
                    start=False
                    screen.blit(background,(0,0))            
                elif event.key == pg.K_5:
                        if ch5==0:
                            if counter%2==0: 
                                counter+=1
                                TicSprite.add(TicDic[5])
                                ch5=1
                            elif counter%2==1:
                                counter+=1
                                TacSprite.add(TacDic[5])
                                ch5=2
                                     
               
                    
    pg.display.flip()    
    while run is True:
        try:
            data2=arduino.readline()[:2]
        except SerialException:
            sys.exit()        
        u=str(counter%2+1)
        u=u.rstrip('\x00')
        u=str.encode(u)
        arduino.write(bytes(u))
        print(bytes(u))        
        dataC=arduino.readline()[:2]
        data=str(dataC, 'utf-8')
        
        
        
        
        
        if data:
            data=eval(data)
        
        if data==1:
            
            if ch1==0: #gdy wartosc ch% jest zero to znaczy ze na danym polu nie ma zadnej figury-czyli mozna je wybrac
                if counter%2==0: #gdy reszta z dzielenia przez 2 jest rowna 1 jest kolej kolka
                    counter+=1
                    TicSprite.add(TicDic[1])
                    ch1=1 #gdy narysowane jest na nim kolko ch% jest rowne 1
                elif counter%2==1:#kolej kryzyka
                    counter+=1
                    TacSprite.add(TacDic[1])
                    ch1=2 #gdy narysowany jest na nim krzyzyk ch% jest rowne 2
                
            else: #gdy ch% jest rozne od zera nie mozemy go wybrac
                pass            
        elif data==2:
                
                if ch2==0:
                    if counter%2==0: 
                        counter+=1
                        TicSprite.add(TicDic[2])
                        ch2=1
                    elif counter%2==1:
                        counter+=1
                        TacSprite.add(TacDic[2])
                        ch2=2
                    
                else:
                    pass
        elif data==3:
                
                if ch3==0:
                    if counter%2==0: 
                        counter+=1
                        TicSprite.add(TicDic[3])
                        ch3=1
                    elif counter%2==1:
                        counter+=1
                        TacSprite.add(TacDic[3])
                        ch3=2
                    
                else:
                    pass
        elif data==4:
                if ch4==0:
                    if counter%2==0: 
                        counter+=1
                        TicSprite.add(TicDic[4])
                        ch4=1
                    elif counter%2==1:
                        counter+=1
                        TacSprite.add(TacDic[4])
                        ch4=2
                    
                else:
                    pass
        elif data==5:
            if ch5==0:
                if counter%2==0: 
                    counter+=1
                    TicSprite.add(TicDic[5])
                    ch5=1
                elif counter%2==1:
                    counter+=1
                    TacSprite.add(TacDic[5])
                    ch5=2
                
            else:
                pass
        elif data==6:
            if ch6==0:
                if counter%2==0: 
                    counter+=1
                    TicSprite.add(TicDic[6])
                    ch6=1
                elif counter%2==1:
                    counter+=1
                    TacSprite.add(TacDic[6])
                    ch6=2
                
            else:
                pass
        elif data==7:
            if ch7==0:
                if counter%2==0: 
                    counter+=1
                    TicSprite.add(TicDic[7])
                    ch7=1
                elif counter%2==1:
                    counter+=1
                    TacSprite.add(TacDic[7])
                    ch7=2
                        
                else:
                    pass
        elif data==8:
            if ch8==0:
                if counter%2==0: 
                    counter+=1
                    TicSprite.add(TicDic[8])
                    ch8=1
                elif counter%2==1:
                    counter+=1
                    TacSprite.add(TacDic[8])
                    ch8=2
                
            else:
                pass
        elif data==9:
            if ch9==0:
                if counter%2==0: 
                    counter+=1
                    TicSprite.add(TicDic[9])
                    ch9=1
                elif counter%2==1:
                    counter+=1
                    TacSprite.add(TacDic[9])
                    ch9=2
                
            else:
                pass            
            
            
                
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()    
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                
        data=0              
    #updatujemy wszystkie sprity
        TicSprite.update()
        TicSprite.clear(window, background)
        TicSprite.draw(window)   
        TacSprite.update()
        TacSprite.clear(window, background)
        TacSprite.draw(window)     
        #print(ch2,ch3,counter)
        #srodkowy pasek pionowy
        if ch4==ch5==ch6==1:
            line=pg.image.load('vertRLineMid.png')
            screen.blit(line,(0,0))
            run=False
            finish=True
        elif ch1==ch2==ch3==1:
            line=pg.image.load('vertRLineLeft.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch1==ch5==ch9==1:
            line=pg.image.load('angRLine1.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch7==ch8==ch9==1:
            line=pg.image.load('vertRlineRight.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch3==ch5==ch7==1:
            line=pg.image.load('angRLine.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch2==ch5==ch8==1:
            line=pg.image.load('horRLine.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch1==ch4==ch7==1:
            line=pg.image.load('horRLineTop.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch3==ch6==ch9==1:
            line=pg.image.load('horRLineBot.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch4==ch5==ch6==2:
            line=pg.image.load('vertBLineMid.png')
            screen.blit(line,(0,0))
            run=False
            finish=True
        elif ch1==ch2==ch3==2:
            line=pg.image.load('vertBLineLeft.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch1==ch5==ch9==2:
            line=pg.image.load('angBLine1.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch7==ch8==ch9==2:
            line=pg.image.load('vertBlineRight.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch3==ch5==ch7==2:
            line=pg.image.load('angBLine.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch2==ch5==ch8==2:
            line=pg.image.load('horBLine.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch1==ch4==ch7==2:
            line=pg.image.load('horBLineTop.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        elif ch3==ch6==ch9==1:
            line=pg.image.load('horBLineBot.png')
            screen.blit(line,(0,0))
            finish=True
            run=False
        emptylist=[]    
        listCh=[ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9]
        for i in listCh:
            if  bool(i) is True:
                emptylist.append(True)
        if len(emptylist)==9:
            finish=True
            run=False            
        pg.display.flip()
        
        
    while finish is True:
        try:
            data2=arduino.readline()[:2]
        except SerialException:
            sys.exit()        
                
        data1=arduino.readline()[:2]
        data1=str(data1, 'utf-8') 
        if data1:
            data1=eval(data1)    
            
        gameover = pg.image.load('gameover.png')
        screen = pg.display.get_surface()
        screen.blit(gameover,(0,0))
        pg.display.flip()
        if data1==5:
            start = True
            finish=False        
            data=0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()  
            elif event.type == pg.KEYDOWN:
                start = True
                finish=False            
        
                

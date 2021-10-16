#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:39:46 2021

@author: caojiajia
"""
#pip install pygame 先安裝遊戲設計套件

import pygame,sys,os,random
pygame.init()

#載入玻璃獸圖片
class rect():
    def __init__(self,filename,initial_position):
        self.image=pygame.image.load('niffler.png')
        self.rect=self.image.get_rect() #抓取圖片大小
        self.rect.topleft=initial_position #抓好圖片跟尺寸之後再顯示
  
#載入加隆圖片
class goldrect(pygame.sprite.Sprite):
    def __init__(self,gold_position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Galleon.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=gold_position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)

        
        

#背景
def drawback(): 
    my_back=pygame.image.load('斜角巷.jpeg') 
    bakscreen.blit(my_back,[0,0])

        
def loadtext(levelnum,score,highscore):
    my_font=pygame.font.SysFont(None,24)
    levelstr='Level:'+str(levelnum)   #金幣掉落速度的等級
    text_screen=my_font.render(levelstr, True, (11, 23, 70))
    bakscreen.blit(text_screen, (650,50))
    highscorestr='Higescore:'+str(highscore)   #最高分
    text_screen=my_font.render(highscorestr, True, (25, 25, 112))
    bakscreen.blit(text_screen, (650,80))
    scorestr='Score:'+str(score)    #分數
    text_screen=my_font.render(scorestr, True, (61, 89, 171))
    bakscreen.blit(text_screen, (650,110))    

def loadgameover(scorenum,highscore):
    my_font=pygame.font.SysFont(None,50)  #遊戲結束
    levelstr='GAME OVER'
    over_screen=my_font.render(levelstr, True, (178, 34, 34))
    bakscreen.blit(over_screen, (300,240))
    highscorestr='YOUR SCORE IS '+str(scorenum)  #這次玩的分數
    over_screen=my_font.render(highscorestr, True, (178, 34, 34))
    bakscreen.blit(over_screen, (280,290))
    if scorenum>int(highscore):   #載入歷史最高分
        highscorestr='YOUR HAVE GOT THE HIGHEST SCORE!'
        text_screen=my_font.render(highscorestr, True, (255, 215, 0))
        bakscreen.blit(text_screen, (100,340))
        highfile=open('highscore','w')
        highfile.writelines(str(scorenum)) #寫入最高分紀錄 
        highfile.close()  
    
def gethighscore(): #讀取最高分檔案
    if os.path.isfile('highscore'):  #判斷路徑
        highfile=open('highscore','r')
        highscore=highfile.readline() 
        highfile.close() 
    else:
        highscore=0
    return highscore
                  
bakscreen=pygame.display.set_mode([800,600])
bakscreen.fill([0,160,233])
pygame.display.set_caption('玻璃獸和他的加隆們')
drawback()



levelnum=1 #降落速度level
scorenum=0 #得分
highscore=gethighscore()#最高分

ileft=1  #記錄向左移動步數、控制圖片
iright=10 #記錄向左移動步數、控制圖片

x=100
y=450
filename='niffler.png'
backimg_ren=rect(filename,[x,y])
bakscreen.blit(backimg_ren.image,backimg_ren.rect)
loadtext(levelnum,scorenum,highscore)
goldx=random.randint(50,580)
speed=[0,levelnum]
mygold=goldrect([goldx,100],speed) 
pygame.display.update()

while True:
    if scorenum>0 and scorenum/50.0==int(scorenum/50.0):#每50分增加一個level
        levelnum=scorenum/50+1
        speed=[0,levelnum]
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    #make gold    

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:#按下左键

        drawback()  
        loadtext(levelnum,scorenum,highscore)

        if iright > 14 :iright=10
        iright=iright+1
        filename='image\\'+str(iright)+'.png' #移動的迴圈
        if x<50 :
            x=50
        else:
            x=x-10

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

        
    if pressed_keys[pygame.K_RIGHT]:#按下右键

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if ileft > 4 :ileft=0
        ileft=ileft+1
        filename='image\\'+str(ileft)+'.png'
        if x>560:
            x=560
        else:
            x=x+10

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

    drawback()
    loadtext(levelnum,scorenum,highscore)
    mygold.move()
    bakscreen.blit(mygold.image,mygold.rect) 
    
    backimg_surface=rect(filename,[x,y])
    bakscreen.blit(backimg_surface.image,backimg_surface.rect)
    if mygold.rect.top>600:#判斷有沒有接到金幣、金幣落地遊戲結束
        loadgameover(scorenum,highscore)
    if mygold.rect.colliderect(backimg_surface.rect):#判斷有沒有接到金幣
        scorenum+=5
        loadtext(levelnum,scorenum,highscore)
        goldx=random.randint(50,580)
        mygold=goldrect([goldx,100],speed) 
    pygame.display.update()
    


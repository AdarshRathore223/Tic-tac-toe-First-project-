from subprocess import REALTIME_PRIORITY_CLASS
import pygame as p,sys,time
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import *
import random

p.init()

p.display.set_caption('TIC TAC TOE')
loss=p.image.load('image/lost.png')
background=p.image.load('image/bg.png')
background2=p.image.load('image/background2.png')
image = p.image.load('image/intro.png')
image2 = p.image.load('image/button.png')
retryimg=p.image.load('image/retry.png')
exitimg=p.image.load('image/exit.png')
youwin=p.image.load('image/win.png')
gamedraw=p.image.load('image/draw-game.png')
youwin = p.transform.scale(youwin,(600,500)) 
screen = p.display.set_mode( (1000,1000))
exitimg=p.transform.scale(exitimg,(100,100))
image = p.transform.scale(image,(500,250))
loss = p.transform.scale(loss,(600,500)) 
retryimg=p.transform.scale(retryimg,(150,150))
image2 = p.transform.scale(image2,(150,150))
background = p.transform.scale(background,(1000,1000)) 
background2 = p.transform.scale(background2,(1000,1000)) 
def pmove():
    while True:
        coordm=None
        for event in p.event.get():
            if event.type == p.QUIT:
             sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
             coordm= p.mouse.get_pos()
             if 333>coordm[0]>0 and 333>coordm[1]>0 and matrix[0][0]==0: # 1,1 
              radius,width=100,30
              matrix[0][0]=5
              p.draw.circle(screen,(224,255,255),(166,166),radius,width)
              p.display.update()
              return
             elif 666>coordm[0]>333 and 333>coordm[1]>0 and matrix[0][1]==0: #1,2 
              radius,width=100,30
              matrix[0][1]=5
              p.draw.circle(screen,(224,255,255),(499,166),radius,width)
              p.display.update()
              return
             elif 333>coordm[1]>0 and 999>coordm[0]>666 and matrix[0][2]==0: #1,3 
              radius,width=100,30
              matrix[0][2]=5
              p.draw.circle(screen,(224,255,255),(832,166),radius,width)
              p.display.update()
              return
             elif 333>coordm[0]>0 and 666>coordm[1]>333 and matrix[1][0]==0: #2,1 
              radius,width=100,30
              matrix[1][0]=5
              p.draw.circle(screen,(224,255,255),(166,499),radius,width)
              p.display.update()
              return
             elif 666>coordm[0]>333 and 666>coordm[1]>333 and matrix[1][1]==0:  #2,2
              radius,width=100,30
              matrix[1][1]=5
              p.draw.circle(screen,(224,255,255),(499,499),radius,width)
              p.display.update()
              return
             elif 666>coordm[1]>333 and 999>coordm[0]>666 and matrix[1][2]==0:  #2,3
              radius,width=100,30
              matrix[1][2]=5
              p.draw.circle(screen,(224,255,255),(832,499),radius,width)
              p.display.update()
              return
             elif 333>coordm[0]>0 and 999>coordm[1]>666 and matrix[2][0]==0: #3,1 
              radius,width=100,30
              matrix[2][0]=5
              p.draw.circle(screen,(224,255,255),(166,832),radius,width)
              p.display.update()
              return
             elif 666>coordm[0]>333 and 999>coordm[1]>666 and matrix[2][1]==0:  #3,2
              radius,width=100,30
              matrix[2][1]=5
              p.draw.circle(screen,(224,255,255),(499,832),radius,width)
              p.display.update()
              return
             elif 999>coordm[0]>666 and 999>coordm[1]>666 and matrix[2][2]==0:  # 3,3
              radius,width=100,30
              matrix[2][2]=5
              p.draw.circle(screen,(224,255,255),(832,832),radius,width)
              p.display.update()
              return
def start():
    global losss,matrix
    pmove() 
    if matrix[1][1]==0:
        draw_cross(1,1)
    else:    
        check_win()
        check()
        check_win()
        if losss==1:
            return
    while True:
        pmove()
        check_win()
        if losss==1:
            return
        check()
        check_win()
        if losss==1:
            return
def check_win():
    for a1 in range(0,3):
        a2=0
        if matrix[a1][a2]+matrix[a1][a2+1]+matrix[a1][a2+2]==300:
           p.display.update()
           lose() 
           
    for a2 in range(0,3):
        a1=0
        if matrix[a1][a2]+matrix[a1+1][a2]+matrix[a1+2][a2]==300:
           lose()
    if matrix[0][0]+matrix[1][1]+matrix[2][2]==300:
           lose()
    if matrix[0][2]+matrix[1][1]+matrix[2][0]==300:
           lose()  
    for a1 in range(0,3):
        a2=0
        if matrix[a1][a2]+matrix[a1][a2+1]+matrix[a1][a2+2]==15:
          win() 
           
    for a2 in range(0,3):
        a1=0
        if matrix[a1][a2]+matrix[a1+1][a2]+matrix[a1+2][a2]==15:
          win()
    if matrix[0][0]+matrix[1][1]+matrix[2][2]==15:
          win()
    if matrix[0][2]+matrix[1][1]+matrix[2][0]==15:
          win()    
    if matrix[0][0]!=0 and matrix[0][1]!=0 and matrix[0][2]!=0 and matrix[1][0]!=0 and matrix[1][1]!=0 and matrix[1][2]!=0 and matrix[2][0]!=0 and matrix[2][1]!=0 and matrix[2][2]!=0:
        draw()
def check():
        global beg
        work=0
        a=0
        loop=0
        work1=0        
        if loop==0:
            for a1 in range(0,3):
                a2=0 
                if matrix[a1][a2]+matrix[a1][a2+1]+matrix[a1][a2+2]==200:
                    loop=1
                    if matrix[a1][a2]==0:
                            draw_cross(a1,a2)
                    elif matrix[a1][a2+1]==0:
                            draw_cross(a1,a2+1)
                    elif matrix[a1][a2+2]==0:
                            draw_cross(a1,a2+2)
        
            for a2 in range(0,3):
                a1=0 
                if matrix[a1][a2]+matrix[a1+1][a2]+matrix[a1+2][a2]==200:
                    loop=1
                    if matrix[a1][a2]==0:
                            draw_cross(a1,a2)
                    elif matrix[a1+1][a2]==0:
                            draw_cross(a1+1,a2)
                    elif matrix[a1+2][a2]==0:
                                draw_cross(a1+2,a2)
        if loop==0 and work1==0:
            if matrix[0][0]+matrix[2][2]==10 or matrix[0][2]+matrix[2][0]==10:
               loop=1
               work1=1
               num=random.randint(0,3)
               if num==0 and matrix[1][0]==0:
                   draw_cross(1,0)
                   print(num)
               elif num==1 and matrix[0][1]==0:
                   draw_cross(0,1)
                   print(num)
               elif num==2 and matrix[2][1]==0:
                   draw_cross(2,1)
                   print(num)
               elif num==3 and matrix[1][2]==0:
                   print(num)
                   draw_cross(1,2)                        
        if loop==0:
            if matrix[0][0]+matrix[1][1]+matrix[2][2]==200:
                loop=1
                if matrix[0][0]==0:
                            draw_cross(0,0)
                elif matrix[1][1]==0:
                            draw_cross(1,1)
                elif matrix[2][2]==0:
                            draw_cross(2,2)
        if loop==0:
            if matrix[0][2]+matrix[1][1]+matrix[2][0]==200:
                loop=1
                
                if matrix[0][2]==0:
                            draw_cross(0,2)
                elif matrix[1][1]==0:
                            draw_cross(1,1)
                elif matrix[2][0]==0:
                            draw_cross(2,0)
                p.display.update()


        if loop==0:
            for a1 in range(0,3):
                    a2=0 
                    if matrix[a1][a2]+matrix[a1][a2+1]+matrix[a1][a2+2]==10:
                        work=1
                        if matrix[a1][a2]==0:
                            draw_cross(a1,a2)
                        elif matrix[a1][a2+1]==0:
                            draw_cross(a1,a2+1)
                        elif matrix[a1][a2+2]==0:
                            draw_cross(a1,a2+2)
            if work==0:
                for a2 in range(0,3):
                        a1=0
                        if matrix[a1][a2]+matrix[a1+1][a2]+matrix[a1+2][a2]==10:
                            work=1
                            if matrix[a1][a2]==0:
                                draw_cross(a1,a2)
                            elif matrix[a1+1][a2]==0:
                                draw_cross(a1+1,a2)
                            elif matrix[a1+2][a2]==0:
                                draw_cross(a1+2,a2)
            if work==0:
                if matrix[0][0]+matrix[1][1]+matrix[2][2]==10:
                    work=1
                    if matrix[0][0]==0:
                        draw_cross(0,0)
                    elif matrix[1][1]==0:
                        draw_cross(1,1)
                    elif matrix[2][2]==0:
                        draw_cross(2,2)
            if work==0:
                if matrix[0][2]+matrix[1][1]+matrix[2][0]==10:
                    work=1
                    if matrix[0][2]==0:
                        draw_cross(0,2)
                    elif matrix[1][1]==0:
                        draw_cross(1,1)
                    if matrix[2][0]==0:
                        draw_cross(2,0)
            if work==0:
                if matrix[0][0]==0:
                        work=1
                        draw_cross(0,0)
                elif matrix[2][0]==0:
                        work=1
                        draw_cross(2,0)
                elif matrix[0][2]==0:
                        work=1
                        draw_cross(0,2)
                elif matrix[2][2]==0:
                        work=1
                        draw_cross(2,2)
        if loop==0:
            print('condition matched')
            for a1 in range(0,3):
                for a2 in range(0,3):
                    if a==0 and work==0:
                        if matrix[a1][a2]==0:
                            a=1
                            draw_cross(a1,a2)
def draw_cross(x,y):
    if x==0 and y==0:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400-loc,375-loc),(600-loc,625-loc), 30)
       p.draw.line(screen, (255,0,0),(400-loc,625-loc),(600-loc,375-loc), 30)
       p.display.update()
    if x==0 and y==1:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400,375-loc),(600,625-loc), 30)
       p.draw.line(screen, (255,0,0),(400,625-loc),(600,375-loc), 30)
       p.display.update() 
    if x==0 and y==2:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400+loc,375-loc),(600+loc,625-loc), 30)
       p.draw.line(screen, (255,0,0),(400+loc,625-loc),(600+loc,375-loc), 30)
       p.display.update()
    if x==1 and y==0:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400-loc,375),(600-loc,625), 30)
       p.draw.line(screen, (255,0,0),(400-loc,625),(600-loc,375), 30)
       p.display.update() 
    if x==1 and y==1:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400,375),(600,625), 30)
       p.draw.line(screen, (255,0,0),(400,625),(600,375), 30)
       p.display.update() 
    if x==1 and y==2:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400+loc,375),(600+loc,625), 30)
       p.draw.line(screen, (255,0,0),(400+loc,625),(600+loc,375), 30)
       p.display.update()
    if x==2 and y==0:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400-loc,375+loc),(600-loc,625+loc), 30)
       p.draw.line(screen, (255,0,0),(400-loc,625+loc),(600-loc,375+loc), 30)
       p.display.update() 
    if x==2 and y==1:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400,375+loc),(600,625+loc), 30)
       p.draw.line(screen, (255,0,0),(400,625+loc),(600,375+loc), 30)
       p.display.update() 
    if x==2 and y==2:
       matrix[x][y]=100
       p.draw.line(screen, (255,0,0),(400+loc,375+loc),(600+loc,625+loc), 30)
       p.draw.line(screen, (255,0,0),(400+loc,625+loc),(600+loc,375+loc), 30)
       p.display.update()
def drawgrid():
    screen.blit( background,(0,0))
    p.draw.line(screen,(224,255,255),(0,333),(1000,333),10)
    p.draw.line(screen,(224,255,255),(0,666),(1000,666),10)
    p.draw.line(screen,(224,255,255),(333,0),(333,1000),10)
    p.draw.line(screen,(224,255,255),(666,0),(666,1000),10)
    p.display.update()
def lose():
    global losss,matrix
    losss=1
    time.sleep(2)
    screen.blit(background,(0,0))
    screen.blit(loss,(250,50))
    screen.blit(retryimg,(450,600))
    screen.blit(exitimg,(450,800))
    p.display.update()
def win():
    global losss,matrix
    losss=1
    time.sleep(2)
    screen.blit(background,(0,0))
    screen.blit(youwin,(250,50))
    screen.blit(retryimg,(450,600))
    screen.blit(exitimg,(450,800))
    p.display.update()
def draw():
    global losss,matrix
    losss=1
    p.display.update()
    time.sleep(2)
    screen.blit(background,(0,0))
    screen.blit(gamedraw,(-270,150))
    screen.blit(retryimg,(450,600))
    screen.blit(exitimg,(450,800))
    p.display.update()

loop1=1
while loop1==1:
    loc=333
    condition=1
    x,y=0,0
    losss,beg=0,0
    loop1,loop2,loop3=1,1,1
    screen.blit(background,(0,0))
    screen.blit(image,(250,150))
    screen.blit(image2,(450,500))
    matrix=[[0,0,0],[0,0,0],[0,0,0]]
    for event in p.event.get():
        if event.type == p.QUIT:
         sys.exit()
        if event.type == p.MOUSEBUTTONDOWN:
            coor=0
            coor= p.mouse.get_pos()
            if 578>coor[0]>475 and 521<coor[1]<622:
                while loop2==1:
                    screen.blit(background,(0,0))
                    drawgrid()
                    start()
                    loop2=0
                    matrix=[[0,0,0],[0,0,0],[0,0,0]]
                    while loop3==1:
                        for event in p.event.get():
                            if event.type == p.QUIT:
                             sys.exit()
                            if event.type == p.MOUSEBUTTONDOWN:
                             Retry= p.mouse.get_pos()
                             print(Retry)
                             if 604>Retry[0]>343 and 787>Retry[1]>600:
                                loop3=0
                                loop1=1
                                p.display.update() 
        p.display.update()
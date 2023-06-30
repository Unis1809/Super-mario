import time

import pygame
from pygame.locals import *
pygame.init()
screen_W=900
screen_H=900
screen = pygame.display.set_mode((screen_W,screen_H))
size=100
over=0
score=0
mainmenu=True
pygame.display.set_caption("Super Fangelton")
fontt=pygame.font.SysFont("Times New Roman",30,"bold")
fonti=pygame.font.SysFont("Times New Roman",90,"bold")
white=(0,0,0)
run=True
mlevel=3
level=1
world_data=[
[1,1,1,1,1,1,1,1,1],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,4],
 [0,0,0,0,0,0,1,1,1],
 [1,1,1,0,0,0,1,1,1],
 [0,3,3,0,2,0,0,0],
 [1,1,1,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [1,1,1,1,1,1,1,1,1]]
def reee(level):
    player.res(x, 0, screen_H - 150)
    w.empty()
    ene.empty()
    cu.empty()
    cuu.empty()
    if level==1:
        world_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 3, 3, 0, 2, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]


    if level==2:
        world_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 3, 1, 1, 1, 1, 4],
            [0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 2, 3, 0, 0, 0, 3, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 3, 3, 0, 2, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

    if level == 3:
        world_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 4, 1],
            [0, 2, 3, 0, 0, 1, 3, 2, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 3, 3, 1, 0, 2, 0, 0,0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    worldd = game(world_data)
    return worldd

def drawtext(text,font,textcol,x,y):
    imge=font.render(text,True,textcol)
    screen.blit(imge,(x,y))




def draw():
    for line in range (0,10):
        pygame.draw.line(screen,(100,100,100),(0,line*size),(screen_W,line*size))
        pygame.draw.line(screen,(100,100,100),(line*size,0),(line*size,screen_H))
background=pygame.image.load("images\\mn.jpg")
resi=pygame.image.load("images\\e-removebg-preview.png")
start=pygame.image.load("images\\st-removebg-preview.png")
exitt=pygame.image.load("images\\exit-removebg-preview.png")
class but():
    def __init__(self,x,y,image):
       self.image=image
       self.rect=self.image.get_rect()
       self.rect.x=x
       self.rect.y=y
       self.click=False


    def draw(self):
        act=False
        p=pygame.mouse.get_pos()
        if self.rect.collidepoint(p):
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                act=True
                self.click=True


        if pygame.mouse.get_pressed()[0]==0:
            self.click=False

        screen.blit(self.image, self.rect)

        return act
res = but(50, 50, resi)
class player():
    def __init__(self,x,y):
        self.res(x,900)
    def update(self,over):
        dx=0
        dy=0
        if over ==0:
            k=pygame.key.get_pressed()
            if k[pygame.K_UP] :
                self.vy=-7



            if k[pygame.K_LEFT]:
                dx -= 2
            if k[pygame.K_RIGHT]:
                dx += 2
            self.vy += 1
            if self.vy > 4:
                self.vy = 4
            dy += self.vy
            self.in_a=True
            for lin in g.list:
                if lin[1].colliderect(self.rect.x+dx, self.rect.y , self.width, self.h):
                    dx=0
                if lin[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.h):
                    if self.vy<0:
                        dy=lin[1].bottom-self.rect.top
                    elif self.vy >= 0:
                        dy = lin[1].top - self.rect.bottom
                        self.vy=0
                        self.in_a=False

            if pygame.sprite.spritecollide(self,ene,False):
                over=-1
            if pygame.sprite.spritecollide(self, w, False):
                over=1

            self.rect.y += dy
            self.rect.x += dx
            if self.rect.bottom>screen_H:
                self.rect.bottom=screen_H

            if self.rect.right>screen_W:
                self.rect.right=screen_W
            if self.rect.left<0:
                self.rect.left=0
        elif over==-1:

            if self.rect.y>300:
                self.rect.y-=5



        screen.blit(self.image, self.rect)
        return over


    def res(self,x,y):
        laiib = pygame.image.load("images\\playr-removebg-preview.png")
        
        self.image = pygame.transform.scale(laiib, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.h = self.image.get_height()
        self.vy=0
        self.in_a=True
class game():
    def __init__(self,data):
        self.list=[]
        mokab=pygame.image.load("images\\sq.png")
        rcount=0
        for row in data:
            ccount=0
            for lin in row:
                if lin==1:
                    img=pygame.transform.scale(mokab,(size,size))
                    rect=img.get_rect()
                    rect.x=ccount*size
                    rect.y=rcount*size
                    lin=(img,rect)
                    self.list.append(lin)
                if lin==2:
                    blob=enemy(ccount*size,rcount*size+45)
                    ene.add(blob)
                if lin==3:
                    blo = cup(ccount * size, rcount * size + 5)
                    cu.add(blo)

                if lin==4:
                    blodd = won(ccount * size, rcount * size + 15)
                    w.add(blodd)

                ccount=ccount+1
            rcount=rcount+1
    def draw(self):
        for lin in self.list:
            screen.blit(lin[0],lin[1])
            pygame.draw.rect(screen,(255,255,255),lin[1],2)
class enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images\\download (1).png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y=y
        self.move=1
        self.c=0
    def update(self):
        self.rect.x+=self.move
        self.c+=1
        if self.c>30:
            self.move*=-1
            self.c*=-2
class cup(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        imge = pygame.image.load("images\\cc-removebg-preview.png")
        self.image=pygame.transform.scale(imge,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class won(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        imge = pygame.image.load("images\\ssss-removebg-preview.png")
        self.image=pygame.transform.scale(imge,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y



world_data=[
[1,1,1,1,1,1,1,1,1],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,4],
 [0,0,0,0,0,0,1,1,1],
 [1,1,1,0,0,0,1,1,1],
 [0,3,3,0,2,0,0,0],
 [1,1,1,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [1,1,1,1,1,1,1,1,1]]
ene=pygame.sprite.Group()
cu=pygame.sprite.Group()
cuu=pygame.sprite.Group()
w=pygame.sprite.Group()
g=game(world_data)
x=player(0,100)
res=but(50,50,resi)
stt=but(50,400,start)
exi=but(900-400,400,exitt)




run=True
while run:
    screen.blit(background,(0,0))
    


    if mainmenu==True:
        if exi.draw():
            run=False
        if stt.draw():
            mainmenu=False


    else:
        g.draw()
        if over==1:
            drawtext(" You won my heart", fontt, white, 350, 450)
        if over==0:
            ene.update()

            if pygame.sprite.spritecollide(x,cu,True):
                score+=1


        drawtext("Score "+str(score),fontt,white,13,20)
        drawtext("Level " + str(level), fontt, white, 13, 830)
        cu.draw(screen)
        ene.draw(screen)
        w.draw(screen)
        over=x.update(over)

        if over == -1:
            if res.draw():

                g = reee(level)
                over=0
                score=0
            if score==0:
                drawtext(" GameOver " + str(score) + " Cups", fontt, white, 350, 450)

        if over==1:
            level+=1
            if level<=mlevel:
                world_data=[]
                g=reee(level)
                over=0
            else:
                if res.draw():
                    level=1
                    world_data = []
                    g = reee(level)
                    over = 0



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    pygame.display.update()

pygame.quit()
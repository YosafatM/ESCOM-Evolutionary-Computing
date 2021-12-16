import pygame
import numpy as np
import time
from random import randint

width, height = 1000, 1000
nxC, nyC = 50, 50
dimCW = width/nxC
dimCH = height/nyC
b1=2
b2=6
s1=3
s2=7
u1=1
u2=8
r1=1
r2=4
pygame.init()

screen = pygame.display.set_mode([height, width])

bg = 0, 0, 0
screen.fill(bg)

gameState = np.zeros((nxC, nyC))


pauseExect = True
running = True

Q0 = 0, 0, 0  # Campo libre
Q1 = 0, 255, 255  # Nutriente no encontrado
Q2 = 139, 0, 155  # Repelente

mins = np.zeros((nxC, nyC))
cont = 0
val = np.zeros((nxC, nyC))
incre = 0


def getMoore(n_neigh, crit):
    x = 0
    if(n_neigh[0] == crit):
        x +=1
    if(n_neigh[1] == crit):
        x +=1
    if(n_neigh[2] == crit):
        x +=1
    if(n_neigh[3] == crit):
        x +=1
    if(n_neigh[4] == crit):
        x +=1
    if(n_neigh[5] == crit):
        x +=1
    if(n_neigh[6] == crit):
        x +=1
    if(n_neigh[7] == crit):
        x +=1
    return x

while running:

    aux = np.copy(gameState)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            if mouseClick[0] == 1:
                aux[celX, celY] = 1
            else:
                aux[celX, celY] = 2
    screen.fill(bg)
    #print(val)
    for x in range(0, nxC):
        for y in range(0, nyC):
            if not pauseExect:
                n_neigh = np.array([gameState[(x-1) % nxC, (y-1) % nyC], 
                                    gameState[(x) % nxC, (y-1) % nyC], 
                                    gameState[(x+1) % nxC, (y-1) % nyC], 
                                    gameState[(x-1) % nxC, (y) % nyC], 
                                    gameState[(x+1) % nxC, (y) % nyC], 
                                    gameState[(x-1) % nxC, (y+1) % nyC], 
                                    gameState[(x) % nxC, (y+1) % nyC], 
                                    gameState[(x+1) % nxC, (y+1) % nyC]])
                
                # Q0
                if gameState[x, y] == 0:
                    if (getMoore(n_neigh,1)>b1 and getMoore(n_neigh,1)<b2):
                        aux[x, y] = 1
                    else:
                        aux[x, y] = 0
                # Q1
                elif gameState[x, y] == 1:
                    if (getMoore(n_neigh,1)>s1 and getMoore(n_neigh,1)<s2):
                        aux[x, y] = 1
                    elif (getMoore(n_neigh,2)>u1 and getMoore(n_neigh,2)<u2):
                        aux[x, y] = 2
                    else:
                        aux[x, y] = 0
                # Q2
                elif gameState[x, y] == 2:
                    if (getMoore(n_neigh,2)>r1 and getMoore(n_neigh,2)<r2):
                        aux[x, y] = 2  
                    else:
                        aux[x, y] = 0                        
                
                    
            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]

            if(aux[x, y] == 0):
                pygame.draw.polygon(screen, (Q0), poly, 0)
            elif(aux[x, y] == 1):
                pygame.draw.polygon(screen, (Q1), poly, 0)
            elif(aux[x, y] == 2):
                pygame.draw.polygon(screen, (Q2), poly, 0)

    gameState = np.copy(aux)
    time.sleep(0.1)
    pygame.display.flip()

pygame.quit()

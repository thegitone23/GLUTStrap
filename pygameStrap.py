#This is a pyOpenGL+pygame code template 

#importing stuff
#pygame imports
import pygame
from pygame.locals import *
#opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *
#other imports
import math

#defing functions for basic shapes
def drawPixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def drawLine(a,b,c,d):
    glBegin(GL_LINES)
    glVertex2f(a,b)
    glVertex2f(c,d)
    glEnd()

def drawCircle(x,y,r=50):
    toRad = (math.pi/180)
    for i in range (0,360):
        drawPixel(x+(r*math.cos(toRad*i)),y+(r*math.sin(toRad*i)))

#main drawing logic
def draw():
    #coding logic here
    drawCircle(0,0)


#main function
def main():
    #boiler-plate setup code
    pygame.init()
    display = (800,600) #the pygame windows resolution
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(0,800,600,0) #defining drawing limits

    #the main loop 
    while True:

        #event hadling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear the frame
        draw() #calling the function with drawing logic
        pygame.display.flip() #bring up the updated screen

#calling main()
main()

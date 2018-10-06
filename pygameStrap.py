#This is a pyOpenGL+pygame code template 

#importing stuff
#pygame imports
import pygame
from pygame.locals import *
#opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    #coding logic here
    print("Working!!!")


#main function
def main():
    #boiler-plate setup code
    pygame.init()
    display = (800,600) #the pygame windows resolution
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(65,display[0]/display[1],0.1,20.0)
    glTranslatef(0.0,0.0,-5)
    
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

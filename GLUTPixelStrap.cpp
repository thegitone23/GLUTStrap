//This Is A Basic GLUT Pixel Drawing Program Template
//Put Your Drawing Logic In draw()
//Assuming GLUT Has Been Set-Up To Be Used With GCC
//Build Using g++ GLUTStrap.cpp  glut32.lib -lopengl32 -lglu32
//Executable Generated Will Require glut32.dll And glut32.lib In The Same Folder (On Windows)
#include <GL/glut.h>

//draw a pixel at x,y
void drawPixel(GLint x, GLint y)
{
    glBegin(GL_POINTS);
        glVertex2i(x,y);
    glEnd();
}

//draw whatever you feel like in here
void draw()
{
    //Code Your Drawing Logic Here
    
    
    glFlush();
}

//intializing stuff
void init()
{
    glutInitWindowSize(800,600);
    glutCreateWindow("MyGLUTProgram");
    glClearColor(0,0,0,0); //setting clear to black
    glClear(GL_COLOR_BUFFER_BIT); //applying the clear
    glColor3f(0.8,0.0,0.0); //drawings will have red shade
    gluOrtho2D(-399,400,-299,300); //defined limits in which to draw
}

int main(int argc, char **argv)
{
    glutInit(&argc,argv); 
    init();
    glutDisplayFunc(draw);
    glutMainLoop();
}

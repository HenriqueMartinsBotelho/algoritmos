#include <GL/glut.h>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <iostream>


using namespace std;

struct Point{
    float x, y;
    unsigned char r, g, b;
};


std::vector< Point > points;



void display(void){
    /* glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glShadeModel(GL_FLAT); 
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    //glOrtho(-50, 50, -50, 50, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glColor3ub( 255, 255, 255 );
    glEnableClientState( GL_VERTEX_ARRAY );
    glEnableClientState( GL_COLOR_ARRAY );
    glVertexPointer( 2, GL_FLOAT, sizeof(Point), &points[0].x );
    glColorPointer( 3, GL_UNSIGNED_BYTE, sizeof(Point), &points[0].r );
    glLineWidth( 3.0 );
    glPointSize(3.0);
    glDrawArrays( GL_LINE_STRIP, 0, points.size() );
    glDisableClientState( GL_VERTEX_ARRAY );
    glDisableClientState( GL_COLOR_ARRAY );
    glFlush();
    glutSwapBuffers(); */

    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_LINES);
    glVertex2d(2,3);
    glVertex2d(4,5);
    glVertex2d(10,20);
    glVertex2d(30,40);

        //glVertex2i(points[0].x, points[0].y);
        //glVertex2i(points[1].x, points[1].y);
    glEnd();
    glFlush();


    
    







}

void reshape(int w, int h){
    glViewport(0, 0, w, h);
}

int main(int argc, char **argv)
{

    /* ifstream file ("pontosTeste.txt");
    double input = 0.0;
    double x, y;
    char separator;
    int i = 0;
    while (file >> x >> y){
        cout << x << endl;
        cout << y << endl;
        //for (int i = 0; i < 4 ; i++){
            points[i].x = x; 
            points[i].y = y;
            i++;
        //} 
    } 
    file.close(); */






  glutInit(&argc, argv);
    //glutInitDisplayMode(GLUT_SINGLE);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity(); 
    glOrtho(0, 1024, 728, 0, 0,1);

    glutInitWindowSize(1000, 600);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Hello world :D");
    glutDisplayFunc(display);
    glutMainLoop();
    

    for( size_t i = 0; i < 4; ++i ){
        Point pt;
        pt.x = 0;
        pt.y = 0;
        pt.r = rand() % 255;
        pt.g = rand() % 255;
        pt.b = rand() % 255;
        //pt.a = 255;
        points.push_back(pt);
    } 


    // Lendo os pontos de um arquivo e armazendo no vetor points
    ifstream file ("pontosTeste.txt");
    double input = 0.0;
    double x, y;
    char separator;
    int i = 0;
    while (file >> x >> y){
        points[i].x = x; 
        points[i].y = y;
        i++;
    } 
    file.close();  
    // ********************************************************


   /*    points[1].x=20;
    points[1].y=20;
    points[2].x=10;
    points[2].y=40;
    points[3].x=20;
    points[3].y=40;  */ 

    /* for (size_t i = 0; i < 4; i++){
        cout << points[i].x << endl;
        cout << points[i].y << endl;

    } */
    

    

    


    glutMainLoop();
    return 0;
}

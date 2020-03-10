def findIntersection(e1,e2):
        x1 = e1[0].x
        y1 = e1[0].y 
        x2 = e1[1].x
        y2 = e1[1].y
        x3 = e2[0].x
        y3 = e2[0].y 
        x4 = e2[1].x
        y4 = e2[1].y
        px= ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)) 
        py= ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        return [px, py]

from scipy.spatial import distance
import math
import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import os


#x = abscissa; y = ordenada; w = peso
class Ponto:
    def __init__(self, x,y,w):
        self.x = x
        self.y = y
        self.w = w
    

def w(p1,p2):
    return distance.euclidean((p1.x,p1.y),(p2.x,p2.y))*(p1.w + p2.w)/2


def findIntersection(e1,e2):
        x1 = e1[0].x
        y1 = e1[0].y 
        x2 = e1[1].x
        y2 = e1[1].y
        x3 = e2[0].x
        y3 = e2[0].y 
        x4 = e2[1].x
        y4 = e2[1].y
        px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        return [px, py]


a = Ponto(3,4,1)
b = Ponto(7,6,1)
c = Ponto(3,7,1)
d = Ponto(6,3,1)

e1 = [a,b]
e2 = [c,d]


inter = findIntersection(e1,e2)
print(inter)


'''
# Given three colinear Pontos p, q, r, the function checks if  
# Ponto q lies on line segment 'pr'  
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
  
def orientation(p, q, r): 
    # to find the orientation of an ordered triplet (p,q,r) 
    # function returns the following values: 
    # 0 : Colinear Pontos 
    # 1 : Clockwise Pontos 
    # 2 : Counterclockwise 
      
    # See https://www.geeksforgeeks.org/orientation-3-ordered-Pontos/amp/  
    # for details of below formula.  
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 
          
        # Clockwise orientation 
        return 1
    elif (val < 0): 
          
        # Counterclockwise orientation 
        return 2
    else: 
          
        # Colinear orientation 
        return 0
  
# The main function that returns true if  
# the line segment 'p1q1' and 'p2q2' intersect. 
def doIntersect(p1,q1,p2,q2): 
      
    # Find the 4 orientations required for  
    # the general and special cases 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    # General case 
    if ((o1 != o2) and (o3 != o4)): 
        return True
  
    # Special Cases 
  
    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1 
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
  
    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1 
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True
  
    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2 
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True
  
    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2 
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True
  
    # If none of the cases 
    return False
  
# Driver program to test above functions: 
p1 = Ponto(1, 1,1) 
q1 = Ponto(10, 1,1) 
p2 = Ponto(1, 2,1) 
q2 = Ponto(10, 2,1) 
  
if doIntersect(p1, q1, p2, q2): 
    print("Yes") 
else: 
    print("No") 
  
p1 = Ponto(10, 0,1) 
q1 = Ponto(0, 10,1) 
p2 = Ponto(0, 0,1) 
q2 = Ponto(10,10,1) 
  
if doIntersect(p1, q1, p2, q2): 
    print("Yes") 
else: 
    print("No") 
  
p1 = Ponto(-5,-5,1) 
q1 = Ponto(0, 0,1) 
p2 = Ponto(1, 1,1) 
q2 = Ponto(10, 10,1) 
  
if doIntersect(p1, q1, p2, q2): 
    print("Yes") 
else: 
    print("No") 

'''



'''
a = Ponto(3,4,1)
b = Ponto(7,6,1)
c = Ponto(3,7,1)
d = Ponto(6,3,1)

e1 = [a,b]
e2 = [c,d]

def cross(e1,e2):
'''
def intersect(p1, p2, p3, p4):
    d1 = (p1 - p3) * (p4 - p3) 
    d2 = (p2 - p3) * (p4 - p3)
    d3 = (p3 - p1) * (p2 - p1)
    d4 = (p4 - p1) * (p2 - p1)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True

    
    
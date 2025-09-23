def equilateral(sides):
    if sum(sides) > 0:
        if sides[0] == sides[1] == sides[2]:
            return True
        return False
    return False
    
def isosceles(sides):
    a,b,c = sides[0], sides [1], sides[2]
    if equilateral(sides):
        return True
    if sum(sides) > 0 and a + b >= c and b + c >= a and a + c >= b:
        if sides[0] == sides[1] != sides[2] or sides[0] == sides[2] != sides[1] or sides[1] == sides[2] != sides[0]:
            return True
        return False
    return False

def scalene(sides):
    a,b,c = sides[0], sides [1], sides[2]
    
    if sum(sides) > 0 and a + b >= c and b + c >= a and a + c >= b:
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
            
        return False
    return False
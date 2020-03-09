#There are 5 different ways to prove that this shape is a parallelogram. Choose one of the methods.
#1 Show that both pairs of opposite sides are congruent.
#2 Show that both pairs of opposite sides are parallel.
#3 Show that one pair of sides is parallel and congruent.
#4 Show that the diagonals bisect each other.
#4 Show that the opposite angles are congruent.

# In this example, we will show that both pairs of opposite sides are parallel.
# To do this we need to calculate the slope of each side.
# If we can show that the slopes of the opposite sides are the same, then the opposite
# sides are parallel.

#Step 2: Next, prove that the parallelogram is a rectangle.
#We can do this by showing that that the diagonals are congruent
# or by showing that one of the angles is a right angle.
#It may be easier to show that one of the angles is a right angle
# because we have already computed all of the slopes.

#If you multiply the slopes of two perpendicular lines in the plane, you get −1 . 
#That is, the slopes of perpendicular lines are opposite reciprocals .

function ehRetangulo =  fourPointsRetangle(A,B,C,D)

SlopAB = (B(2) - A(2))/(B(1) - A(1))
SlopCD = (D(2) - C(2))/(D(1) - C(1))
SlopBC = (C(2) - B(2))/(C(1) - B(1))
SlopAD = (D(2) - A(2))/(D(1) - A(1))

ehParalelogramo = false;
if(SlopAB == SlopCD && SlopBC == SlopAD)
    ehParalelogramo = true
endif
if(SlopAB == SlopBC && SlopAD == SlopCD)
    ehParalelogramo = true
endif

ehRetangulo = false;
if ((SlopAB * SlopAD == -1) && ehParalelogramo == true)
    ehRetangulo = true
endif


endfunction

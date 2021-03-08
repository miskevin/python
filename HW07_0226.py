#HW07(挑戰題)
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

for height in range(-3,4,1):
    for a in range(abs(height)):
        print(" ",end='')
    for b in range(2*(4-abs(height))-1):
        print("*",end='')
    print()

    
    
    
#teacher sol:
for i in range(1,5):
    print(' '*(4-i)+'*'*(2*i-1))
    
for i in range(3,0,-1):
    print(' '*(4-i)+'*'*(2*i-1))

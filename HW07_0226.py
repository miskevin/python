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

    
    
#other student sol:use center(var)
s = '*'
for i in range(1,8,2):
    print((s*i).center(7))
for i in range(5,0,-2):
    print((s*i).center(7))

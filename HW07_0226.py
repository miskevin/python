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

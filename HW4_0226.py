
#【program】
level = int(input("make triangle:"))
for i in range(1,level):
    for a in range(1,i+1):
        print (a, end='')
    print()
print("finish")

#【result】
#make triangle:5
#1
#12
#123
#1234
#finish

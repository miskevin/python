#【Program】
number = int(input("please enter the times:"))
add = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)
        add += i
print("The even number's total is", add)

#【Result】
#please enter the times:10
#2
#4
#6
#8
#10
#the even sum is 30

#2.輸入迴圈次數，判斷哪些數值是奇數?那些是偶數?

#【Program】
number = int(input("please enter the times:"))
for i in range(1, number +1):
    if i%2 == 0:
        print(i,"is even!")
    else:
        print(i,"is odd!")

#【Result】
#please enter the times:10
#1 is the odd!
#2 is the even!
#3 is the odd!
#4 is the even!
#5 is the odd!
#6 is the even!
#7 is the odd!
#8 is the even!
#9 is the odd!
#10 is the even!

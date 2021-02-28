#HW06
#由使用者輸入數值，請透過FOR將1~該數值
#做加總，最後印出總和

#【program】
num = int(input("please enter the value to sum:"))
total = 0
for add in range(1,num+1):
    total += add
    print(total)

#【result】
#please enter the value to sum:10
#1
#3
#6
#10
#15
##21
#28
#36
#45
#55

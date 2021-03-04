#【牛刀小試】
#最大值100
#最小值0
#如果答案80
#輸入65，顯示"請輸入66~100"的直
#輸入95，顯示"請輸入66~94"的直

#【program】
import random

mx=101
mn=0
count = 0
ans = random.randint(1, 100)
guess = 0
while ans != guess:
    guess = int(input("Guess number (0 to 100):"))
    if ans > guess:
        mn = guess
        print("enter the number between",mn+1,"to",mx-1)
    if ans < guess:
        mx = guess
        print("enter the number between",mn+1,"to",mx-1)
    count += 1
print ("you got it, guess",count,"times!")

#【result】
#Guess number (0 to 100):50
#enter the number between 51 to 100

#Guess number (0 to 100):75
#enter the number between 51 to 74

#Guess number (0 to 100):62
#enter the number between 63 to 74

#Guess number (0 to 100):69
#enter the number between 63 to 68

#Guess number (0 to 100):65
#enter the number between 66 to 68

#Guess number (0 to 100):67
#enter the number between 68 to 68

#Guess number (0 to 100):68
#you got it, guess 7 times!


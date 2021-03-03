#【牛刀小試】
#最大值100
#最小值0
#如果答案80
#輸入65，顯示"請輸入66~100"的直
#輸入95，顯示"請輸入66~94"的直

#【program】
import random

mx=100
mn=0
count = 0
ans = random.randint(mn, mx)
guess = 0
while ans != guess:
    print(ans)
    guess = int(input("Guess number (0 to 100):"))
    if ans > guess:
        mn = guess
        print("enter the number between",mn,"to",mx)
    if ans < guess:
        mx = guess
        print("enter the number between",mn,"to",mx)
    count += 1
print ("you got it, guess",count,"times!")

#【result】
#Guess number (0 to 100):50
#enter the number between 0 to 50
#Guess number (0 to 100):30
#enter the number between 0 to 30
#Guess number (0 to 100):20
#enter the number between 0 to 20
#Guess number (0 to 100):10
#enter the number between 0 to 10
#Guess number (0 to 100):1
#enter the number between 1 to 10
#Guess number (0 to 100):6
#enter the number between 1 to 6
#Guess number (0 to 100):2
#enter the number between 2 to 6
#Guess number (0 to 100):5
#enter the number between 2 to 5
#Guess number (0 to 100):4
#enter the number between 2 to 4
#Guess number (0 to 100):3
#you got it, guess 10 times!


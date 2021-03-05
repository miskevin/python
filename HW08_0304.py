#魔王題
#開始寫卡在輪詢比對 行16~18
#參考網路上作法，花很多時間處理字串比對，不愧是魔王題，過去有用WEB寫過

import random
#Gen 4 number of string and
arr=random.sample('0123456789', 4)
print ("Generator number :", arr)

flag = 1    #while finish this game in 4A
while flag:
    #enter 4 guess numbers
    GN = input("Guess 4 numbers by different number:")
    
    #check same position and number in list(A)
    A = 0
    for i in range(4):
        if(arr[i] == GN[i]):
            A += 1
            
    #check diffent position and same number in list(B)
    B = 0
    p1 = 0   #compair pattern 1 and 2
    while p1 < 4:
        p2 = 0
        while p2 < 4:
            if p1 == p2:   #avoid myself
                p2 += 1
                continue
            if(arr[p1] == GN[p2]):
                B += 1
            p2 += 1
        p1 += 1
    print("Result:", A,"A", B,"B", sep='')
    #check all number is correct!
    if A == 4:
        flag = 0
        print("You got it!")

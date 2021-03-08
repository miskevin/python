#1~49之間亂數曲六個不重複，並印出
#順便排序
import random
group=[]
for i in range(1,50):
    group.append(i)
arr=random.sample(group, 6)
print(arr)

for j in range(len(arr)-1):
    for k in range(len(arr)-1):
        if arr[k] > arr[k+1]:
            arr[k], arr[k+1] = arr[k+1],arr[k]
print(arr)

#result
#[41, 36, 13, 43, 23, 27]
#[13, 23, 27, 36, 41, 43]

#[9, 30, 44, 18, 40, 3]
#[3, 9, 18, 30, 40, 44]

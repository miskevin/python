#氣泡排序法(bubble sort)

nb = list()
while len(nb) < 5:
    num = int(input("please enter a number:"))
    nb.append(num)
    print("the contend of list",nb)
print("bubble sort!")

for j in range(len(nb)-1):
    for i in range(len(nb)-1):
        if nb[i] > nb[i+1]:
            nb[i], nb[i+1] = nb[i+1],nb[i]
print(nb)


#please enter a number:5
#the contend of list [5]

#please enter a number:1
#the contend of list [5, 1]

#please enter a number:4
#the contend of list [5, 1, 4]

#please enter a number:2
#the contend of list [5, 1, 4, 2]

#please enter a number:8
#the contend of list [5, 1, 4, 2, 8]
#bubble sort!
#[1, 2, 4, 5, 8]



#teachere by teacher:
nb = list()
while len(nb) < 6:
    num = int(input("please enter a number:"))
    nb.append(num)
    print("the contend of list",nb)

a = len(nb)
for k in range(a-1):
    for x in range(a-k-1):
        if nb[x] > nb[x+1]:
            nb[x], nb[x+1] = nb[x+1],nb[x]
print("bubble sort twice!",end='')
print(nb)

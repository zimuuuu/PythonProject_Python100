num=0
list=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                num+=1
                list.append([i,j,k]) #or print(i,j,k)
print(num,list)
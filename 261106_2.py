a=int(input("请输入净利润："))
level=[1000000,600000,400000,200000,100000,0]
per=[0.01,0.015,0.03,0.05,0.075,0.1]
total=0
for i in range(0,6):
    if a>level[i]:
       total+=(a-level[i])*per[i]
       a=level[i]
print(f"应发放的奖金总数：{total}元")
N,C=map(int,input().split())
num = list(map(int,input().split()))
cnt={}

for n in num:
    if n not in cnt:
        cnt[n]=1
    else:
        cnt[n]+=1

numList=[]
for number in cnt.keys():
    numList.append((cnt[number],number))

numList.sort(key=lambda list: (-list[0],num.index(list[1])))
print(*numList)
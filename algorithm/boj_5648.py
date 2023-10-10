n, *list = input().split()

while len(list) < int(n):
    list+=input().split()

list = [int(i[::-1]) for i in list]
list.sort()

# for j in range(len(list)):
#     print(list[i])
print(*list, sep='\n')
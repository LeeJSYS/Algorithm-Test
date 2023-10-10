S=input().rstrip()

list = [S[i:] for i in range(len(S))]
list.sort()

print(*list,sep='\n')

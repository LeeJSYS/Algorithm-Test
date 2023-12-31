# def find_parent(parent,x):
#     if parent[x]!=x:
#         return find_parent(parent,parent[x])
#     return x
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
    

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a > b:
        parent[a]=b
    else:
        parent[b]=a
# v, e : node수, 연산수
v, e = map(int,input().split())
parent = [i for i in range(v+1)]
cycle=False

for _ in range(e):
    a, b = map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)

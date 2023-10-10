# B=[b1,b2,b3,b4,b5,b6,...,bn]
# bk>=a인 k?

# def binary_search(a,B,start,end):
#     result=-1
#     while start <= end:
#         mid = (start + end)//2
#         if B[mid]<a:
#             start = mid + 1
#             result= mid
#         else:
#             end = mid - 1
#     return result


# T=int(input())
# for _ in range(T):
#     N, M = map(int,input().split())
#     A=list(map(int,input().split()))
#     B=list(map(int,input().split()))
#     A.sort()
#     B.sort()
#     cnt=0
#     for a in A:
#         cnt+=binary_search(a,B,0,len(B)-1)
#     print(cnt)
        
def binarySearch(data, list):
    start=0
    end=len(list)-1
    result=-1
    while start <= end:
        mid = (start+end)//2
        if(data <= list[mid]):
            end = mid -1
        else: 
            start = mid+1
            result = mid
    return result

test_case=int(input())
for _ in range(test_case):
    A, B = map(int,input().split())
    A_List=list(map(int,input().split()))
    B_List=list(map(int,input().split()))
    A_List.sort()
    B_List.sort()
    cnt=0
    for a in A_List:
        cnt+=(binarySearch(a,B_List)+1)
            
    print(cnt)


array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(start,end,array):
    if start >= end:
        return 
    
    pivot = start
    left = start+1
    right = end
    while left <= right:
        if array[left]<=pivot:
            left+=1
            continue
        if array[right]>=pivot:
            right-=1
            continue
        
        array[left],array[right] = array[right],array[left]

    array[right],array[pivot] = array[right],array[pivot]
    quick_sort(start,right,array)
    quick_sort(right+1,end,array)

quick_sort(0,len(array)-1,array)

def moveval(index,newindex,arr):
    oldv = arr[index]
    oldv2 = arr[newindex]
    
    for i in range(len(arr)):
        if i == newindex:
            arr[i] = int(arr[i])
            arr[i] = oldv
        if i == index:
            arr[i] = oldv2
    
    return arr


arr = [0,1,2,3,4,5,6,7]
lst = []

arr = moveval(1,7,arr)
lst.append(1)
lst.append(7)
print(arr)
arr = moveval(lst[1],lst[0],arr)
print(arr)
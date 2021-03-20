def insertShiftArray(arr, val):
    if val == "":
        print('no value entered')
    mid = len(arr)//2
    if len(arr)%2 == 0:
        mid -=1

    new_list = []
    for i in range(len(arr)):
        new_list.append(arr[i])
        if i == mid:
            new_list.append(val)
    return new_list

def insertShiftArray2(arr, val):
    if val == "":
        print('no value entered')
    mid = len(arr)//2
    if len(arr)%2 !=0:
        mid+=1
    arr.insert(mid, val)
    return arr

def insertShiftArray3(arr, val):
    if val == "":
        print('no value entered')
    mid = len(arr)// 2

    new_list = arr
    for i in range(len(arr)):
        if i < mid:
            new_list[i]=arr[i]
        elif i == mid:
            new_list[i]=val
        if i > mid:
            new_list[i]=arr[i-1]
    return new_list

def removeAndShiftArray(arr):
    mid = len(arr)//2
    new_list = []
    for i in range(len(arr)):
        if i != mid:
            new_list.append(arr[i])
    return new_list

def removeAndShiftArray2(arr):
    mid=len(arr)//2
    arr.pop(mid)
    return arr
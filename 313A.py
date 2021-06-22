x = int(input())

arr = list(x)

if x >= 0:
    arr = arr
else:
    if arr[len(arr)-1] >= arr[len(arr)-2]:
        arr = arr[:len(arr-1)]
    else:
        arr = arr[:len(arr)-2] + arr[len(arr)-1:]


print(arr)
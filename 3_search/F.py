def lower_bound(arr, x, n):
    left = -1
    right = n

    while left < right - 1:
        mid = (left + right) // 2
        if x <= arr[mid]:
            right = mid
        else:
            left = mid
    
    return right


n = int(input())
answer = n

left = 0
right = n + 1

while answer:
    mid = (left + right) // 2
    print(mid)

    answer = int(input())
    if answer == -1:
        right = mid + 1
    elif answer == 1:
        left = mid
    else:
        break

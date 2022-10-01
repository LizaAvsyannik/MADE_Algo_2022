def is_possible(timbers, width, k):
    for t in timbers:
        k -= t // width
    return k <= 0
    

def max_possible_width(timbers, left, right, k):
    while left < right - 1:
        mid = (left + right) // 2
        if is_possible(timbers, mid, k):
            left = mid
        else: 
            right = mid
    return left
    

n, k = map(int, input().split())
    
max_timber_length = 0
timbers = []
for i in range(n):
    timbers.append(int(input()))
    if timbers[i] > max_timber_length:
        max_timber_length = timbers[i]
    
print(max_possible_width(timbers, 0, max_timber_length + 1, k))
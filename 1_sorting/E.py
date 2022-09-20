import sys
from collections import defaultdict
from random import choice

SYMBOLS_DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50}

def roman_to_arabic(roman_str):
    arabic_n = 0
    roman_length = len(roman_str)

    i = 0
    while (i < roman_length):
        a = SYMBOLS_DICT[roman_str[i]]
        if i + 1 >= roman_length:
            arabic_n += a
        else:
            b = SYMBOLS_DICT[roman_str[i + 1]]
            if a >= b:
                arabic_n += a
            else:
                arabic_n += (b - a)
                i += 1
        i += 1
    return arabic_n

def split(arr, l, r, x):
    if r - l <= 1:
        if arr[r] < arr[l]:
            arr[r], arr[l] = arr[l], arr[r]
        return l, r 
        
    m2 = l
    while (m2 <= r):
        if arr[m2] < x:
            arr[m2], arr[l] = arr[l], arr[m2]
            m2 += 1
            l += 1
        elif arr[m2] == x:
            m2 += 1
        else:
            arr[m2], arr[r] = arr[r], arr[m2]
            r -= 1
    return l - 1, m2
        
def quick_sort(arr, l, r):
    if r <= l:
        return
    
    x = choice(arr[l:r + 1])
    m1, m2 = split(arr, l, r, x)
   
    quick_sort(arr, l, m1)
    quick_sort(arr, m2, r)
    
inp = sys.stdin.readlines()
kings = [k.split() for k in inp[1:]]

kings_dict = defaultdict(list)
numbers_dict = defaultdict()
for k in kings:
    arabic_n = roman_to_arabic(k[1])
    kings_dict[k[0]].append(arabic_n )
    numbers_dict[arabic_n] = k[1]

# sort king's names
kings_names = list(kings_dict.keys())
quick_sort(kings_names, 0, len(kings_names) - 1)

# sort numbers for each name
for k, v in kings_dict.items():
    quick_sort(v, 0, len(v) - 1)

for name in kings_names:
    for n in kings_dict[name]:
        print(f'{name} {numbers_dict[n]}')

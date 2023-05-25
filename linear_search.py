import pandas as pd
import time
import random

world_data = pd.read_csv('/Users/namanh.ngco/Documents/Algorithm/Data /World_maps/worldcities.csv')
world_data.shape



def linear_search(text_input):
    for i in world_data['country']:
        if i == text_input:
            return True


def merge_sort(unsorted_list):
    a = list(unsorted_list)
    if len(a) > 1:
        mid = len(a)//2

        L = a[:mid]
        R = a[mid:]

        L = merge_sort(L)

        R = merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            a[k] = L[i]
            k += 1
            i += 1
        
        while j < len(R):
            a[k] = R[j]
            k += 1
            j += 1
    return a

def binary_search(sorted_list, text_input):
    
    mid = len(sorted_list)//2

    L = sorted_list[mid:]
    R = sorted_list[:mid]
    if text_input == sorted_list[mid]:
        return sorted_list.index(text_input)
    elif text_input < sorted_list[mid]:
        return binary_search(R, text_input)
    else:
        return binary_search(L, text_input)



y = merge_sort(world_data['country'])

s1 = 0
s2 = 0

for i in range(100):
    
    text_input = random.choice(world_data['country'])

    t1 = time.time()
    linear_search(text_input)
    t2 = time.time()

    s1 = s1 + t2 - t1

    t3 = time.time()
    binary_search(y, text_input)
    t4 = time.time()
    s2 = s2 + t4 - t3 

print(s1/100)
print(s2/100)
print(s2/s1)


 
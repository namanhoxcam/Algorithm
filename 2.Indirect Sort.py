import random

t  = int(input())

def main(n):
    i,j,k  = random.sample([range(n), 3])


for i in range(t):
    n = int(input())
    if n >= 3:
        list_number = []
        times = 0
        while times < n:
            input_number = int(input())
            if input_number not in list_number:
                list_number.append(input_number)
                n += 1
            else:
                continue
        print(list_number)
    
    

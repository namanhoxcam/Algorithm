tc = int(input())
for tc in range(1, tc + 1):
    a = int(input())
    b = int(input())
    c = int(input())
    m = abs(b-c) + (c-1) - (a-1)
    if m > 0:
        print("1")
    elif m < 0:
        print("2")
    else:
        print("3")
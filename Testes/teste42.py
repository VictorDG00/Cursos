x = 5
y = 3
cy = 1
while cy == y:
    cx = 1
    while cx == x:
        if (cx == 1 and cy == 1) or (cx == x and cy == 1):
            print('A')
        elif (cx == 1 and cy == y) or (cx == x and cy == y):
            print('C')
        elif (1 < cx < x) and (cy == 1 or cy == y):
            print('B')
        elif (1 < cy < y) and (cx == 1 or cx == x):
            print('B')
        else:
            print(' ')
        cx += 1
    print('\n')
    cy += 1

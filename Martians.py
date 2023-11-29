import random
b = 0
z = 0
while b != 3:
    a = []
    b = 0
    for i in range(0,7):
        n = random.randint(0,1)
        a.append(n)
        if n == 1:
            b += 1
            if b == 3:
                for c in range(i,6):
                    a.append(0)
                break
print('Please, print 3 coordinates separates by spaces.')
while z == 0:
    x = [int(s) for s in input().split()]
    if len(x) != 3:
        print('Error, wrong coordinates!')
        exit()
    else:
        for i in range(0,3):
            if x[i] < 0 or x[i] > 6:
                print('Error, wrong coordinates!')
                exit()
        if a[x[0]] == 1 and a[x[1]] == 1 and a[x[2]] == 1:
            print('Congratulations, you got all 3 boxes right!')
            z = 1
        elif a[x[0]] == 1 and a[x[1]] == 1 and a[x[2]] != 1:
            print('Two coordinates are right! \n Try again!')
        elif a[x[0]] == 1 and a[x[1]] != 1 and a[x[2]] == 1:
            print('Two coordinates are right! \n Try again!')
        elif a[x[0]] != 1 and a[x[1]] == 1 and a[x[2]] == 1:
            print('Two coordinates are right! \n Try again!')
        elif a[x[0]] != 1 and a[x[1]] != 1 and a[x[2]] == 1:
            print('One coordinate is right! \n Try again!')
        elif a[x[0]] == 1 and a[x[1]] != 1 and a[x[2]] != 1:
            print('One coordinate is right! \n Try again!')
        elif a[x[0]] != 1 and a[x[1]] == 1 and a[x[2]] != 1:
            print('One coordinate is right! \n Try again!')
        else:
            print('Wrong coordinates, try again!')

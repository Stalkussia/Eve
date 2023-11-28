import random
b = 0
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
print(a)
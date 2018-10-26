# Η συνάρτηση 
def f(x):
    return -1/6 * (x - 1) * (x - 2) * (x + 2) * (x - 4)

while True:
    x1, x2, n = input().split(',')
    x1, x2, n = float(x1), float(x2), int(n)
    if n == 0:
        break
    
    #Ο τύπος είναι I = (dx / 2 ) * (f0 + 2f1 + .. + fn)
    #Όπου dx = (x2 - x1) / 2 , fi = f(x1 + i * dx)

    dx = (x2 - x1) / n 
    res = f(x1) + f(x2)

    for i in range(1, n):
        x1 += dx
        res += 2 * f(x1)
    
    res *= (dx / 2)

    print('{:.3f}'.format(res))
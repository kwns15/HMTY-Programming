a,b,c = input().split(',')
sides = sorted([float(a), float(b), float(c)], reverse = True)
a, b, c = sides
print('{:.2f} {:.2f} {:.2f}'.format(a, b, c))
if a < b + c:
    P = a + b + c
    t = P / 2
    area = (t * (t - a) * (t - b) * (t - c)) ** 0.5
    print('Perimeter: {:.2f}'.format(P))
    print('Area: {:.2f}'.format(area))
    if a == b and b == c:
        print('Equilateral triangle')
    elif a ==b or b == c:
        print('Isosceles triangle')
    if a ** 2 == b ** 2 + c ** 2:
        print('Right triangle')
    elif a ** 2 > b ** 2 + c ** 2:
        print('Obtuse triangle')
    else :
        print('Acute triangle')
else:
    print('Not a triangle')




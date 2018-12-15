def isMagicSquare(data):

    numbers = [int(n) for n in data.split(',')]
    
    a = len(numbers) ** 0.5
    
    if int(a) != a : return -1 # not a square
    
    a = int(a)
    sums = {}
    mainDiagonal = 0
    secondaryDiagonal = 0

    for i in range(a):
        row = sum(numbers[i * a: (i + 1) * a])
        column = sum(numbers[i ::a])

        mainDiagonal += numbers[i * a + i]
        secondaryDiagonal += numbers[(i + 1) * a - 1 - i]

        if row not in sums:
            sums[row] = True
        if column not in sums:
            sums[column] = True

    if mainDiagonal not in sums:
        sums[mainDiagonal] = True
    if secondaryDiagonal not in sums:
        sums[secondaryDiagonal] = True

    if len(sums) == 1 : 
        temp = {}
        for n in numbers:
            if n not in temp:
                temp[n] = 1
            else:
                temp[n] += 1
        for c in temp.values():
            if c > 1: return len(sums) # same number appearing twice or more
        
        return 0

    return len(sums)


while True:

    data = input()

    if data == "end" : break

    print(isMagicSquare(data))
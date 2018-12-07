operations = {'+' : lambda a, b: a+b, '-' : lambda a, b: a-b, '*' : lambda a, b: a*b,
              '/' : lambda a, b: a//b}

systems = {'(2)' : lambda a : str(bin(a))[2:], '(8)' : lambda a : str(oct(a))[2:], '(10)' : lambda a : str(a), '(16)' : lambda a : str(hex(a))[2:]}

def parseNumber(num):
    
    data = num.split('(')
    data[1] = int(data[1][:-1])
    
    return int(data[0], data[1])

def parse(data):
    data = data.split('-->')
    numbers = data[0]
    result = data[1]
    
    for oper in '+-*/':
        if oper in numbers:
            numbers = numbers.split(oper)
            break
    
    numbers = [parseNumber(n) for n in numbers]

    resultnum = operations[oper](numbers[0], numbers[1])

    if resultnum == 0 : return '0'

    resultnum = systems[result](resultnum)
    
    if resultnum[0] != '0' : resultnum = '0' + resultnum
    
    return resultnum
while True:

    data = input()

    if data == 'END' or data == 'end': break
    
    print(parse(data))

    

    
    
data = input()

if len(data) == 1:
    if data.isdigit():
        print('The Unicode code of number {} is {}'.format(data, ord(data)))
    elif data.isalpha():
        print('The Unicode code of character {} is {}'.format(data, ord(data)))
    else:
        print('Wrong!')
else:
    print('Wrong!')
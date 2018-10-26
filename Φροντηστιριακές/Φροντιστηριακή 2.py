while True:
    data = input()
    if data == 'END' or data == 'end':
        break
    counters = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
                '7': 0, '8': 0, '9': 0, 'chars': 0}
    for c in data:
        if c in counters:
            counters[c] += 1
        else:
            counters['chars'] += 1
    for key in counters:
        if counters[key] > 9:
            counters[key] = '*'
    out = ''
    for v in counters.values():
        out += str(v)
    print(out)

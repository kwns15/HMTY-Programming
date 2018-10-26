data = input()
scale = data[-1] # Το σύμβολο που δώθηκε
value = float(data[:-1]) # Ο αριθμός

if scale in 'CFK' and value <=200 and value >= -100:
    if scale == 'C':
        tF = value * 1.8 + 32
        tK = value + 273.15
        print('{} {:.2f}F {:.2f}K'.format(data, tF, tK)) #Παρατηρείστε στο παράδειγμα η πρώτη έξοδος είναι ολόιδια με την είσοδο
    elif scale == 'F':
        tC = (value - 32) / 1.8
        tK = tC + 273.15
        print('{} {:.2f}C {:.2f}K'.format(data, tC, tK))
    else:
        tC = value - 273.15
        tF = tC * 1.8 + 32
        print('{} {:.2f}C {:.2f}f'.format(data, tC, tF))
else:
    print('Λάθος')
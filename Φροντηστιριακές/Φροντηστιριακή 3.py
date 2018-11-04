
def evaluate(num):

    # επιστρέφουμε True για κάθε δεκτή είσοδο
    # επιστρέφουμε False για κάθε μη δεκτή είσοδο

    splitChar = None
    cardNum = []

    i = 0

    for c in num:
        if not c.isdigit():
            #έλεγχος αν ο χαρακτήρας διαχωρισμού ειναι δεκτός και σε σωστή θέση
            if c in '- ' and i % 5 == 4:
                if splitChar == None:
                    splitChar = c
                elif c != splitChar:
                    return False
            else:
                return False
        else:
            # μετατροπή του χαρεκτήρα σε ακέραιο
            cardNum.append(int(c))
        i += 1

    # έλεγχος αν τα ψηφία του αριθμού είναι 16
    if len(cardNum) != 16:
        return False


    # έλεγχος πρώτου ψηφίου 
    if cardNum[0] < 4 or cardNum[0] > 7:
        return False

    # διπλασιαμός των ψηφίων σε περιττές θέσεις και μερικό άυροισμα τους
    cardSum = 0 
    for n in cardNum[::2]:
        n *= 2
        while n > 9:
            if n // 10 == 1:
                n = 1 + n % 10
        cardSum += n
    # άθροισμα όλωμ των "νέων" ψηφίων
    cardSum += sum(cardNum[1::2])

    # έλεγχος διαραιτότητας του αποτελέσματος με το 10
    return cardSum % 10 == 0

while True:
    data = input()

    if data == 'END' or data == 'end':
        break
    
    # κλήση της συνάρτησης και εκτύπωση του αποτελέσματος
    
    print(evaluate(data))



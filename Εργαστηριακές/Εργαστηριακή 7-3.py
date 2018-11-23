#setting up

notes = ['La', 'La#', 'Si', 'Do', 'Do#',
         'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#']


allnotes = []
d = 2 ** (2/12)

freq = 440

note = len(notes) - 1

while freq >= 20:
    freq = int(freq / d)
    allnotes.append([notes[note], freq])
    note -= 1
    if note < 0:
        note = len(notes) - 1

freq = 440
note = 0

while freq <= 20000:
    allnotes.append([notes[note], freq])
    freq = int(freq * d)
    note += 1
    if note == len(notes):
        note = 0

allnotes.sort(key = lambda i: i[1])

def closestNote(f):
    for i, note in enumerate(allnotes):
        if f < note[1]:break

    if abs(f - allnotes[i-1][1]) < abs(f - allnotes[i][1]):
        return allnotes[i-1][0]
    else:
        return allnotes[i][0]

#Main Loop

while True:
    data = int(input())

    if data == 0:
        break
    print(closestNote(data))
    

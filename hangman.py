from random import choice
from words import word_list
#KarsonLawson on twitter
worda = choice(word_list)
word = list(worda)

attemps = 0
maxattemps = 5
hidden = []
for boom in word:
    hidden.append('_')

gameover = False
while not gameover:
    print(f'the word isssss: {" ".join(hidden)}' )
    print(f'you have {maxattemps - attemps} attemps left')
    print(' -------')
    print(' |   |')
    print(' |   ' + ('0' if attemps > 0 else ''))
    print(' |  ' + ('/|\\' if attemps > 1  else ''))
    print(' |   ' + ('|' if attemps > 2 else ''))
    print(' |   ' + ('/\\' if attemps > 3 else ''))
    print(' |_________')
    print('         ')
    guess = input('guess a letter dood:')

    if guess in word:
        print(f'yee {guess} was in da word')
        for i in range(len(word)):
            letta = word[i]
            if guess == letta:
                hidden[i] = word[i]
                word[i] = '_'
    else:
        print(f'no boomer {guess} is not in da word try again')
        attemps += 1

    if all('_' == char for char in word):
        print(f'congrats bro u got it the word was {worda}')
        gameover = True

    if attemps >= maxattemps:
        print(f'you lost boomer it was {worda}')
        gameover = True

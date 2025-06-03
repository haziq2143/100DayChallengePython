import random
import hangman 
import words

word = random.choice(words.wordList)
print(word)
letter = []
ges = []
for i in word:
    letter.append(i)
for x in word:
    ges.append('_')

nyawa = 0
while len(letter) != 0:
    placeHold = ''
    guess = input("Masukkan Huruf: ").lower()
    
    for i in range(len(word)):       
        if guess == word[i]:
            ges[i] = guess
            letter.remove(guess)
            
    if guess not in word:
        nyawa+=1
        print(hangman.hangman[nyawa])
    
    for i in ges:
        placeHold += i
    
    if "_" not in placeHold :
        print("Menang")
        break
    elif nyawa == 6:
        print("Anda Kalah")
        break
    print(placeHold)





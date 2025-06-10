class Flashcard() :
    def __init__(self, word , meaning) :
        self.word = word 
        self.meaning = meaning 

    def __str__(self) :
        return self.word+ '('+self.meaning+')'
     

flash = []
print('welcome to the flashcard application')

while (True) :
    word = input('enter the name you want to add in flashcard == ')
    meaning = input('enter the meaning of word == ')

    flash.append(Flashcard(word,meaning))
    option = int(input('if you want add another word to flashcard ... enter 0 >> \t\n for exit ... enter 1 >> '))

    if option == 1 :
       print('thankyou') 
       break

print('\t your flashcard')
for i in flash :
    print('>>', i)
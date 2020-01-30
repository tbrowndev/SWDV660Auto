def MilitarySpelling(word):
    militaryAlphabetDictionary = {'a':"Alpha",'b':"Bravo",'c':"Charlie",'d':"Delta",'e':"Echo",'f':"Foxtrot",'g':"Golf",'h':"Hotel",'i':"India",'j':"Juliet",'k':"Kilo",'l':"Lima",'m':"Mike",'n':"November",'o':"Oscar",'p':"Papa",'q':"Quebec",'r':"Romeo",'s':"Sierra",'t':"Tango",'u':"Uniform",'v':"Vistor",'w':"Whiskey",'x':"X-Ray",'y':"Yankee",'z':"Zulu"}
    wordSpellingMilitary = ""
    for char in word:
        wordSpellingMilitary = wordSpellingMilitary + militaryAlphabetDictionary.get(char.lower(), char.lower()) + " - "
    return wordSpellingMilitary[0:len(wordSpellingMilitary)-3]

def Main():
    word = input("Enter a Word (No SPACES): ")
    print("Military Spelling of your word:")
    print(MilitarySpelling(word))

Main()

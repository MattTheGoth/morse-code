# morse_eng.py

# A program to convert a morse code input into English

# Coded by Matthew Plummer September 2016

# Version 1.2


morse2eng = {'-...': 'b', '-.-.': 'c', '.----.': "'", '.--.': 'p', '--.-': 'q',
    '..--.-': '_', '----.': '9', '--': 'm', '-.-': 'k', '..-.': 'f', 
    '.---': 'j', '-....-': '-', '...-': 'v', '--...': '7', '.-..': 'l', 
    '-.': 'n', '---..': '8', '.': 'e', '-..-': 'x', '-..-.': '/', '.----': '1',
    '.--': 'w', '.-..-.': '"', '--..--': ',', '.--.-.': '@', '--.': 'g', 
    '-...-': '=', '.-.-.-': '.', '...--': '3', '.....': '5', '....': 'h', 
    '..--..': '?', '....-': '4', '.-.-.': '+', '-.-.-.': ';', '--..': 'z', 
    '-----': '0', '.-.': 'r', '..---': '2', '---': 'o', '..-': 'u', '..': 'i', 
    '-': 't', '-.-.--': '!', '-..': 'd', '-.--': 'y', '-....': '6', 
    '---...': ':', '.-': 'a', '...': 's', '/': ' '}



print("Type 'quit' to quit.")

while True:
    morse = input('What do you want to translate from morse code? ')
    if morse == 'quit':
        break
    else:
        characters = morse.split()
        out = []
        for c in characters:
            e = morse2eng[c]
            out.append(e)
            s = ''.join(out)
        print(s)
        


# morse_code.py

# A program to translate English input into morse code and output the contents
# to a file called morse_out.txt in the same directory.

# Coded by Matthew Plummer September 2016

# Version 1.2

filename = 'morse_out.txt'
f = open(filename, 'a')

morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-.'}



print("Type 'quit' to quit.")

while True:
    text = input('What do you want to convert to morse code?: ')
    if text.lower() == 'quit':
        break
    else:
        out = []
        characters = list(text.lower())
        for c in characters:
            if c == ' ':
                out.append('/ ')
            else:
                m = morse[c]
                out.append(m)
                out.append(' ')
        s = ''.join(out)
        f.write('\n' + text + '\n')
        f.write(s)
        print(text, '\n', s)
f.close()
                

# morse_code.py

# A program to translate English input into morse code and output the contents
# to a file called morse_out.txt in the same directory.

# Coded by Matthew Plummer September 2016

# Version 1.2

filename = 'morse_out.txt'
f = open(filename, 'a')

eng_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-.'}


morse_eng = {'-...': 'b', '-.-.': 'c', '.----.': "'", '.--.': 'p', '--.-': 'q',
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



def eng2morse():
    """ A function to translate alphanumeric input into morse code."""
    try:
        text = input('What do you want to convert to morse code?: ')
        out = []
        characters = list(text.lower())
        for c in characters:
            if c == ' ':
                out.append('/')
            else:
                m = eng_morse[c]
                out.append(m)
                out.append(' ')
        s = ''.join(out)
        f.write('\n' + text + '\n' + s)
        print(text, '\n', s)
    except KeyError:
        pass

def morse2eng():
    """ A function to translate morse code input into alpha-numeric characters.
        """
    try:
        morse = input('What do you want to translate from morse code? ')
        characters = morse.split()
        out = []
        for c in characters:
            e = morse_eng[c]
            out.append(e)
            s = ''.join(out)
        print(s)
    except KeyError:
        pass
        
#~ def choose_function:
    #~ print("

print("To translate from alpha-numeric to morse code please type 'translate'")
print("\nTo interpret morse code into alpha-numeric characters, "
        "please type 'interpret'")
print("\nType 'quit' to exit.")

while True:
    choice = input()
    if choice == 'quit':
        break
    elif choice == 'translate':
        while True:
            eng2morse()
    elif choice == 'interpret':
        morse2eng()

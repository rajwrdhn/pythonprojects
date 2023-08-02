MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'
                }

def encrypt(message):
    morse_msg = ""
    for letter in message:
        try:
            if letter in MORSE_CODE_DICT.keys():
                morse_msg += MORSE_CODE_DICT[letter] + " "
            else:
                morse_msg = "letter not in morse code!"
                break
        except KeyError:
            morse_msg = "Invalid Key!"

    return morse_msg

def main():
    message = input("Enter the message to be encrypted! \n").upper()
    morse = encrypt(message)
    print(morse)

if __name__== '__main__':
    main()
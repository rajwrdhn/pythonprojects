#Paint Area Calculator
import math
import string

def paint_area_calc(height, width, coverage):

    num_of_cans = height*width/coverage

    print(math.ceil(num_of_cans))

paint_area_calc(height=3,width=7, coverage=5)

def prime_checker(number):
    is_prime = True
    for r in range(2,number):
        if number%r == 0:
            is_prime = False
            print("Not Prime!")
            break
    
    if is_prime:
        print(f"{number} is Prime!")

prime_checker(13)

#caeser cypher

alphabets = list(string.ascii_lowercase)
direction = input("Type encode to encrypt and decode to decrypt!")
text = input("Enter the encryption text: \n").lower()
shift = int(input("Enter the shift number for the encryption!\n"))

def encryption(text, shift):
    new_text = []
    for letter in text:
        letter_position = alphabets.index(letter)
        new_position = letter_position + shift
        if new_position > 25:
            new_position = new_position%25 -1
        new_letter = alphabets[new_position]
        new_text.append(new_letter)
    
    print("".join(new_text))

def decryption(e_text, shift):
    original_text = ""
    for letter in e_text:
        letter_position = alphabets.index(letter)
        new_position = letter_position - shift
        new_letter = alphabets[new_position]
        original_text += new_letter
    
    print(original_text)

encryption(text=text, shift=shift)
decryption("ezqz",shift)
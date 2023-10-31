'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def shift_letter(letter, shift):
    if letter.isspace():
        print(" ")
    elif letter.isalpha() and len(letter) == 1 and letter.isupper():
        Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Index = Alphabet.index(letter)
        shifted = (Index + shift) % 26
        letter_shifted = Alphabet[shifted]
        return letter_shifted
    else:
        raise ValueError("Enter only one capitalized English letter or a space.")

try:
    letter = input("Enter one letter here: ")

    if letter.isalpha():
        shift = int(input("Enter desired number of shifts here: "))
        result = shift_letter(letter, shift)
    else:
        result = " "
    
    print(result)
except ValueError as e:
    print("Input error:", e)
except Exception as e:
    print("An error occurred:", e)
    

#NEXT ITEM

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_message = ""

    for char in message:
        if char.isalpha() and char.isupper():
            char_index = alphabet.index(char)
            shifted_index = (char_index + shift) % 26
            shifted_char = alphabet[shifted_index]
        elif char.isspace():
            shifted_char = " "
        else:
            # Handle non-alphabet characters
            raise ValueError("Enter only uppercase English letters and spaces.")
        shifted_message += shifted_char

    return shifted_message

try:
    message = input("Enter the message (uppercase letters and spaces only): ")
    shift = int(input("Enter the desired number of shifts: "))
    result = caesar_cipher(message, shift)
    print("Shifted message: ", result)
except ValueError as e:
    print("Input error:", e)
except Exception as e:
    print("An error occurred:", e)
    
    #NEXT ITEM

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def shift_by_letter(letter, letter_shift):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter_index = alphabet.index(letter)
        letter_shift_index = alphabet.index(letter_shift)
        shifted_index = (letter_index + letter_shift_index) % 25
        shifted_letter = alphabet[shifted_index]
        return shifted_letter

letter = input("Enter a letter (uppercase or space): ")
letter_shift = input("Enter the shift letter (uppercase or space): ")

if letter.isalpha() and letter.isupper() and letter_shift.isalpha() and letter_shift.isupper():
    result = shift_by_letter(letter, letter_shift)
    print("Shifted letter:", result)

elif letter == " " and letter_shift == " ":
    result = " "
    print(result)
    
    #NEXT ITEM

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def vigenere_cipher(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    # Extend the key to match the length of the message

    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(message)):
        message_char = message[i]
        key_char = key[i]

        # Find the shift value based on the key_char
        shift = alphabet.index(key_char)

        # Shift the message_char by the shift value for encoding
        if message_char.isupper():
            shifted_index = (alphabet.index(message_char) + shift) % 26
            shifted_char = alphabet[shifted_index]
            result += shifted_char
        else:
            result += " "  # Preserve spaces in the message

    return result

# Example usage with user input:
message = input("Enter the message to encode (uppercase letters and spaces): ")
key = input("Enter the key (uppercase letters): ")
encoded_message = vigenere_cipher(message, key)
print("Encoded message:", encoded_message)

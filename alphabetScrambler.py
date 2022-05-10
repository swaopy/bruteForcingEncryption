# scrambled_alphabet_cipher

from microbit import *

# Scrambled alphabet cipher.
def scramble(text, encrypt):
    alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    crypta = "PTQGMKCRSVEXADZBJFOWYNIHLU"
    result = ""
    
    if encrypt is False:
        temp = alpha
        alpha = crypta
        crypta = temp

    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]

    return result

# The script starts executing statements from here.

sleep(1000)

print("Set your keyboard to CAPS LOCK.")
print()

while True:
    text = input("Enter a CAPS LOCK string: ")
    
    result = scramble(text, True)

    print("scrambled result =", result)
    
    result =  scramble(result, False)
    
    print("unscrambled result =", result)
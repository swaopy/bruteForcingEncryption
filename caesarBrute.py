# radio_receive_images_caesar_brute_force.py

from microbit import *
import radio

''' Function converts plaintext to ciphertext using key '''

def caesar(key, word):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in word:
        
        letter = letter.upper()
        index = ( alpha.find(letter) + key ) % 26
        result = result + alpha[index]
    
    return result

''' Script starts from here... '''

radio.on()
radio.config(channel=7)

sleep(1000)

while True:
    
    packet = radio.receive()

    if packet:
        print("Receive encrypted:", packet)
        # packet = caesar(-3, packet)             # <- comment
        # print("packet:", packet)                # <- comment
        # display.show(getattr(Image, packet))    # <- comment
        for key in range(-1, -26, -1):            # <- add
            result = caesar(key, packet)          # <- add
            print("key:", key, "result:", result) # <- add
            sleep(200)                            # <- add
        print()                                   # <- add
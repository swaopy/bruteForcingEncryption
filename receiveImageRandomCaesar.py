# radio_receive_images_caesar_brute_force_try_this.py

from microbit import *
import radio

''' Function converts plaintext to ciphertext using key '''

def ascii_shift(key, text):                 # <- change (try this)
    result = ""                             # <- chante (try this)
    for letter in text:                     # <- change (try this)
        ascii = ( ord(letter) + key - 32 ) % 94 + 32  # <- change (try this)
        result = result + chr(ascii)        # <- change (try this)
    return result                           # <- change (try this)

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
        # for key in range(-1, -26, -1):          # <- add
        for key in range(-1, -94, -1):            # <- change (try this)
            # result = caesar(key, packet)        # <- add
            result = ascii_shift(key, packet)     # <- change (try this)
            print("key:", key, "result:", result) # <- add
            sleep(200)                            # <- add
        print()                                   # <- add
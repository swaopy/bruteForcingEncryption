# radio_send_images_caesar_key_unknown_try_this.py

from microbit import *
import radio
import random                               # <- add

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

string_list = ["HAPPY", "SAD", "ANGRY"]

# key = random.randint(1, 25)               # <- add
key = random.randint(1, 93)                 # <- change (try this)

while True:
    
    for packet in string_list:
        print("packet:", packet)
        display.show(getattr(Image, packet))
        
        # packet = caesar(3, packet)             # <- change (before)
        # packet = caesar(key, packet)           # <- change (after)
        packet = ascii_shift(key, packet)        # <- change (try this)
        
        
        print("Send encrypted:", packet)
        radio.send(packet)
        # sleep(2500)                       # <- change (before)
        sleep(6000)                         # <- change (after)
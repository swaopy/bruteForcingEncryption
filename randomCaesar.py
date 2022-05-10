# radio_send_images_caesar_key_unknown.py

from microbit import *
import radio
import random                               # <- add

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

string_list = ["HAPPY", "SAD", "ANGRY"]

key = random.randint(1, 25)                 # <- add

while True:
    
    for packet in string_list:
        print("packet:", packet)
        display.show(getattr(Image, packet))
        
        # packet = caesar(3, packet)        # <- change (before)
        packet = caesar(key, packet)        # <- change (after)
        
        
        print("Send encrypted:", packet)
        radio.send(packet)
        # sleep(2500)                       # <- change (before)
        sleep(6000)                         # <- change (after)
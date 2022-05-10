# decimal_bank_vault_crack.py                 # <- change

from microbit import *
import radio

radio.on()
radio.config(channel=7)

# digits = ['0','1']                          # <- comment (before change)
digits = ['0','1','2','3','4','5']            # <- change

display.show(Image.ARROW_W)

while True:
    if button_a.was_pressed():
        
        display.clear()

        for a in digits:
            for b in digits:
                for c in digits:
                    pin = ''.join([a, b, c])
                    
                    print("pin =", pin)
                    
                    for x in range(3):
                        for y in range(int(pin[x])):
                            display.set_pixel(x, y, 9)

                    response = None
                    while response is None:
                        radio.send(pin)
                        sleep(100)
                        response = radio.receive()
                            
                    print(response)
                    if response == "Access granted.":
                        while True:
                            display.scroll(pin)

                    sleep(4000)
                    display.clear()
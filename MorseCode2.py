import RPi.GPIO as GPIO
from time import sleep

KEY = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setwarnings(False)

pin = 4
dot_time =  0.2 #0.5
dash_time = 0.5 #1
space_time = 1 #3

message = raw_input("Enter message here: ")
 
def toMorse(message):
    message = message.upper()
    encoded_message = " "

    for character in message:
        encoded_message += KEY[character] + " "
    
    return encoded_message

def run():
    encoded_message = toMorse(message)
    print(encoded_message)
    
    for i in range (0,100):
    
        for character in encoded_message:
            if character == ".":
                GPIO.output(pin, True)
                sleep(dot_time)
                GPIO.output(pin, False)
                sleep(dot_time)
            elif character == "-":
                GPIO.output(pin, True)
                sleep(dash_time)
                GPIO.output(pin, False)
                sleep(dash_time)
            elif character == " ":
                sleep(space_time)
run()

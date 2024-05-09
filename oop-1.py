import pyfiglet
import time

def convert_to_ascii(message):
    ascii_message = pyfiglet.figlet_format(message)
    return ascii_message

def send_message(ascii_message):
    print("Sending message...")
    time.sleep(2) 
    print("Message sent successfully!")
    print(ascii_message)

def convert_to_string(ascii_numbers):
    message = ''.join(chr(num) for num in ascii_numbers)
    return message

def main():
    message = convert_to_string([98, 101, 114, 97, 98, 101, 114, 32, 98, 105, 114, 32, 107, 97, 104, 118, 101, 32, 105, 99, 109, 101, 121, 101, 32, 110, 101, 32, 100, 101, 114, 115, 105, 110, 63])
    ascii_message = convert_to_ascii(message)
    send_message(ascii_message)

print(main())
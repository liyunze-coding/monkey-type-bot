import pyautogui as ptg
from PIL import ImageGrab
import cv2
import numpy as np
import string
import pytesseract as ptr
import time
import random
import random
import decimal

'''
Users will have to edit the tuples bbox and bbox2 according to the screen capture

bbox should capture all 3 lines shown in monkey type
bbox2 should capture the bottom 2 lines shown in monkey type
'''

bbox = (395, 520, 1560, 665)
bbox2 = (400, 580, 1560, 665)

def waiting_for_start():
    while 1:
        if ptg.position()[0] <= 10:
            break

def replace_char(text):
    new_text = ''
    for char in text:
        if char in string.ascii_letters or char == ' ':
            new_text += char
        if char == '\n':
            new_text += ' '
    
    return new_text

def process_image(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_gray = np.array([10,10,10])
    upper_gray = np.array([110,110,110])

    mask = cv2.inRange(hsv,lower_gray,upper_gray)

    image[mask == 0] = (55,52,50)
    return image

def get_words(image):
    cv2.imwrite('screenshot.png', image)
    text = ptr.image_to_string(image)
    text = replace_char(text)

    return text

def send_words_human(text):
    for word in text.split(' '):
        interval = decimal.Decimal(random.randrange(15, 30))/1000
        
        ptg.write(word, interval=interval)
        ptg.write(' ')

def send_words_bot(text):
    ptg.write(text, interval=0.000001)
    time.sleep(0.1)

def main():
    image = np.array(ImageGrab.grab(bbox=bbox))
    image = process_image(image)

    text = get_words(image)
    
    send_words_bot(text)

    while 1:
        try:
            image = np.array(ImageGrab.grab(bbox=bbox2))
            image = process_image(image)

            text = get_words(image)
            print(text)

            
            
            send_words_bot(text)
        except:
            break


if __name__ == "__main__":
    waiting_for_start()
    main()
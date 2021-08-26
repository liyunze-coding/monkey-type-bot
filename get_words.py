import cv2
import numpy as np
import pytesseract as ptr
import string

'''
this file acts as a testing environment for the image processing
to get rid of the yellow bar
and to test the tesseract OCR 
'''

def replace_char(text):
    new_text = ''
    for char in text:
        if char in string.ascii_letters or char == ' ':
            new_text += char
        if char == '\n':
            new_text += ' '
    
    return new_text

image = cv2.imread('ss.png')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_gray = np.array([0,0,0])
upper_gray = np.array([120,120,120])

mask = cv2.inRange(hsv,lower_gray,upper_gray)

image[mask == 0] = (55,52,50)

cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.waitKey(0)

text = replace_char(ptr.image_to_string(image))
print(text)
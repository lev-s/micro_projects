#github.com/lev-s

#Install packages before using

#cmd code to install cv2:
#py -m pip install opencv-python

#cmd code to install pyautogui:
#py -m pip install pyautogui

##################################################################
from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)

input_Text = input("Please, enter the text to generate into CAPTCHA image:\n")

captcha_text = input_Text

data = image.generate(captcha_text)

image.write(captcha_text, "CAPTCHA.png")
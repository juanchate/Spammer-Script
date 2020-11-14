import pyautogui
import time
import keyboard
time.sleep(5)
#Change the first parameter to the location of the file you want to use, also you should eliminate the second parameter
#If the text of the file is written in english
file = open("beemoviescript.txt", "r", encoding='Latin-1')
for word in file:
    if keyboard.is_pressed('p'):
        break
    pyautogui.typewrite(word)
    pyautogui.press('enter')
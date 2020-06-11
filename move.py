import pyautogui
import random
import time
import pygetwindow as gw
from random_word import RandomWords
import keyboard


while keyboard.is_pressed('esc') == False:

    counter = 0
    t = random.randrange(1, 30, 3)
    rc = random.randint(2, 20)
    print('waiting for', t, 'seconds')
    time.sleep(t)
    task = random.randrange(1,4,1)
    print('task is', task)
    if task == 1:
        print(rc, 'movements')
        while rc > counter and keyboard.is_pressed('esc') == False:
            counter += 1
            print('counter is', counter)
            y = random.randrange(0, 764)
            x = random.randrange(0, 1360)
            duration = random.uniform(0, 5)
            pyautogui.moveTo(x,y, duration)
    if task == 2:
        try:
            win = gw.getWindowsWithTitle('Блокнот')[0]
            win.activate()
            print('some text printing')
            r = RandomWords()
            rword = r.get_random_word() + " "
            pyautogui.typewrite((rword), interval=0.2)
        except:
            pyautogui.typewrite('Hello world ', interval=0.2)
    if task == 3:
            print('pressing ALT+TAB')
            pyautogui.hotkey('alt', 'tab')
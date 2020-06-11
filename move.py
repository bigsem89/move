import pyautogui
import random
import time
import pygetwindow as gw
from random_word import RandomWords
import keyboard

import logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')
#logging.disable(logging.CRITICAL)
logging.info('start of program')

while keyboard.is_pressed('esc') == False:

    counter = 0
    t = random.randrange(1, 30, 3)
    rc = random.randint(2, 20)
    logging.info(f'Waiting for {t} seconds')
    time.sleep(t)
    task = random.randrange(1,4,1)
    logging.info(f'task is {task}')
    if task == 1:
        logging.info(f'{rc} movements')
        while rc > counter and keyboard.is_pressed('esc') == False:
            counter += 1
            logging.info(f'counter is {counter}')
            y = random.randrange(0, 764)
            x = random.randrange(0, 1360)
            duration = random.uniform(0, 5)
            pyautogui.moveTo(x,y, duration)
    if task == 2:
        try:
            win = gw.getWindowsWithTitle('Блокнот')[0]
            win.activate()
            logging.info('some text printing')
            r = RandomWords()
            rword = r.get_random_word() + " "
            pyautogui.typewrite((rword), interval=0.2)
        except:
            pyautogui.typewrite('Hello world ', interval=0.2)
    if task == 3:
            logging.info('pressing ALT+TAB')
            pyautogui.hotkey('alt', 'tab')

logging.info('end of program')
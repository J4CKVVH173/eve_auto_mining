import time

import numpy as np
import pyscreenshot as sc

from pynput.keyboard import Controller

screen = (1000, 200, 1200, 500)
keyboard = Controller()

COLOR_FOR_FIND = np.array([33, 35, 43])
counter = 0

if __name__ == '__main__':
    time.sleep(1)
    im = sc.grab(bbox=screen)
    im.show()
    array = np.array(im)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if np.array_equal(array[0][0], COLOR_FOR_FIND):
                counter += 1
    print(counter)
    keyboard.press('f1')

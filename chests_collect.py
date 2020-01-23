import time

import numpy as np
import pyautogui
import pyscreenshot as sc
from pynput.keyboard import Controller
from pynput.mouse import Button, Controller as MouseController

SCREEN = (1500, 1000, 1760, 1100)  # Место экрана которое будет обрабатываться
CHEST = (1617, 1048)  # Место где находится сундук
keyboard = Controller()
mouse = MouseController()

COLOR_FOR_FIND = np.array([0, 230, 203])  # цвет который будет искаться на месте обработки
counter = 0


if __name__ == '__main__':
    while True:
        time.sleep(60)
        im = sc.grab(bbox=SCREEN)
        array = np.array(im)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                # если искомый пиксель есть в обрабатываемой области экрана, увеличиваем счетчик
                if np.array_equal(array[i][j], COLOR_FOR_FIND):
                    counter += 1
        print(counter)
        # если в обрабатываемой области достаточно искомых пикселей, перемещаем курсор в нужное места экрана
        # и производим клин
        if counter > 1000:
            pyautogui.moveTo(*CHEST)
            time.sleep(0.1)  # небольшие паузы перед действиями
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            pyautogui.move(-200, -200)
        counter = 0

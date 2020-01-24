import time

import numpy as np
import pyscreenshot as sc
from pynput.mouse import Button as MButton, Controller as MController


class Bot:
    def __init__(self):
        self.SCREEN = (1500, 1000, 1760, 1100)  # Место экрана которое будет обрабатываться
        self.CHEST = (1617, 1048)  # Место где находится сундук
        self.COLOR_FOR_FIND = np.array([0, 230, 203])  # цвет который будет искаться на месте обработки
        self.MOUSE_CONTROLLER = MController()

    def bot_execute(self):
        counter = 0
        im = sc.grab(bbox=self.SCREEN)
        array = np.array(im)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                # если искомый пиксель есть в обрабатываемой области экрана, увеличиваем счетчик
                if np.array_equal(array[i][j], self.COLOR_FOR_FIND):
                    counter += 1
        # если в обрабатываемой области достаточно искомых пикселей, перемещаем курсор в нужное места экрана
        # и производим клин
        if counter > 1000:
            mouse_position = self.MOUSE_CONTROLLER.position
            self.MOUSE_CONTROLLER.position = self.CHEST
            self.MOUSE_CONTROLLER.click(MButton.left, 1)
            time.sleep(0.1)
            self.MOUSE_CONTROLLER.position = mouse_position


bot = Bot()

while True:
    time.sleep(60)
    bot.bot_execute()

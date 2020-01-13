import numpy
import pyscreenshot as sc

screen = (1500, 20, 1900, 300)

arrays = []

if __name__ == '__main__':
    im = sc.grab(bbox=screen)
    arrays.append(numpy.array(im))

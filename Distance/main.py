import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Pixel:

    def __init__(self, x, y):
        self.x = x
        self.y = y


np.power(2,3)


def euclid(p1,p2):
    dis = np.sqrt(np.power((p1.x-p2.x),2)+np.power((p1.y-p2.y),2))
    return dis


def city_block(p1,p2):
    return np.absolute(p1.x-p2.x)+np.absolute(p1.y-p2.y)


def chessboard(p1,p2):
    return max(np.absolute(p1.x-p2.x),np.absolute(p1.y-p2.y))


p1 = Pixel(21,8)
p2 = Pixel(8,2)


print(euclid(p1, p2))

print(city_block(p1, p2))

print(chessboard(p1, p2))

img=mpimg.imread('images.png')
imgplot = plt.imshow(img)
plt.show()
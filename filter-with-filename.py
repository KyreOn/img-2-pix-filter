from PIL import Image
import numpy as np


class Image2PixelFilter:
    def __init__(self, p_size, g_scale_step):
        self.__pixel_size = p_size
        self.__grayscale_step = g_scale_step
        self.__img_arr = np.array(Image.open("img2.jpg"))

    def get_average(self, x, y):
        average = np.sum((self.__img_arr[y: y + self.__pixel_size, x: x + self.__pixel_size])) / 3
        return int(average // (self.__pixel_size * self.__pixel_size))

    def make_gray(self, x, y):
        average = self.get_average(x, y)
        self.__img_arr[y: y + self.__pixel_size, x: x + self.__pixel_size] = \
            int(average // self.__grayscale_step) * self.__grayscale_step

    def convert(self, out_file):
        height, width = len(self.__img_arr), len(self.__img_arr[1])
        for y in range(0, height, self.__pixel_size):
            for x in range(0, width, self.__pixel_size):
                self.make_gray(x, y)
        res = Image.fromarray(self.__img_arr)
        res.save(out_file)
        print("Готово")


f = Image2PixelFilter(10, 50)
f.convert("newres.jpg")



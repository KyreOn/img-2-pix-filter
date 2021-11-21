import PIL
from PIL import Image
import numpy as np


class Image2PixelFilter:
    def __init__(self, p_size, g_scale_step):
        self.__pixel_size = p_size
        self.__grayscale_step = g_scale_step
        self.__img_arr = None

    def get_average(self, x, y):
        average = np.sum((self.__img_arr[y: y + self.__pixel_size, x: x + self.__pixel_size])) / 3
        return int(average // (self.__pixel_size * self.__pixel_size))

    def make_gray(self, x, y):
        average = self.get_average(x, y)
        self.__img_arr[y: y + self.__pixel_size, x: x + self.__pixel_size] = \
            int(average // self.__grayscale_step) * self.__grayscale_step

    def convert(self, in_file, out_file):
        try:
            self.__img_arr = np.array(Image.open(in_file))
            height, width = len(self.__img_arr), len(self.__img_arr[1])
            for y in range(0, height, self.__pixel_size):
                for x in range(0, width, self.__pixel_size):
                    self.make_gray(x, y)
            res = Image.fromarray(self.__img_arr)
            res.save(out_file)
            print("Готово")
        except FileNotFoundError:
            print(f"'{in_file}' не найден. Проверьте правильность введенного имени")
        except PIL.UnidentifiedImageError:
            print(f"'{in_file}' не является изображением. Проверьте правильность введенного имени")
        except ValueError:
            print(f"Невозможно записать полученное изображение в '{out_file}'. Проверьте расширение файла")


input_file = input("Имя входного изображения: ")
output_file = input("Имя выходного изображения: ")

pixel_size = input("Размер пикселей(необязательно): ")
p_size_int = int(pixel_size) if pixel_size.isdigit() else 10

grayscale_step = input("Шаг градации серого(необязательно): ")
g_scale_step_int = int(grayscale_step) if grayscale_step.isdigit() else 50


f = Image2PixelFilter(p_size_int, g_scale_step_int)
f.convert(input_file, output_file)


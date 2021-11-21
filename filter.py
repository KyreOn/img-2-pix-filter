import PIL
from PIL import Image
import numpy as np


class Image2PixelFilter:
    def __init__(self, p_size: int, g_scale_step: int, in_file: str):
        """
        :param p_size: Размер квадратов мозаики
        :param g_scale_step: Шаг градации серого
        :param in_file: Путь к входному изображению

        >>> f = Image2PixelFilter(10, 50, "img2.jpg")

        >>> f = Image2PixelFilter(10, 50, "img.jpg")
        'img.jpg' не найден. Проверьте правильность введенного имени
        >>> f = Image2PixelFilter(10, 50, "filter.py")
        'filter.py' не является изображением. Проверьте правильность введенного имени
        """
        self.__pixel_size = p_size
        self.__image = in_file
        self.__grayscale_step = g_scale_step
        try:
            self.__img_arr = np.array(Image.open(self.__image))
        except FileNotFoundError:
            print(f"'{in_file}' не найден. Проверьте правильность введенного имени")
        except PIL.UnidentifiedImageError:
            print(f"'{in_file}' не является изображением. Проверьте правильность введенного имени")

    def get_average(self, x: int, y: int) -> int:
        """
        Возвращает среднюю яркость цвета в квадрате с длинной, равной
        размеру мозаики, с заданными координатами верхнего левого угла.
        :param x: x-координата левого верхнего угла квадрата
        :param y: y-координата левого верхнего угла квадрата
        :return: Средняя яркость в квадрате
        >>> f = Image2PixelFilter(10, 50, "img2.jpg")
        >>> f.get_average(0, 0)
        18
        >>> f.get_average(-10, 0)
        0
        >>> f.get_average(0, -10)
        0
        >>> f.get_average(9999999999999, 99999999999)
        0
        """
        average = np.sum((self.__img_arr[y: y + self.__pixel_size, x: x + self.__pixel_size])) / 3
        return int(average // (self.__pixel_size * self.__pixel_size))

    def make_gray(self, x: int, y: int):
        """
        Закрашивает все пиксели в квадрате в серый цвет, полученной
        в функции *get_average* яркости и "округленной" до определенной градации серого.
        :param x: x-координата левого верхнего угла квадрата
        :param y: y-координата левого верхнего угла квадрата
        """
        average = self.get_average(x, y)
        self.__img_arr[y: y + self.__pixel_size, x: x + self.__pixel_size] = \
            int(average // self.__grayscale_step) * self.__grayscale_step

    def convert(self, out_file: str):
        """
        Переводит входное изображение в массив цветов. И делит
        его на квадраты. После чего проходит по каждому квадрату, выполняя для него функцию
        *make_gray*. Выводит полученный результат в виде изображения с заданным названием.
        :param out_file: Название выходного изображения
        >>> f = Image2PixelFilter(10, 50, "img2.jpg")
        >>> f.convert("newres.jpg")
        Готово
        >>> f.convert("newres.txt")
        Невозможно записать полученное изображение в 'newres.txt'. Проверьте расширение файла
        """
        try:
            height, width = len(self.__img_arr), len(self.__img_arr[1])
            for y in range(0, height, self.__pixel_size):
                for x in range(0, width, self.__pixel_size):
                    self.make_gray(x, y)
            res = Image.fromarray(self.__img_arr)
            res.save(out_file)
            print("Готово")
        except ValueError:
            print(f"Невозможно записать полученное изображение в '{out_file}'. Проверьте расширение файла")


input_file = input("Имя входного изображения: ")
output_file = input("Имя выходного изображения: ")

pixel_size = input("Размер пикселей(необязательно): ")
p_size_int = int(pixel_size) if pixel_size.isdigit() else 10

grayscale_step = input("Шаг градации серого(необязательно): ")
g_scale_step_int = int(grayscale_step) if grayscale_step.isdigit() else 50

f = Image2PixelFilter(p_size_int, g_scale_step_int, input_file)
f.convert(output_file)


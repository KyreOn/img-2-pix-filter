from filter import Image2PixelFilter


input_file = input("Имя входного изображения: ")
output_file = input("Имя выходного изображения: ")

pixel_size = input("Размер пикселей(необязательно): ")
p_size_int = int(pixel_size) if pixel_size.isdigit() else 10

grayscale_step = input("Шаг градации серого(необязательно): ")
g_scale_step_int = int(grayscale_step) if grayscale_step.isdigit() else 50

f = Image2PixelFilter(p_size_int, g_scale_step_int, input_file)
f.convert(output_file)
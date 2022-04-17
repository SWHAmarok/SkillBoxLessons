# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

#
def smile(x, y, color):
    point = sd.get_point(x, y)
    radius = sd.random_number(20, 60)
    left_eye = sd.get_point(x - radius * .4, y + radius * .4)
    right_eye = sd.get_point(x + radius * .4, y + radius * .4)
    bottom_point_smile = sd.get_point(x - radius * .66, y - radius * .66)
    top_point_smile = sd.get_point(x + radius * .66, y + radius * 0.01)
    bottom_point_half_smile = sd.get_point(x - radius * .66, y - radius * .33)
    sd.circle(center_position=point, radius=radius, color=color, width=2)
    sd.circle(center_position=left_eye, radius=radius * 0.1, color=color, width=2)
    sd.circle(center_position=right_eye, radius=radius * 0.1, color=color, width=2)
    sd.ellipse(left_bottom=bottom_point_smile, right_top=top_point_smile, width=2, color=color)
    sd.rectangle(left_bottom=bottom_point_half_smile, right_top=top_point_smile, color=sd.background_color, width=0)


for _ in range(10):
    x = sd.random_number(150, 1000)
    y = sd.random_number(150, 400)
    color = sd.random_color()
    smile(x=x, y=y, color=color)

sd.pause()

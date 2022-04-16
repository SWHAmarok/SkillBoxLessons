# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw
sd = simple_draw
sd.resolution = (600, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

#
x, y = 0, 0
step_x, step_y = 100, 50
for x in range(0, 1201, step_x):
    leff_bottom_point = sd.get_point(x, y)
    right_top_point = sd.get_point(x + step_x, y + step_y)
    for y in range(0, 601, step_y):
        x -= step_y
        leff_bottom_point = sd.get_point(x, y)
        right_top_point = sd.get_point(x + step_x, y + step_y)
        sd.rectangle(left_bottom=leff_bottom_point, right_top=right_top_point, color=sd.COLOR_ORANGE, width=1)
sd.pause()
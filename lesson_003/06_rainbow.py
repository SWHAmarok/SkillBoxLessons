# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
#
# x1, x2 = 50, 350
# y1, y2 = 50, 450
# i = 0
# step = 5
#
# for i in range(6):
#     i += 1
#     x1 -= step
#     x2 -= step
#     start_point = sd.get_point(x1, y1)
#     end_point = sd.get_point(x2, y2)
#     sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[i], width=5)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
#
x, y = 350, -80
central_point = sd.get_point(x, y)
radius = 400
step = 30
i = -1
for i in range(7):
    radius += step
    sd.circle(center_position=central_point, radius=radius, color=rainbow_colors[i], width=30)
    i += 1

sd.pause()

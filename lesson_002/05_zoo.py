#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# Код для добавления объекта в указанное место в списке. Использование оперции .insert()
zoo.insert(1, 'bear')
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# Код для добавления в список объектов из другого списка. Использование сложения списков и операции .extend()
zoo = zoo + birds
print(zoo)

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
# Код для убирания слона из списка и вывод списка на консоль. Использование операции .remove()
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# Код для вывода номеолв клеток, в которых находятся требуемые объекты - лев и жаворонок. Использование операции inbex().
print('Лев находится в клетке №', zoo.index('lion') + 1, '\nЖаворонок находится в клетке №', zoo.index('lark') + 1)



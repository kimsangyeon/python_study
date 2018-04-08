#coding=utf-8

import math

x1 = 2
y1 = 1
x2 = 5
y2 = 5

# 좌표 (x1, y1) (x2, y2) math.atan2(y2 - y1, x2 - x1)
# math.tan((y2 - y1 / x2 - x1))
angle = math.atan2(y2 - y1, x2 - x1)

print(angle * 57.17448)


# x = math.atan(1)
# y = x * 180 / math.pi
# print(x)
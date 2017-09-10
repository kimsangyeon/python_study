# coding=utf-8

"""
list = 배열 (array)
"""

list = ['sun', 'mon', 'tue', 'wed', 'thu', 'fir', 'sat']
print("sunday : ", list[0])

list[0] = "sunday"
print("일요일:", list[0])

print(list[1:3])

days = ['mon', 'tue', 'wed']
week = [days, list]
print(week)nums = ['one', 'two', 'three']
week = [nums, list]
print(week)
print(week[1][1])
print(week[0][0])

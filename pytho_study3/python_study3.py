# coding=utf-8

"""
list = 배열 (array)
"""

list = ['sun', 'mon', 'tue', 'wed', 'thu', 'fir']
print("sunday : ", list[0])

list[0] = "sunday"
print("일요일:", list[0])

print(list[1:3])

nums = ['one', 'two', 'three']
week = [nums, list]
print(week)
print(week[1][1])
print(week[0][0])

# append 맨뒤에 추가
list.append('sat')
print(week)

# insert 원하는 index에 추가
list.insert(1, 'holiday')
print(week)

# remove 데이터 삭제
list.remove('mon')
print(week)

# sort 정렬
list.sort();
print(week)

# reverse 뒤집기
list.reverse();
print(week)



# coding=utf-8
# 튜플 (tuple)

pi_tuple = (3,1,4,1,5,9)
print(pi_tuple)

conv_list = list(pi_tuple)
print(conv_list)

conv_tuple = tuple(conv_list)
print(conv_tuple)

l = len(pi_tuple)
print(l)

# index 리스트와 동일
print(pi_tuple[1])

# index - 뒤에서
print(pi_tuple[-2])

print(pi_tuple[3:])
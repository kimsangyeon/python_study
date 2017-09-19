# coding=utf-8
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    remainder = a//b
    quotient = a/b

    print(remainder)
    print("%.11f" % quotient)
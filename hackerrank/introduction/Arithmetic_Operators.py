if __name__ == '__main__':
    a = int(input())
    b = int(input())
    constraintsN = pow(10, 10);

    if a < 1 or b < 1 or a > constraintsN or b > constraintsN:
        print("Wrong input num! : 1 <= n <= 10^10 ")

    print(a + b)
    print(a - b)
    print(a * b)

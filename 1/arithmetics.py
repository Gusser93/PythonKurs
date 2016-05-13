def square(root):
    return root * root


def div(dividend, divisor):
    return (dividend + 0.0) / divisor


def cube(number):
    return square(number) * number


if __name__ == "__main__":
    print "This provides square(x), div(a,b) and cube(x)"

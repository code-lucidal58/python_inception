"""
Convert integers of base10 to another base in the range [2,36]. Representation will be in alphanumeric format.
"""
import string


def base_convertor(n, b):
    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + list(string.ascii_uppercase)
    if b < 2 or b > 36:
        raise ValueError('base b must be in the range [2,36]')
    sign = -1 if n < 0 else 1
    n = n * sign
    digits = list()
    if n == 0:
        return [0]
    while n > 0:
        n, m = divmod(n, b)  # here, n  = n//b and m = n%b
        digits.insert(0, mapping[m])

    encoding = ''.join(map(str, digits))
    return '-' + encoding if sign == -1 else encoding


if __name__ == '__main__':
    print(base_convertor(3451, 16))
    print(base_convertor(255, 8))
    print(base_convertor(-255, 8))
    print(base_convertor(314, 2))

import math


def soNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorSum_solve(n):
    k = 2
    sum_ = 0
    while n > 1:
        while n % k == 0:
            sum_ += k
            n /= k
        k += 1

    return sum_


def factorSum(n):
    while n != factorSum_solve(n):
        n = factorSum_solve(n)
    return n


def greatestCommonPrimeDivisor(a, b):
    lsta = []
    lstb = []
    for i in range(2, a):
        if a % i == 0:
            lsta.append(i)
    for i in range(2, b):
        if b % i == 0:
            lstb.append(i)
    lst_out = []
    for i in lsta:
        if i in lstb:
            lst_out.append(i)
    ls = []
    for i in lst_out:
        if soNguyenTo(i):
            ls.append(i)

    if lst_out:
        ls.sort(reverse=True)
        return ls[0]
    else:
        return -1


def maxFraction(numerators, denominators):
    cs = 0
    for i in range(len(numerators)):
        if numerators[cs] * denominators[i] < numerators[i] * denominators[cs]:
            cs = i
    return cs


def lastDigitDiffZero(n):
    return int(str(int(str(math.factorial(n))[::-1]))[0])
print(lastDigitDiffZero(5))
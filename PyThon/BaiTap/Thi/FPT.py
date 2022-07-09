# arr = [int(x) for x in input('Nhap cac so').split(',')]


def evenDigitsNumber(arr):
    if 0 <= len(arr) <= 10 ** 5:
        op = []
        for x in arr:
            if 0 <= x <= 10 ** 6:
                dem = 1
                while x >= 10:
                    x /= 10
                    dem += 1
                if dem != 0 and dem % 2 == 0:
                    op.append(x)
            else:
                evenDigitsNumber(arr)
        out_p = int(len(op))
        print(out_p)
    else:
        evenDigitsNumber(arr)


def messageScreen(arr, k):
    if 0 <= len(arr) <= 10 ** 5 and 1 <= k <= 10 ** 8:
        for x in arr:
            if 0 <= x <= 10 ** 5 and type(x)== int:
                op = []
                for n in arr:
                    if n in op:
                        continue
                    else:
                        op.append(n)
                y = 1
                tra = False
                for x in op:
                    if int(y) == int(k):
                        tra = x
                        print(tra)
                        break
                    else:
                        y += 1
                if not tra:
                    return -1
                else:
                    return tra
            else:
                exit()
    else:
        exit()

arr = [1,1, 2, 3]
k = 2
messageScreen(arr, k)

def count_pass_student(arr):
    if 1 <= len(arr) <= 10 ** 5:
        sum = 0
        for v in arr:
            sum += v
        sum /= len(arr)
        op = 0
        for v in arr:
            if v >= sum:
                op += 1
            else:
                continue
        print(op)
        return op
    else:
        return False


def join_number(m, n):
    if 1 <= len(m) and len(n) <= 8:
        a = m + n
        a.sort(reverse=True)
        b = ''
        for i in a:
            b += str(i)
        b = int(b)
        print(b)
        return b
    else:
        return False


def equilateralNumber(a):
    if -10000000 <= int(a) <= 10000000 and type(a)== int:
        b = abs(a)
        b = ' '.join(str(b))
        c = [int(x) for x in b.split()]
        chan = 0
        le = 0
        for i in c:
            if i % 2 == 0:
                chan += 1
            else:
                le += 1
        if chan == le:
            return True
        else:
            return False
    else:
        exit()

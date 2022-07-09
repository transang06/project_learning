import math


# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456
def bai_9():
    c = 50
    h = 30
    items = [x for x in input('Nhap cac gia tri cach nhau boi (,):\n').split(',')]
    out = []
    for x in items:
        x = int(x)
        out.append(str(round(math.sqrt((2 * c * x) / h))))
    print(','.join(out))


def bai_10():
    rows, cols = [int(x) for x in input('nhap x va y cach nhau boi (,): \n').split(',')]
    multilist = [[0 for x in range(cols)] for y in range(rows)]
    for row in range(rows):
        for col in range(cols):
            multilist[row][col] = row * col

    print(multilist)


def bai_11():
    in_put = [x for x in input('nhap x va y cach nhau boi (,): \n').split(',')]
    # in_put = sorted(in_put) # tu lam
    in_put.sort()
    print(','.join(in_put))


def bai_12():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break
    for sentence in lines:
        print(sentence)


def bai_13():
    in_put = [x for x in input('nhap vao: ').split()]
    print(" ".join(sorted(list(set(in_put)))))


def bai_14():
    in_put = [x for x in input('nhap vao so nhi phan: ').split(',') if (int(x, base=2) % 5 == 0)]
    print(','.join(in_put))


def bai_15():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and \
                (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            values.append(s)
    print(",".join(values))


def bai_16():
    s = input('Nhap chuoi: ')
    d = {"So": 0, "Chu": 0}
    for i in s:
        if i.isdigit():  # check i co phai so ko
            d['So'] += 1
        elif i.isalpha():  # check i co phai chu k
            d['Chu'] += 1
        else:
            pass
    print("Số chữ cái là:", d["Chu"])
    print("Số chữ số là:", d["So"])


def bai_17():
    s = input("Nhập câu của bạn: ")
    d = {"UPPER CASE": 0, "LOWER CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER CASE"] += 1
        elif c.islower():
            d["LOWER CASE"] += 1
        else:
            pass
    print("Chữ hoa:", d["UPPER CASE"])
    print("Chữ thường:", d["LOWER CASE"])


def bai_18():
    a = input("Nhập số a: ")
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a, a))
    n3 = int("%s%s%s" % (a, a, a))
    n4 = int("%s%s%s%s" % (a, a, a, a))
    print("Tổng cần tính là: ", n1 + n2 + n3 + n4)


def bai_19():
    netAmount = 0
    while True:
        s = input("Nhập nhật ký giao dịch: ")
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation == "D":
            netAmount += amount
        elif operation == "W":
            netAmount -= amount
        else:
            pass
    print(netAmount)


bai_19()

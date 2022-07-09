def bai_01():
    in_put = range(2000, 3201)
    out_put = []
    for x in in_put:
        if (x % 7 == 0) and (x % 5 != 0):
            out_put.append(str(x))
    print(','.join(out_put))


def bai_02_me():
    out_put = 1
    in_put = int(input('nhap so de tinh giai thua: '))
    while in_put > 0:
        out_put = out_put * in_put
        in_put -= 1

    print(out_put)


def bai_02_solution():
    in_put = int(input('nhap so de tinh giai thua: '))

    def fact(in_put):
        if in_put == 0:
            return 1
        return in_put * fact(in_put - 1)

    print(fact(in_put))


def bai_3():
    in_put = int(input('Nhap vao 1 so nguyen: '))
    out_put = dict()
    for i in range(1, in_put + 1):
        out_put[i] = i * i
    print(out_put)


def bai_4():
    in_put = input('Nhap vao 1 chuoi cac so nguyen tach nhau boi (,): \n')
    list_ = in_put.split(',')  # mac dinh la list
    tuple_ = tuple(in_put.split(','))
    print(list_)
    print(tuple_)


def bai_5():
    class ChuHoa:
        def __init__(self):
            self.str = ''

        def getString(self):
            self.str = input("Nhap chuoi: ")

        def printString(self):
            print(self.str.upper())

    strObj = ChuHoa()
    strObj.getString()
    strObj.printString()


def bai_6():
    in_put = int(input('Nhap vao 1 so de tinh binh phuong: '))

    def square(x):
        return x ** 2

    print("binh phuong cua", in_put, "la", square(in_put))


def bai_7():
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)


def bai_8():
    class Person:
        name = "person"

        def __init__(self, name=None):
            self.name = name

    jeffrey = Person("Jeffrey")
    print("%s name is %s" % (Person.name, jeffrey.name))
    nico = Person()
    nico.name = "Nico"
    print("%s name is %s" % (Person.name, nico.name))

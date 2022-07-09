import random

print(dir(random))

num1, num2 = [int(x) for x in input('nhap 2 so: ').split()]

if num1 > 0:
    print(num1, "la so duong")
else:
    print(str(num1) + " la so am")


def Numbers_Random(num_1=0, num_2=0):
    if num_1 < num_2:
        print('so ngau nhien', random.randrange(num_1, num_2))
    elif num_1 < num_2:
        print('so ngau nhien', random.randrange(num_2, num_1))
    else:
        return num_1


Numbers_Random(num1, num2)
print('Tong 2 so', num1, num2, 'là', num1 + num2)

for x in range(num1, num2, 3):
    print(x)



# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456
import re


def bai_21():
    value = []
    items = [x for x in input("Nhập mật khẩu: ").split(',')]
    for p in items:
        if len(p) < 6 or len(p) > 12:
            continue
        if not re.search("[a-z]", p):
            continue
        elif not re.search("[0-9]", p):
            continue
        elif not re.search("[A-Z]", p):
            continue
        elif not re.search("[$#@]", p):
            continue
        elif re.search("\s", p):
            continue
        else:
            pass
        value.append(p)
    print(",".join(value))

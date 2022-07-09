def before(y1, m1, d1, y2, m2, d2):
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return True
    return False

def day_in_week(y, m, d):
    tab = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + int(y/4) - int(y/100) + int(y/400) + tab[m-1] + d) % 7

def valid(y1, m1, d1, y2, m2, d2, y, m, d, w):
    if not (before(y1, m1, d1, y, m, d) and before(y, m, d, y2, m2, d2)):
        return False
    if day_in_week(y, m, d) == 0:
        if w == 8:
            return True
        return False
    return day_in_week(y, m, d) + 1 == w

def main():
    y1, m1, d1, y2, m2, d2, w = map(int, input().split())
    n = int(input())
    for i in range(n):
        y, m, d = map(int, input().split())
        if valid(y1, m1, d1, y2, m2, d2, y, m, d, w):
            print("VALID")
        else:
            print("INVALID")

main()
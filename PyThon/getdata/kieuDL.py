import json


def caodl():
    with open('data.txt', 'r', encoding='utf-8') as f:
        a = f.readlines()
        output = {}
        content = []
        htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'),
            ('', '<em>'),
            ('', '</em>')
        )
        for idx, val in enumerate(a):
            val = val.strip()
            if '<h1 class="dt-news__title">' in val:
                output["title"] = a[idx + 1].strip()
                # w.write("Tiêu đề bài viết: " + a[idx + 1].strip() + "\n")
                for code in htmlCodes:
                    output["title"] = output["title"].replace(code[1], code[0])
            elif "<p>" in val:
                nd = val.split("<p>")[1].split("</p>")[0]
                for code in htmlCodes:
                    nd = nd.replace(code[1], code[0])
                content.append(nd)
        output["content"] = content
        # with open('data1.txt', 'w') as ajs:
        #     json.dump(output, ajs)
        # with open('data1.txt', 'r', encoding='utf-8') as rjs:
        #     data = json.load(rjs)
        #     print(data["title"])
        #     for i in data["content"]:
        #         print(i)

        with open('index.html', 'r', encoding='utf-8') as rjs:
            read = rjs.read()
            read = read.replace("@@title@@", output["title"])
            ll = ""
            for i in output["content"]:
                ll += i + "<br><br>"
            read = read.replace("@@content@@", ll)
        tenfile = output["title"][0:10] + '.html'
        with open(tenfile, 'w', encoding='utf-8') as rjs:
            rjs.write(read)


def btlist():
    n = int(input())
    out = []
    for i in range(n):
        a = input()
        out.append(a.split())
    out1 = []
    for i in out:
        if i[0] == 'insert':
            out1.insert(int(i[1]), int(i[2]))
        elif i[0] == 'print':
            print(out1)
        elif i[0] == 'remove':
            out1.remove(int(i[1]))
        elif i[0] == 'append':
            out1.append(int(i[1]))
        elif i[0] == 'sort':
            out1.sort()
        elif i[0] == 'pop':
            out1.pop()
        elif i[0] == 'reverse':
            out1.reverse()
    return out1


def learnset():
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    s3 = {3, 4, 5}
    s4 = s1.intersection(s2, s3)
    s5 = s1.symmetric_difference(s2)
    print(s4)
    print(s5)


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' (' + str(self.capacity) + 'L)')

    def __add__(self, other):
        return (self.name + "&" + other.name + "(" + str(self.capacity + other.capacity) + "L)")


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)

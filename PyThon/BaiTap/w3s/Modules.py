import ClassStudent
from mymodule import person1
import platform
import datetime
import math
import json
import re


def showSystem():
    x = platform.system()
    print(x)


def callClass():
    ClassStudent.Student("Tran", "Sang", "2020").welcome()
    a = person1["age"]
    print(a)


def createNgay():
    x = datetime.datetime(2020, 5, 17)
    print(x)


def ngayGio():
    x = datetime.datetime.now()
    print(x)
    print(x.day)
    print(x.month)
    print(x.year)
    print(x.strftime("%A"))


def toan():
    arr = [5, 10, 20]
    x = min(arr)
    y = max(arr)
    print(x)
    print(y)
    print(abs(-65))
    print(4 ** 6)
    print(pow(4, 6))
    x = math.sqrt(64)
    print(x)
    x = math.ceil(1.4)  # lam tron lne
    y = math.floor(1.4)  # lam tron xuong
    print(x)
    print(y)
    x = math.pi
    print(x)


def jsonToPython():
    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    print(y["age"])


def pythonToJson():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    y = json.dumps(x, indent=4, separators=(". ", " = "))
    print(y)


def showJSON():
    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }
    print(json.dumps(x, indent=4, sort_keys=True))


def search_():
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)
    x = re.split("\s", txt)
    print(x)


search_()

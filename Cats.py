cats=[
    {"name":"Baron",
    "sex":"M",
    "age":2},
    {"name":"Sam",
    "sex":"M",
    "age":2}
    ]

class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

for i in cats:
    obj=Cat(name=i.get("name"),sex=i.get("sex"), age=i.get("age"))
    print('Имя', obj.name, 'Пол', obj.sex, 'Возраст', obj.age)


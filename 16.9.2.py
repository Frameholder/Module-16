#16.9.2
# #Напишите код для описания геометрической фигуры.
#Создайте класс «прямоугольник» с помощью метода  __init__(). На выходе в консоли вам необходимо получить длину и ширину с итоговыми значениями.

print('Задание 19.9.2')
class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def square(self):
        return self.a*self.b

Rec=Rectangle(5,10)

print(Rec.square())

#16.9.3
#Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее:
# Клиент "Иван Петров". Баланс: 50 руб.

print('Задание 19.9.3')
print('______')

class Wallet:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Клиент: {self.name}. Баланс:{self.balance}'
name=str(input('Enter your name '))
balance=int(input('Enter amount you want to spend, USD '))
Client1 = Wallet(name, balance)

print(Client1.__str__())
print('______')
print('______')

#16.9.4
#составлять список нескольких гостей. Решите задачу с помощью метода
# конструктора и примените один из принципов наследования.

#При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
print('______')
print('______')

print('Задание 19.9.4')
print('______')

class Data:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status



    def __str__(self):
        return f'Клиент: {self.name}. Место жительства:{self.city}. Статус:{self.status}'

Client1 = Data(name='Ivanov', city='Moscow', status='Teacher')
Client2 = Data(name='Gosia', city='Daleko', status='in a relationships')
Client3 = Data(name='Boris Britva', city='London', status='Killer')
print(Client1.__str__())
print(Client2.__str__())
print(Client3.__str__())

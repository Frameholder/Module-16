Shapes=['Circle','Square','Rectangle']
print('Есть список фигур', Shapes)

while True:
    Figure = str(input('Введите название фигуры '))
    Figure_split = Figure.split()
    anb = set(Figure_split) & set(Shapes)
    if not anb:
        for i in Figure_split:
            if i not in Shapes:
                print(f'Нет такой фигуры в списке', {i})
    elif len(Figure_split)>1:
        print('Нельзя одновременно использовать более одной фигуры')
    else:
        break
print(Figure_split)
L1=['Circle']
L2=['Rectangle']
L3=['Square']


class Geom_Figure:
    if Figure_split == L1:
        def __init__(self, Figure_split, r):
            self.r = r
            self.Figure_split = Figure_split
    if Figure_split == L2:
        def __init__(self, Figure_split, a, b, width, height):
        #elif Figure_split==L2:
            self.a=a
            self.b=b
            self.width=width
            self.height=height

            self.Figure_split = Figure_split

    if Figure_split == L3:
        def __init__(self, Figure_split, a, width, height):
            #elif Figure_split==L3:
            self.a = a
            self.width = width
            self.height = height
            self.Figure_split = Figure_split
        #self.Figure_split=Figure_split


    def __str__(self):
        if self.Figure_split==L2:
            return f'Rectangle (a={self.a}, b={self.b}, width={self.width}, height={self.height})'
        elif self.Figure_split==L1:
            return f'Circle (r={self.r})'
        elif self.Figure_split==L3:
            return f'Square (a={self.a},width={self.width},height={self.height})'

if Figure_split==L1:
    r=int(input('Введите радиус круга '))


if Figure_split==L2:
    a = int(input('Введите сторону а '))
    b = int(input('Введите сторону b '))
    width= int(input('Введите ширину '))
    height = int(input('Введите высоту '))

if Figure_split==L3:
    a = int(input('Введите сторону а '))
    width= int(input('Введите ширину '))
    height = int(input('Введите высоту '))

if Figure_split==L1:
    A=Geom_Figure(Figure_split,r)
if Figure_split==L2:
    A=Geom_Figure(Figure_split,a,b,width,height)
if Figure_split==L3:
    A=Geom_Figure(Figure_split,a,width,height)
print(A)




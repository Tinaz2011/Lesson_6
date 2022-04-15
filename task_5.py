class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'start paint


class Pen(Stationery):
    def draw(self):
        return f'start paint {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'start paint {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'start paint {self.title}'


pen = Pen('Pen')
print(pen.draw())
pencil = Pencil('Prncil')
print(pencil.draw())
handle = Handle('Marcker')
print(handle.draw())
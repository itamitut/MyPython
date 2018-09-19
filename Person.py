class Person:
    def __init__(self, n):
        self.name = n

    def __del__(self):
        print('До свидания, ' + self.name)


p1 = Person("Sam")
print(p1.name)
del p1


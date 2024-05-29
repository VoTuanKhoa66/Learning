class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

print(d.name)   
print(e.name)   

d.add_tricks('roll over')
e.add_tricks('play dead')

print(f'{d.name}\'s tricks : {d.tricks[0]}')
print(f'{e.name}\'s tricks : {e.tricks[0]}')



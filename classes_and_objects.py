class Person:
    def __init__(self, name='Daniel', age=19, networth=0.01, country='Colombia', city='Villavicencio'):
        self.name = name
        self.age = age
        self.networth = networth
        self.country = country
        self.city = city

    def print_info(self):
        print(f'This person: {self.name} who is {self.age} committed war crimes in afganistan in 2004, his current location is {self.country}. {self.city}')

    def change_name(self, name: str):
        self.name = name


p1 = Person()
p1.print_info()
p1.change_name('BRo')
p1.print_info()
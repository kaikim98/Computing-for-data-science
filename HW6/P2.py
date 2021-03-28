from P1 import Country # Do Not Modify

class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries
        
    def total_population(self):
        x = 0
        for i in self.countries:
            x += i.population
        return x
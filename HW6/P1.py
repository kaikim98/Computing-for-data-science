class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    
    def is_larger(self, other):
        print(self.area > other.area)
        
    def population_density(self):
        print(self.population / self.area)
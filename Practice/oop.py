from math import sqrt
class City:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = ""
    def find_closest_neighborhood(self, neighborhoods, name=""):
        min_distance = float("inf")
        closest = None
        for neighborhood in neighborhoods:
            distance = sqrt(((self.x - neighborhood.x) ** 2 + (self.y - neighborhood.y) ** 2))
            if distance < min_distance:
                min_distance = distance
                closest = neighborhood

        return closest, closest.name
    
    
class Neighborhood:
    def __init__(self, x, y, name):
        self.name = name
        self.neighborhoods = []
        self.x = x
        self.y = y
    

if __name__ == "__main__":
    city = City()
    city.x = 5
    city.y = 5
    n1 = Neighborhood(1, 2, "Downtown")
    n2 = Neighborhood(10, 10, "Uptown")
    n3 = Neighborhood(4, 4, "Midtown")
    neighborhoods = [n1, n2, n3]
    closest, name  = city.find_closest_neighborhood(neighborhoods)
    print(f"The closest neighborhood is at ({closest.x}, {closest.y})")
    print(f"Neighborhood name is: {name}")
    
from dataclasses import dataclass

@dataclass
class Place:
    name : str
    description : str
    city : str
    rating : float

    def __post_init__(self):
        if not isinstance(self.name, str) or not isinstance(self.description, str) or not isinstance(self.city, str):
            raise TypeError("Invalid input")
        if not isinstance(self.rating, (int , float)) or not (0 <=  self.rating  <= 5):
            raise TypeError("Invalid rating, must be between 0 - 5")
        
    def display_places(self):
        print(f"Name : {self.name}")
        print(f"Description : {self.description}")
        print(f"City : {self.city}")
        print(f"Ratings : {self.rating}")
    
def get_place_input():
    place_name = input("Enter name of place : ")
    place_description = input(f"Enter description of {place_name} : ")
    place_city = input("Enter city in which place is located : ")
    place_rating = float((input("Enter the rating of place : ")))
    # input is bydefault string, eror must be handled seperately
    return Place(place_name, place_description, place_city, place_rating)



place1 = get_place_input()
place1.display_places()
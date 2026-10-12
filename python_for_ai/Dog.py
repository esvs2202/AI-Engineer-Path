class Dog:
    def __init__(self, breed):
        self.breed = breed 

    def available_store_locations(self):
        d = {"Poodle": "Kukatpally store",
             "Pomerian": "Gachibowli store",
             "Golden retriever": "Secunderabad store",
             "Doberman": "Nampally store",
             "German shepherd": "Patancheruvu store",
             "Shitzu" : "LB Nagar store"}

        if d.get(self.breed) is not None:
         return f"These breeds are available in {d.get(self.breed)}"
        else:
           return f"These breeds are not available in any store"

breed_input = input("What breed of dog you are looking for ? ")

d = Dog(breed = breed_input)
print(d.available_store_locations())


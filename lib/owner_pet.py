class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type!")
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance!")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only Pet objects can be added.")
        pet.owner = self

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def get_sorted_pets(self):
        pets = self.pets()
        
        for pet in pets:
            if not isinstance(pet, Pet):
                raise Exception("All pets must be Pet instances.")
        
        sorted_pets = sorted(pets, key=lambda pet: pet.name)
        return sorted_pets

#Inheritance
class nonveg:
    favourite_food = 'Mutton biryani'

    def sweet(self):
        print("breed halwa")

class veg:
    favourite_food = 'Mushroom biryani'
    liked_food = 'Paneer tikka'

    def sweet(self):
        print('palkova')

class both(nonveg,veg):
    most_favourite = 'mandi'

both = both()
both.sweet()
print(both.favourite_food, both.liked_food, both.favourite_food,sep=",")
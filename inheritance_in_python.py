#parent class
class Room:
    def area(self,l,b):
        self.l=l
        self.b=b
        print(self.l*self.b)
#child class
class KitchenRoom(Room):
    def kitchenmsg(self):
        print("has slab and sink")


# r=Room()
# r.area(10,20)

r1=KitchenRoom()
r1.area(10,20)
r1.kitchenmsg()
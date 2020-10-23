import random as r
class User:
    def __init__(self):
        self.inventory = ['Map']
        self.health = 150
        self.battleReady = False
        self.poisoning = 5
    def pickup(self,room, item):

        if (item in room.contents):
            print("You now have", item)
            self.inventory.append(item)
            room.contents.remove(item)
            self.checkInventory()
            pass
        else:
            print("That item is not in this room")
            pass

    def drop(self, room,item):
        if item in self.inventory:
            print("You have dropped the", item)
            self.inventory.remove(item)
            if room.contents == None:
                room.contents = []
                room.contents.append(item)
            else:
                room.contents.append(item)
        else:
            print("You don't have that item")

    def listInventory(self):
        print("You are currently carrying:")
        if self.inventory == []:
            print("   nothing.")
        else:
            for i in range(len(self.inventory)):
                print("   ", self.inventory[i])
    def unlock(self,room,floorPlan,direction):
        def getAllLockStatus():
            rooms = ["Room1", "Room2", "Room3", "Room4", "Room5", "Room6", "Room7", "Room8",
                     "Room9", "Room10", "Room11", "Room12", "Room13", "Room14", "Room15",
                     "Room16", "Room17", "Room18"]

            for i in range(len(rooms)):
                if getattr(room,direction) == rooms[i]:

                    return floorPlan[i].keyRequired
                else:
                    pass
        if getAllLockStatus() in self.inventory:
            rooms = ["Room1", "Room2", "Room3", "Room4", "Room5", "Room6", "Room7", "Room8",
                     "Room9", "Room10", "Room11", "Room12", "Room13", "Room14", "Room15",
                     "Room16", "Room17", "Room18"]

            for i in range(len(rooms)):
                if getattr(room, direction) == rooms[i]:

                    floorPlan[i].lock = "Unlocked"
                    print("Unlocked!")
                else:
                    pass
    def attack(self,user_health):
        if self.battleReady == True:
            x = r.randint(5,25)
            y = r.randint(1,20)

            if y == 10:
                x = 35

            else:
                x = x
            return x
        else:
            print("You are unequipped for battle!")
    def checkInventory(self):
        if "Sword" in self.inventory:
            self.battleReady = True
        else:
            pass
    def use(self,item):
        if item == "Heart":
            self.health += 25
            self.inventory.remove(item)
        else:
            print("This item cannot be used right now")



class Room:
    def __init__(self, name, north, east, south, west, up, down,enemy, contents):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.enemy = enemy
        self.contents = contents


    def displayRoom(self):
        if self.name == None:
            pass
        else:
            print("Room name: ",self.name)
        if self.north == None:
            pass
        else:
            print("  Room to the north:  ",self.north)
        if self.east == None:
            pass
        else:
            print("  Room to the east:   ", self.east)
        if self.south == None:
            pass
        else:
            print("  Room to the south:  ", self.south)
        if self.west == None:
            pass
        else:
            print("  Room to the west:   ", self.west)
        if self.up == None:
            pass
        else:
            print("  Room above:         ", self.up)
        if self.down == None:
            pass
        else:
            print("  Room below:         ", self.down)
        print("  Room Contents:      ", self.contents)
        print("")
        
class Navigate:
    def __init__(self,RoomData):
        self.floorPlan = []
        for x in RoomData:
            singleRoom = []
            x = x.split(',')
            x[-1] = x[-1].strip()

            for i in range(8):

                if x[i] == 'None':
                    singleRoom.append(None)
                else:
                    singleRoom.append(eval(x[i]))

            if len(x) == 7:
                singleRoom.append([])
            else:
                itemList = []
                for i in range(8, len(x)):
                    itemList.append(eval(x[i]))

                singleRoom.append(itemList)
            self.floorPlan.append(Room(singleRoom[0],singleRoom[1],singleRoom[2],singleRoom[3],singleRoom[4],singleRoom[5],singleRoom[6],singleRoom[7],singleRoom[8]))

        self.current = self.floorPlan[0]
        self.inventory = ['Map']
    def look(self):
        print("You are currently in the",self.current.name +".")
        print("Contents of the room:")
        if self.current.contents == []:
            print("   None")

        else:
            for i in range(len(self.current.contents)):
                print("   ", self.current.contents[i])



    def move(self,direction):
        def getRoom(name):
            rooms = ["Room1","Room2","Room3","Room4","Room5","Room6","Room7","Room8",
                     "Room9","Room10","Room11","Room12","Room13","Room14","Room15",
                     "Room16","Room17","Room18"]
            for i in range(len(rooms)):
                if name == rooms[i]:

                    return self.floorPlan[i]
                else:
                    pass

        if direction == "north":
            if self.current.north == None:
                print("You can't move in that direction.")
                self.current = getRoom(self.current.name)
            else:
                print("You are now in the", self.current.north + ".")
                self.current = getRoom(self.current.north)
        elif direction == "east":
            if self.current.east == None:
                print("You can't move in that direction.")
                self.current = getRoom(self.current.name)
            else:
                print("You are now in the", self.current.east + ".")
                self.current = getRoom(self.current.east)
        elif direction == "south":
            if self.current.south == None:
                print("You can't move in that direction.")
                self.current = getRoom(self.current.name)
            else:
                print("You are now in the", self.current.south + ".")
                self.current = getRoom(self.current.south)
        elif direction == "west":
            if self.current.west == None:
                print("You can't move in that direction.")
                self.current = getRoom(self.current.name)
            else:
                print("You are now in the", self.current.west + ".")
                self.current = getRoom(self.current.west)
        elif direction == "up":
            if self.current.up == None:
                print("You can't move in that direction.")
                self.current = getRoom(self.current.name)
            else:
                print("You are now in the", self.current.up + ".")
                self.current = getRoom(self.current.up)
        elif direction == "down":
            if self.current.down == None:
                print("You can't move in that direction.")
                self.current = getRoom(self.current.name)
            else:
                print("You are now in the", self.current.down + ".")
                self.current = getRoom(self.current.down)

    def displayAllRooms(self):
        for i in range(len(self.floorPlan)):
                self.floorPlan[i].displayRoom()
    def pickup(self,item):

        if (item in self.current.contents):
            print("You now have", item)
            self.inventory.append(item)
            self.current.contents.remove(item)
            pass
        else:
            print("That item is not in this room")
            pass

    def drop(self,item):
        if item in self.inventory:
            print("You have dropped the",item)
            self.inventory.remove(item)
            if self.current.contents == None:
                self.current.contents = []
                self.current.contents.append(item)
            else:
                self.current.contents.append(item)
        else:
            print("You don't have that item")
    def listInventory(self):
        print("You are currently carrying:")
        if self.inventory == []:
            print("   nothing.")
        else:
            for i in range(len(self.inventory)):
                print("   ", self.inventory[i])

if __name__ == '__main__':
    RoomData = open('../text_files/Data.txt', 'r')
    game =Navigate(RoomData)
    game.look()
    running = True
    while running == True:

        x = input("Enter a command: ")
        if x == "help":
            print("look:        display the name of the current room and its contents")
            print("north:       move north")
            print("east:        move east")
            print("south:       move south")
            print("west:        move west")
            print("up:          move up")
            print("down:        move down")
            print("inventory:   list what items you're currently carrying")
            print("get <item>:  pick up an item currently in the room")
            print("drop <item>: drop an item you're currently carrying")
            print("help:        print this list")
            print("exit:        quit this game")
        elif x == "look":
            game.look()

        elif x == "north":
             game.move("north")

        elif x == "east":
             game.move("east")

        elif x == "south":
             game.move("south")

        elif x == "west":
             game.move("west")

        elif x == "up":
             game.move("up")

        elif x == "down":
            game.move("down")
        elif x == "inventory":
            game.listInventory()

        elif "get" in x:
            if x == "get":
                print("Item not specified")
                pass
            else:
                y = x.split()
                game.pickup(y[1])
                pass

        elif "drop" in x:
            if x == "drop":
                print("Item not specified")
                pass
            else:
                y = x.split()
                game.drop(y[1])
                pass
        elif x == "exit":
            print("Quitting game.")
            running = False

        else:
            print("Command not recognized")
        print("")





            

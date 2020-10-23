from Enemy import Enemy
class Room:
    def __init__(self, name, lock, key, north, east, south, west, up, down, enemy, contents):
        self.name = name
        self.lock = lock
        self.keyRequired = key
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.enemy = enemy
        self.contents = contents

class Navigate:
    def __init__(self, RoomData,EnemyData):
        self.floorPlan = []
        for x in RoomData:
            singleRoom = []
            x = x.split(',')
            x[-1] = x[-1].strip()

            for i in range(10):

                if x[i] == 'None':
                    singleRoom.append(None)
                else:
                    singleRoom.append(eval(x[i]))

            if len(x) == 10:
                singleRoom.append([])
            else:
                itemList = []
                for i in range(10, len(x)):
                    itemList.append(eval(x[i]))

                singleRoom.append(itemList)
            self.floorPlan.append(
                Room(singleRoom[0], singleRoom[1], singleRoom[2], singleRoom[3], singleRoom[4], singleRoom[5],
                     singleRoom[6], singleRoom[7], singleRoom[8],singleRoom[9],singleRoom[10]))

        self.current = self.floorPlan[0]
        self.EnemyPlan = []
        for x in EnemyData:
            singleEnemy = []
            x = x.split(',')
            x[-1] = x[-1].strip()

            for i in range(4):

                if x[i] == 'None':
                    singleEnemy.append(None)
                else:
                    singleEnemy.append(eval(x[i]))



            self.EnemyPlan.append(
                Enemy(singleEnemy[0], singleEnemy[1], singleEnemy[2], singleEnemy[3]))

    def displayAllRooms(self):
        for i in range(len(self.floorPlan)):
            self.floorPlan[i].displayRoom()

    def look(self):
        print("You are currently in the", self.current.name + ".")
        print("Contents of the room:")
        if self.current.contents == []:
            print("   None")

        else:
            for i in range(len(self.current.contents)):
                print("   ", self.current.contents[i])

    def move(self, direction):

        def getRoom(name):
            rooms = ["Room1", "Room2", "Room3", "Room4", "Room5", "Room6", "Room7", "Room8",
                     "Room9", "Room10", "Room11", "Room12", "Room13", "Room14", "Room15",
                     "Room16", "Room17", "Room18"]
            for i in range(len(rooms)):
                if name == rooms[i]:

                    return self.floorPlan[i]
                else:
                    pass

        def get_lockstatus(direction):
            rooms = ["Room1", "Room2", "Room3", "Room4", "Room5", "Room6", "Room7", "Room8",
                     "Room9", "Room10", "Room11", "Room12", "Room13", "Room14", "Room15",
                     "Room16", "Room17", "Room18"]
            for i in range(len(rooms)):
                if getattr(self.current,direction) == rooms[i]:

                    return self.floorPlan[i].lock
                else:
                    pass

        if getattr(self.current,direction) == None:
            print("You can't move in that direction!")

        else:
            if get_lockstatus(direction) == 'Unlocked':
                print("You are now in the", getattr(self.current, direction) + ".")
                self.current = getRoom(getattr(self.current, direction))

            elif get_lockstatus(direction) == "Locked":
                print("This room is locked!")
                self.current = getRoom(self.current.name)

    def detectEnemy(self):
        if self.current.enemy != None:
            enemies = ['BlubGlub','Torok','Soldier','Dragon']
            for i in range(len(enemies)):
                if self.current.enemy == enemies[i]:
                    return self.EnemyPlan[i]
                else:
                    pass
        else:
            pass
    def detectEnemyNextRoom(self,direction):
        rooms = ["Room1", "Room2", "Room3", "Room4", "Room5", "Room6", "Room7", "Room8",
                 "Room9", "Room10", "Room11", "Room12", "Room13", "Room14", "Room15",
                 "Room16", "Room17", "Room18"]
        for i in range(len(rooms)):
            if getattr(self.current, direction) == rooms[i]:

                return self.floorPlan[i].enemy
            else:
                pass


if __name__ == '__main__':
    RoomData = open('text_files/Data.txt', 'r')
    game = Navigate(RoomData)
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





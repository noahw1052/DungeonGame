#  File: Project2.py
#  Description: Prompts user to navigate through a map that contains various items
#  Student's Name: Noah Wright
#  Student's UT EID: NRW588
#  Course Name: CS 303E
#  Unique Number: 50180
#
#  Date Created: May 5,2020
#  Date Last Modified: May 6, 2020

class Room:
    def __init__(self, name, north, east, south, west, up, down,contents):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
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
        if self.contents == None:
            print("  Room Contents:       []")
            pass
        else:
            print("  Room Contents:      ", self.contents)
        print("")

def createRoom(roomData):
    R = Room(roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6],roomData[7])
    return R

def look():
    print("You are currently in the",current.name +".")
    print("Contents of the room:")
    if current.contents == None:
        print("   None")

    else:
        for i in range(len(current.contents)):
            print("   ", current.contents[i])

def getRoom(name):
    rooms = ["Living Room","Dining Room","Kitchen",
             "Upper Hall","Bathroom","Small Bedroom","Master Bedroom"]
    for i in range(0,7):
        if name == rooms[i]:

            return floorPlan[i]
        else:
            pass

def move(direction):
    if direction == "north":
        if current.north == None:
            print("You can't move in that direction.")
            return getRoom(current.name)
        else:
            print("You are now in the",current.north+".")
            return getRoom(current.north)
    elif direction == "east":
        if current.east == None:
            print("You can't move in that direction.")
            return getRoom(current.name)
        else:
            print("You are now in the",current.east+".")
            return getRoom(current.east)
    elif direction == "south":
        if current.south == None:
            print("You can't move in that direction.")
            return getRoom(current.name)
        else:
            print("You are now in the",current.south+".")
            return getRoom(current.south)
    elif direction == "west":
        if current.west == None:
            print("You can't move in that direction.")
            return getRoom(current.name)
        else:
            print("You are now in the",current.west+".")
            return getRoom(current.west)
    elif direction == "up":
        if current.up == None:
            print("You can't move in that direction.")
            return getRoom(current.name)
        else:
            print("You are now in the", current.up+".")
            return getRoom(current.up)
    elif direction == "down":
        if current.down == None:
            print("You can't move in that direction.")
            return getRoom(current.name)
        else:
            print("You are now in the",current.down+".")
            return getRoom(current.down)


def displayAllRooms():
    for i in range(len(floorPlan)):
        floorPlan[i].displayRoom()
def pickup(item):
    if item in current.contents:
        print("You now have", item)
        inventory.append(item)
        current.contents.remove(item)
        if current.contents == []:
            current.contents = None
        pass
    else:
        print("That item is not in this room")
def drop(item):
    if item in inventory:
        print("You have dropped the",item)
        inventory.remove(item)
        if current.contents == None:
            current.contents = []
            current.contents.append(item)
        else:
            current.contents.append(item)
    else:
        print("You don't have that item")
def listInventory():
    print("You are currently carrying:")
    if inventory == []:
        print("   nothing.")

    else:
        for i in range(len(inventory)):
            print("   ", inventory[i])



# add your code here

##########################################################################
###     All code below this is given to you.  DO NOT EDIT IT unless    ###
###     you need to adjust the indentation to match the indentation    ###
###     of the rest of your code.                                      ###
##########################################################################

def loadMap():
    global floorPlan
    RoomData = open('ProjectData.txt', 'r')
    floorPlan = []
    for x in RoomData:
        singleRoom = []
        x = x.split(',')
        x[-1] = x[-1].strip()

        for i in range(7):

                if x[i] == 'None':
                    singleRoom.append(None)
                else:
                    singleRoom.append(eval(x[i]))

        if len(x) == 7:
            singleRoom.append(None)
        else:
            itemList = []
            for i in range(7,len(x)):
                itemList.append(eval(x[i]))

            singleRoom.append(itemList)


        floorPlan.append(createRoom(singleRoom))



def main():
    global current  # make the variable "current" a global variable
    global inventory
    loadMap()


    # TEST CODE:  walk around the house
    current = floorPlan[0]  # start in the living room
    inventory = []
    look()

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
        if x == "look":
            look()
        if x == "north":
            current = move("north")
        if x == "east":
            current = move("east")
        if x == "south":
            current = move("south")
        if x == "west":
            current = move("west")
        if x == "up":
            current = move("up")
        if x == "down":
            current = move("down")
        if x == "inventory":
            listInventory()
        if "get" in x:
            x = x.split()
            pickup(x[1])
        if "drop" in x:
            x = x.split()
            drop(x[1])
        if x == "exit":
            print("Quitting game.")
            running = False

main()
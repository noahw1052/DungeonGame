from tkinter import *
import sys
from Navigation import Navigate
from User import *
import random as r

sys.path.append("/path/to/script/file/directory/")
RoomData = open('text_files/Data.txt', 'r')
EnemyData = open('text_files/enemies.txt', 'r')
game = Navigate(RoomData,EnemyData)
User = User()
class UserInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Adventure Game")
        self.window.geometry('650x400')
        self.moveButton1 = Button(self.window,text = 'North',command = lambda: self.move('north'))
        self.moveButton2 = Button(self.window, text='South ', command= lambda: self.move('south'))
        self.moveButton3 = Button(self.window, text='West', command= lambda: self.move('west'))
        self.moveButton4 = Button(self.window, text='East ', command= lambda: self.move('east'))
        self.moveButton5 = Button(self.window, text='Up ', command= lambda: self.move('up'))
        self.moveButton6 = Button(self.window, text='Down ', command= lambda: self.move('down'))
        self.lookButton = Button(self.window, text = "Look", command = lambda: self.look())
        self.text1 = Text(self.window)
        self.user_health = Label(self.window,text = "Health")
        self.user_health1 = Label(self.window,text = User.health)
        self.useButton = Button(self.window,text = "Use Item",command = lambda: self.use())


        global item
        item = StringVar(self.window)
        item.set("Pick an item")
        try:
            self.pickUpTab = OptionMenu(self.window,item,*game.current.contents).place(x=00, y=225, width = 200,height = 25)
        except TypeError:
            item.set("Pick an item")

        self.executePickUp = Button(self.window,text="Pick Up",command = lambda: self.get())

        global inventory
        inventory = StringVar(self.window)
        inventory.set("Inventory")
        self.listInventoryButton = Button(self.window,text="Show Inventory",command = lambda: self.inventory())
        try:
            self.dropTab = OptionMenu(self.window,inventory, *User.inventory).place(x = 00 , y = 250, width = 200,height = 25)
        except TypeError:
            pass
        self.executeDrop= Button(self.window,text = "Drop Item",command =lambda: self.dropp())

#Layout

        self.moveButton1.place(x = 500, y = 200,width = 75,height = 25)
        self.moveButton2.place(x = 500, y = 250,width = 75,height = 25)
        self.moveButton3.place(x = 450, y = 225,width = 75,height = 25)
        self.moveButton4.place(x = 550, y = 225,width = 75,height = 25)
        self.moveButton5.place(x = 500, y = 275,width = 75,height = 25)
        self.moveButton6.place(x = 500, y = 300,width = 75,height = 25)
        self.lookButton.place(x = 475, y = 165,width = 125,height = 25)
        self.text1.place(x = 125,y = 000, width = 400, height = 150)
        self.user_health.place(x = 125, y = 175, width = 50)
        self.user_health1.place(x = 175,y = 175)
        self.useButton.place(x = 275, y = 225,width = 125,height = 25)
        self.executePickUp.place(x = 200, y = 225,width = 75,height = 25)

        self.executeDrop.place(x = 200, y =250,width = 75,height = 25)
        self.listInventoryButton.place(x = 275, y = 250,width = 125,height = 25)
#Display Console
        self.add_timestamp()
    def refresh_health(self):
        self.user_health = Label(self.window,text = "Health")
        self.user_health1 = Label(self.window,text = User.health)
        self.user_health.place(x = 125, y = 175, width = 50)
        self.user_health1.place(x = 175,y = 175)
    def add_timestamp(self):
        self.text1.see("end")
        self.text1.after(1000, self.add_timestamp)
    def run_script(self):
        sys.stdout = self
        try:
            del (sys.modules["Navigation"])
        except:
            pass
        import Navigation
        return Navigation
        sys.stdout = sys.__stdout__
    def write(self, txt):
        self.text1.insert(INSERT, txt)
    def flush(self):
        pass

#Button Commands
    def use(self):
        User.use(inventory.get())
        self.refresh_health()
        self.refreshOptionMenus()
    def look(self):
        game.look()
    def move(self,direction):
        self.refresh_health()
        User.unlock(game.current,game.floorPlan, direction)

        if game.detectEnemyNextRoom(direction) != None:
            if User.battleReady == True:
                game.move(direction)
                if game.detectEnemy() != None:
                    self.battleon()
                else:
                    pass
            else:
                print("You cannot go in there! You are not equipped for battle!")
        else:
            game.move(direction)


        item = StringVar(self.window)
        item.set("Pick an item")
        self.refreshOptionMenus()
    def battleon(self):
        BattleTime = Battle()
        BattleTime.window.mainloop
        self.refresh_health()
    def refreshOptionMenus(self):
        try:
            self.pickUpTab = OptionMenu(self.window,item,*game.current.contents).place(x = 00 , y = 225 ,width = 200,height = 25)
            item.set("Pick an item")
        except TypeError:
            item.set("Pick an item")
        try:
            self.dropTab= OptionMenu(self.window,inventory, *User.inventory).place(x = 00 , y = 250, width = 200,height = 25)
            inventory.set("Inventory")
        except TypeError:
            inventory.set("Inventory")
    def inventory(self):
        User.listInventory()
    def get(self):
        User.pickup(game.current,item.get())
        self.refreshOptionMenus()


    def dropp(self):
        User.drop(game.current,inventory.get())
        self.refreshOptionMenus()
class Battle():

    def __init__(self):
        Enemy = game.detectEnemy()
        self.battlestatus = True
        self.window = Tk()
        self.window.title('Battle')
        self.window.geometry('300x300')
        self.listbox = Listbox(self.window)
        self.attackButton = Button(self.window,text = 'Attack', command = self.attack)
        self.user_health = Label(self.window,text = "Health")
        self.user_health1 = Label(self.window,text = User.health)
        self.enemy_health = Label(self.window, text="Enemy Health")
        self.enemy_health1 = Label(self.window, text=int(Enemy.health))
        self.listbox.place(x=0,y=0,width=300,height=150)
        self.attackButton.place(x=0,y=175,width=100,height=25)
        self.user_health.place(x=50, y=150, width=50)
        self.user_health1.place(x=100, y=150)
        self.enemy_health.place(x=150, y=150, width=75)
        self.enemy_health1.place(x=225, y=150)
        self.add_timestamp()
        self.listbox_insert('A '+Enemy.name+' appears')
        if "Bow and Arrow" in User.inventory:
            self.bowButton = Button(self.window,text = 'Bow and Arrow', command = lambda : self.bowandarrow())
            self.bowButton.place(x=200,y=175,width =100,height = 25)
        if "Boomerang" in User.inventory:
            self.boomerangButton = Button(self.window,text = "Boomerang",command = lambda: self.boomerang())
            self.boomerangButton.place(x=0,y =200,width = 100,height =20)
    def update_healthbar(self):
        Enemy = game.detectEnemy()
        self.user_health = Label(self.window,text = "Health")
        self.user_health1 = Label(self.window,text = User.health)
        self.enemy_health = Label(self.window, text="Enemy Health")
        self.enemy_health1 = Label(self.window, text=int(Enemy.health))
        self.attackButton.place(x=0,y=175,width=100,height=25)
        self.user_health.place(x=50, y=150, width=50)
        self.user_health1.place(x=100, y=150)
        self.enemy_health.place(x=150, y=150, width=75)
        self.enemy_health1.place(x=225, y=150)
    def endBattle(self):
        self.window.destroy()
    def add_timestamp(self):
        self.listbox.see("end")
        self.listbox.after(500, self.add_timestamp)
    def listbox_insert(self, item):
        self.listbox.insert(END, item)
    def checkEndGame(self):
        Enemy = game.detectEnemy()
        if User.health <= 0:
            gui.window.destroy()
            self.window.destroy()

        if Enemy.health <= 0:
            self.window.destroy()
            print('You won the battle!')
            Enemy.health = Enemy.original_health
            if game.current.enemy == "Dragon":
                print("You've saved princess Sofia from the wrath of the evil dragon")
                print("An era of peace has been restored to the kingdom")
            game.current.enemy = None
        gui.refresh_health()
    def attack(self):
        Enemy = game.detectEnemy()
        if Enemy.awake == "Awake":
            y = Enemy.attack()
            self.listbox_insert('You took ' + str(y) + ' damage!')
            User.health -= y
            if "Shield" in User.inventory:
                p = r.randint(1, 5)
                if p == 3:
                    y = 0
                    self.listbox_insert("Your shield blocked the hit!")
                else:
                    pass
        else:
            pass
        if Enemy.awake == "Asleep":
            self.listbox_insert('The enemy is stunned it cannot attack!')
        x = User.attack(Enemy.health)
        Enemy.awake = "Awake"
        self.listbox_insert('The enemy took '+str(x)+' damage!')
        Enemy.health -= x
        self.update_healthbar()
        self.checkEndGame()
    def boomerang(self):
        Enemy = game.detectEnemy()
        p = r.randint(1,7)
        if p in [1,4,7]:
            self.listbox_insert("The boomerang missed!")
            y = Enemy.attack()
            if "Shield" in User.inventory:
                b = r.randint(1, 5)
                if b == 3:
                    y = 0
                    self.listbox_insert("Your shield blocked the hit!")
                else:
                    pass
            self.listbox_insert('You took ' + str(y) + ' damage!')
            User.health -= y
        else:
            Enemy.awake = "Asleep"
            self.listbox_insert("The Enemy has been stunned")
        self.update_healthbar()
        self.checkEndGame()
    def bowandarrow(self):
        Enemy = game.detectEnemy()
        p = r.randint(1,8)
        if p in [1,2,3]:
            self.listbox_insert('Your arrow missed')
            pass
        else:
            y = 20
            Enemy.health -= y
            self.listbox_insert('The enemy took ' + str(y) + ' damage!')
        y = Enemy.attack()
        self.listbox_insert('You took ' + str(y) + ' damage!')
        User.health -= y
        self.update_healthbar()
        self.checkEndGame()

gui = UserInterface()
gui.run_script()

game.look()
gui.window.mainloop()
if User.health <= 0:
    root = Tk()
    photo = PhotoImage(file ="images/gameover.gif")
    label = Label(image = photo)
    label.pack()
    root.mainloop()




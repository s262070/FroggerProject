from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='blue')
Grass = drawpad.create_rectangle(0,250,800,600, fill="green")
Road = drawpad.create_rectangle(0,425,800,525, fill="grey")
car1 = drawpad.create_rectangle(350,465,400,490, fill="red")
car2 = drawpad.create_rectangle(350,435,400,460, fill="red")
player = drawpad.create_oval(390,580,410,600, fill="Purple")
bug = drawpad.create_rectangle(350,300,400,330, fill="brown")

direction = 3
direction = -3
fast = 3


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()






    def collisionDetect(self, player):
        global car1
        global car2
        global bug
        px1,py1,px2,py2 = drawpad.coords(player)
        c1x1,c1y1,c1x2,c1y2 = drawpad.coords(car1)
        c2x1,c2y1,c2x2,c2y2 = drawpad.coords(car2)
        bx1,by1,bx2,by2 = drawpad.coords(bug)

        if (px1 > c1x1 and px2 < c1x2)and(py1 < c1y1 and py2 > c1y2):
            print hit

    
    def animate(self):
        global drawpad
        global enemy
        global fast
        global direction
        x1,y1,x2,y2 = drawpad.coords(car1)
        px1,py1,px2,py2 = drawpad.coords(player)

        if x2 > 800:
            direction = - 3
        elif x1 < 0:
            direction = 3
        drawpad.move(car1, direction, 0)
        drawpad.after(5,self.animate)
        x1,y1,x2,y2 = drawpad.coords(car2)
        if x2 > 800:
            fast = - 3
        elif x1 < 0:
            fast = 3
        drawpad.move(car2, fast, 0)
        x1,y1,x2,y2 = drawpad.coords(bug)
        if x2 > 800:
            fast = - 3
        elif x1 < 0:
            fast = 3
        drawpad.move(bug, fast, 0)
        collisionDetect
            

    def key(self,event):
        global drawpad
        global player
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 <= 0:
                drawpad.move(player,0,20)
            else: 
                drawpad.move(player,0,-20)
        if event.char == "s":
            if y2 >= 600:
                drawpad.move(player,0,0)
            else: 
                drawpad.move(player,0,20)
        if event.char == "d":
            if x2 >= 800:
                drawpad.move(player,0,0)
            else: 
                drawpad.move(player,20,0)
        if event.char == "a":
            if x1 <= 0:
                drawpad.move(player,0,0)
            else: 
                drawpad.move(player,-20,0)
                

            
    





            
app = myApp(root)
root.mainloop()
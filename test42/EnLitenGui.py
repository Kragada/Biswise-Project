from tkinter import *

class Application(Frame):
    def _init_(self, master):
        self.master = master
    def create_widgets(self):
        btn1 = Button(self.master, text = "Carlis")
        btn1.pack()
        btn2 = Button(self.master, command=self.buttonClickRickard, text = "Rickard")
        btn2.pack()
        btn3=Button(self.master, text = "Eric")
        btn3.pack()
        btn4=Button(self.master, text = "Anton")
        btn4.pack()

    def buttonClickRickard(self):
        print("Rickard")
        import pong


root = Tk()
root.title("Gui menu")
root.geometry("200x200")
app = Application(root)
#call the method
app.create_widgets()
root.mainloop()
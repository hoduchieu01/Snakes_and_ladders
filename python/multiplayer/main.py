from userInterface import *

def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("850x600")
    img = PhotoImage(file ="UI.gif")

    x = Display(master,img)
    master.mainloop()

main()

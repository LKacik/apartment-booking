from tkinter import Tk, Button


def click_action(button):
    button.config(text=f"funkcja reservation")

root = Tk()
root.title('Rezerwacja Mieszkania')
root.geometry("800x600")
root.mainloop()

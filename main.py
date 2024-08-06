import tkinter as tk
from Model import ContactModel
from View import ContactView
from Controller import ContactController

if __name__ == "__main__":
    root = tk.Tk()
    model = ContactModel()
    view = ContactView(root)
    controller = ContactController(model, view)
    root.mainloop()

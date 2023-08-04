import tkinter as tk

class MainPage:
    def __init__(self, mainroot):
        root = mainroot

        label = tk.Label(root, text="Hello, Tkiter")
        label.pack()
        label1 = tk.Label(root, text="Hello, Tkiter")
        label1.pack()
        button = tk.Button(root, text="click me!", command=lambda: print("button clicked"))
        mainroot.mainloop()
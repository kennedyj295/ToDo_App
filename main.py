import tkinter as tk
root = tk.Tk()

label = tk.Label(root, text="Hello, Tkiter")
label.pack()
button = tk.Button(root, text="click me!", command=lambda: print("button clicked"))
root.mainloop()
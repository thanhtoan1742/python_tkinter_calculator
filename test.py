import tkinter as tk

root = tk.Tk()
root.bind('<Key>', lambda e: print(ord(e.char)))
root.mainloop()
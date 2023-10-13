import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter", background='green', foreground='azure1', height=10, width=10)
greeting.pack()
test = tk.Button(text='click me')
test.pack()
window.mainloop()


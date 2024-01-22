import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text = 'Hello, world!',
                   foreground = 'blue',
                    width = 20,
                    height = 20)
greeting.pack()

window.mainloop()

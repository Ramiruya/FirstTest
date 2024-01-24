import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text = 'Hello, world!',
                   foreground = 'blue',
                    width = 20,
                    height = 20)
button = tk.Button(
    text = 'покакать',
    width = 25,
    height = 5,
    bg = 'green',
    fg = 'red',
    )
button.pack()
greeting.pack()

window.mainloop()

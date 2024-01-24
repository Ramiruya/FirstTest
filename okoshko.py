import tkinter as tk
window = tk.Tk()
window.title('pokakat?')
window.geometry('500x500')
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
button.grid(row = 2, column=3)
greeting.grid(row = 1, column=3)

window.mainloop()

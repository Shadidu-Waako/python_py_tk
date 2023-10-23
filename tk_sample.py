import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(background="Light Blue")
window.title("simple addition")
window.geometry("165x200")

def add():
  x = int(textbox1.get()) + int(textbox2.get())
  textbox3.delete(0, tk.END)
  textbox3.insert(0, string=x)

label1 = ttk.Label(window, text="Enter the numbers to add", padding=5)
label1.place(x=0, y=87)

textbox1 = ttk.Entry(window, textvariable=int, background="white", justify="left", width=8)
textbox1.grid(row=2, column=0)

plus = ttk.Label(window, text="plus", font="bold", justify="left", padding=5)
plus.grid(row=2, column=1)

textbox2 = ttk.Entry(window, textvariable=int, background="white", justify="left", width=8)
textbox2.grid(row=2, column=2)

equal = ttk.Button(window, text=" = ",command=add, padding=5, width=3)
equal.grid(row=3, column=1)

textbox3 = ttk.Entry(window, textvariable=int, background="white", justify="left", width=8)
textbox3.grid(row=4, column=1)


window.mainloop()

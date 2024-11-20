import tkinter as tk


def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.geometry("400x500")
root.title("Calculator MADE IN NAHIYAN ALAM")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10, )

button_frame = tk.Frame(root)
button_frame.pack()

button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 1, 0
buttons = []

for label in button_labels:
    button = tk.Button(button_frame, text=label, font="lucida 15 bold", height=2, width=5)
    button.grid(row=row, column=col, padx=10, pady=10)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1

for button in buttons:
    button.bind("<Button-1>", click)

root.mainloop()

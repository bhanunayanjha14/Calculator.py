from tkinter import *

# ------------------ Functions ------------------

def click(event):
    """This function handles button click events."""
    global scvalue
    text = event.widget.cget("text")   # Get text of clicked button

    if text == "=":
        try:
            # Evaluate the expression and update screen
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")   # Clear screen
    else:
        # Add clicked button text to screen value
        scvalue.set(scvalue.get() + text)

# ------------------ Main Window ------------------

root = Tk()
root.geometry("400x550")
root.title("Calculator - Bhanu")

# ------------------ Screen ------------------

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 25 bold", bg="#EBE8E8", fg="black")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# ------------------ Button Frames ------------------

button_frame = Frame(root)
button_frame.pack()

# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

# ------------------ Create Buttons Dynamically ------------------

for row in buttons:
    frame = Frame(button_frame)
    frame.pack()
    for text in row:
        b = Button(frame, text=text, font="lucida 15 bold", relief=RIDGE, height=2, width=6)
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()

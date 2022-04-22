import tkinter as tk
import tkinter.messagebox as tkmb
import math

def click_button(event):
    btn = event.widget
    # tkmb.showinfo("", f"{btn['text']}のボタンがクリックされました")
    entry.insert(tk.END, btn["text"])

def click_equal(event):
    btn = event.widget
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def click_sqrt(event):
    btn = event.widget
    eqn = entry.get()
    res = math.sqrt(eval(eqn))
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x450")
    entry = tk.Entry(root, justify="right", width="10", font=("Times New Roman", 40))
    entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

    r, c = 1, 0
    for i, num in enumerate(["7","8","9","4","5","6","1","2","3","0","+"]):
        btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30))
        btn.bind("<1>", click_button)
        if i%3 == 0:
            r, c = r+1, 0
        btn.grid(row=r, column=c, padx=10, pady=10)
        c += 1
    btn = tk.Button(root, text="=", font=("Times New Roman", 30))
    btn.bind("<1>", click_equal)
    btn.grid(row=5, column=2, padx=10, pady=10)

    btn = tk.Button(root, text="√", font=("Times New Roman", 30))
    btn.bind("<1>", click_sqrt)
    btn.grid(row=5, column=3, padx=10, pady=10)

    root.mainloop()

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

def click_clear_one(event):
    eqn = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, eqn[:-1])

def click_clear_all(event):
    entry.delete(0, tk.END)

def click_sqrt(event):
    btn = event.widget
    eqn = entry.get()
    res = math.sqrt(eval(eqn))
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("430x520")
    entry = tk.Entry(root, justify="right", width="15", font=("Times New Roman", 40))
    entry.grid(row=0, column=0, padx=5, pady=10, columnspan=4)

    r, c = 1, 0
    for i, num in enumerate(["7","8","9","÷","4","5","6","×","1","2","3","-","0",".","+"]):
        btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30))
        btn.bind("<1>", click_button)
        if i%4 == 0:
            r, c = r+1, 0
        btn.grid(row=r, column=c, padx=5, pady=10)
        c += 1
    btn = tk.Button(root, text="=", font=("Times New Roman", 30))
    btn.bind("<1>", click_equal)
    btn.grid(row=5, column=3, padx=5, pady=10)

    btn = tk.Button(root, text="C", font=("TImes New Roman", 30))
    btn.bind("<1>", click_clear_one)
    btn.grid(row=6, column=0, padx=10, pady=10)

    btn = tk.Button(root, text="AC", font=("TImes New Roman", 30))
    btn.bind("<1>", click_clear_all)
    btn.grid(row=6, column=1, padx=10, pady=10)
    
    btn = tk.Button(root, text="√", font=("Times New Roman", 30))
    btn.bind("<1>", click_sqrt)
    btn.grid(row=5, column=3, padx=10, pady=10)

    root.mainloop()

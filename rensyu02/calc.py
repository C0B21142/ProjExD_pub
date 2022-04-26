import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x450")

    r, c = 0, 1
    for i, num in enumerate(range(9, -1, -1), 1):
        btn = tk.Button(root, text=num, font=("Times New Roman", 30))
        btn.grid(row=r, column=c)
        if i%3 == 0:
            r += 1
            c = 0
        c += 1
        
    root.mainloop()
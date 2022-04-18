import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("300x450")
    frm = tk.Frame(root)
    
    buttons = []
    for i in range(9, -1, -1):
        btn = tk.Button(root, text=f"{i}", font=("Times New Roman", 30))
        buttons.append(btn)
    r, c = 0, 0
    for i, btn in enumerate(buttons):
        if i%3 == 0:
            r, c = r+1, 0
        btn.grid(row=r, column=c, padx=10, pady=10)
        c += 1
    root.mainloop()

if __name__ == "__main__":
    main()

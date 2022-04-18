import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("300x450")
    buttons = []
    for i in range(10):
        btn = tk.Button(root, text=f"{i}", font=("Times New Roman", 30))
        buttons.append(btn)
    for btn in buttons:
        btn.pack()
    root.mainloop()

if __name__ == "__main__":
    main()

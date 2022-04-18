import tkinter as tk
import tkinter.messagebox as tkmb

def click_button(event):
    btn = event.widget
    # tkmb.showinfo("", f"{btn['text']}のボタンがクリックされました")
    entry.insert(tk.END, btn["text"])


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x450")
    entry = tk.Entry(root, justify="right", width="10", font=("Times New Roman", 40))
    entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

    buttons = []
    for i in range(9, -1, -1):
        btn = tk.Button(root, text=f"{i}", font=("Times New Roman", 30))
        btn.bind("<1>", click_button)
        buttons.append(btn)
    r, c = 1, 0
    for i, btn in enumerate(buttons):
        if i%3 == 0:
            r, c = r+1, 0
        btn.grid(row=r, column=c, padx=10, pady=10)
        c += 1
    root.mainloop()

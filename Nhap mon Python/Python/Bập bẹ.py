import tkinter as tk

root = tk.Tk()
def show_text():
    print(entry.get())
    
text = tk.Text(root, height=5, width=30)
text.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Lấy dữ liệu", command=show_text)
btn.pack()

root.mainloop()
import tkinter as tk
r = tk.Tk()
r.geometry("480x480")
r.title('Image Processing Assistant')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
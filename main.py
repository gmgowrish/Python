import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    for widgets in frame.winfo_children():
        widgets.destroy()

    filename = filedialog.askopenfile(initialdir="/", title="Select File",
                                      filetypes=(("ececutables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def run_apps():
    for app in apps:
        os.system(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="openfile", padx=10
                     , pady=5, fg="white", bg="#263D42", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="run Apps", padx=10
                    , pady=5, fg="white", bg="#263D42",command=run_apps)

runApps.pack()

root.mainloop()

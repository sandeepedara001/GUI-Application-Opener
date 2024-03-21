import tkinter as tk
from tkinter import filedialog, Text
import os

root=tk.Tk() # The main root element

apps=[]
folders=[]
if os.path.isfile("save.txt"): # If we have previous history of selected files and folders then loading them to 'apps' variable
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps=tempApps.split(",")
        apps = [app for app in tempApps if app.strip()]

def addApp(): # Function for adding the files

    for widget in frame.winfo_children(): # For destroying the redundancy in the file names, which if not mentioned would append the file name multiple times
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/", title="Select File",
                    filetypes=(("execuatables", "*.exe"),("all files", "*.*"))) # Asking for a file name to open and the exact location will be in the variable
    apps.append(filename)
    for app in apps:
        label=tk.Label(frame, text=app, background="gray") # Fetching the name of the file
        label.pack() # Attaching it to the frame



def addFolder(): # For adding the folders

    for widget in frame.winfo_children():
        widget.destroy()

    foldername=filedialog.askdirectory(initialdir="/", title="Select Folder")
    apps.append(foldername)
    for folder in apps:
        label=tk.Label(frame, text=folder, background="gray")
        label.pack()



def runApps(): # Running the apps
    for app in apps:
        os.startfile(app)


canvas=tk.Canvas(root, height=500, width=500, bg='#263D42') # Attaching canvas
canvas.pack() # attatching it to the root

frame=tk.Frame(root, bg='white') # Adding another container inside using frame
frame.place(relwidth=0.8, relheight=0.7, relx=0.1,rely=0.1) # Used for specifying the position. relx, rely are used for centering it

openFile=tk.Button(root, text='Open file', padx=10, pady=5, fg='white', bg='#263D42', command=addApp) # Adding a button for opening files
openFile.pack() # Attaching to the root

openFolder=tk.Button(root, text='Open Folder', padx=10, pady=5, fg='white', bg='#263D42', command=addFolder) # Another button for opening folders
openFolder.pack() # Attaching to the root

runApps=tk.Button(root, text='Run Apps', padx=10, pady=5, fg='white', bg='#263D42', command=runApps) # Button for running the apps
runApps.pack()

for app in apps: # For attaching the previously opened apps to the root
    label=tk.Label(frame, text=app)
    label.pack()

root.mainloop() # To run it



with open("save.txt", "w") as f: # For storing the file and folder names in a file
    for app in apps:
        f.write(app + ",")

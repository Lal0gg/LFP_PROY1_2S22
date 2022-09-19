
from tkinter import filedialog
import tkinter
from tkinter.filedialog import asksaveasfile


global filpathh
global scroll1
filpathh = filedialog.asksaveasfile(title='Guardar Archivo',filetypes = (("LFP files", "*.lfp*"), ("Text Files","*.txt"),("all files", "*.*")))
try: 
    file = open(filpathh,'w',encoding="utf-8")
    file.write("hola mundo")
    file.close()
    tkinter.messagebox.showinfo("GUARDAR", "Se sobrescribió el archivo :D")
except Exception as e:
    pass
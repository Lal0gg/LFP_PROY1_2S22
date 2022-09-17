import tkinter
from  tkinter import *
import tkinter as tk
from tkinter import BOTTOM, Menu, Scrollbar, Tk, XView, font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from scanner import Scanner



#Variables globales
wnd_menu = None #ventana menu
scroll1 =None
file = "" #contenedor del archivo a analizar


def window_mainMenu():
    global wndw_menu
    global scroll1
    #Configuración ventana menu principal
    wndw_menu = tkinter.Tk()
    wndw_menu.title("App-Scanner")
    wndw_menu.resizable(0,0)
    wndw_menu.geometry("1080x720")
    wndw_menu.config(bg="#E4E3FF")
    wndw_menu.config(bd=30)

    SubMenu= Menu(wnd_menu,selectcolor="green")
    wndw_menu.config(menu=SubMenu)

    #Items del menú1
    file_menu = Menu(SubMenu,tearoff=0)
    SubMenu.add_cascade(label="Archivo",menu=file_menu)
    file_menu.add_command(label="Abrir",command=openfile,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Guardar",command=savefile,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Guardar Como",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Analizar",command=scanner,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Errores",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Salir",font=("Courier 10 bold"),background="#E4E3FF",command=wndw_menu.quit)
    #Items del menú2
    help_menu= Menu(SubMenu,tearoff=0)
    SubMenu.add_cascade(label="Ayuda",menu=help_menu)
    help_menu.add_command(label="Manual de Usuario",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    help_menu.add_separator()
    help_menu.add_command(label="Manual Técnico",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    help_menu.add_separator()
    help_menu.add_command(label="Temas de Ayuda",command=datau,font=("Courier 10 bold"),background="#E4E3FF")
    
    scroll1 = scrolledtext.ScrolledText(wndw_menu, width =60, height=40,font=('Courier', 10),wrap=WORD)
    scroll1.place(x=0,y=10)
    scroll1.focus()

    scroll2 = scrolledtext.ScrolledText(wndw_menu, width =60, height=40, font=('Courier', 10),wrap = WORD)
    scroll2.place(x=515,y=10)
    scroll2.focus()

    wndw_menu.mainloop()

def our_command():
    print("Hola Mundo")

def datau():
    mensaje=messagebox.showinfo("Datos"," Curso: Lenguajes Formales y de Programación\n Nombre: Eduardo Josué González Cifuentes\n Carnet: 201900647 \n Sección: A-")


def openfile():
    global filepath
    global file
    global scroll1
    try:
        filepath = filedialog.askopenfilename()
        file = open(filepath,'r',encoding="utf-8")
        contenido=file.read()
        print(file.read())
        scroll1.insert(tk.INSERT,contenido)
        file.close()
    except:
        pass

def savefile():
    global filepath
    global file
    try: 
        file = open(filepath,'w',encoding="utf-8")
        file.write("hola buenas :v")
        file.close()
    except:
        pass

def scanner():
    global filepath
    global file
    global scroll1
    contenido1 = scroll1.get(1.0,END)
    ScannerGG = Scanner()
    ScannerGG.analyze(contenido1)
    ScannerGG.printScannergg()


window_mainMenu()
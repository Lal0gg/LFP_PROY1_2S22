from ast import Sub
from tkinter import *
import tkinter
from tkinter import font


#Variables Ventanas
wnd_menu = None

def window_mainMenu():
    global wndw_menu
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
    file_menu.add_command(label="Abrir",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Guardar",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Guardar Como",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Analizar",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")
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
    help_menu.add_command(label="Temas de Ayuda",command=our_command,font=("Courier 10 bold"),background="#E4E3FF")

    wndw_menu.mainloop()

def our_command():
    print("Hola Mundo")

window_mainMenu()
import tkinter
from  tkinter import *
import tkinter as tk
from tkinter import BOTTOM, Menu, Scrollbar, Tk, XView, font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from scanner import Scanner
from Clases import Error,Token
from reporteEr import *



#Variables globales
wnd_menu = None #ventana menu
scroll1 =None
file = "" #contenedor del archivo a analizar
bandera = False
fielpath =""
ScannerGG = Scanner()

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
    file_menu.add_command(label="Guardar Como",command=saveas,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Analizar",command=scanner,font=("Courier 10 bold"),background="#E4E3FF")
    file_menu.add_separator()
    file_menu.add_command(label="Errores",command=report,font=("Courier 10 bold"),background="#E4E3FF")
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
    scroll2.configure(state='disabled')
    scroll2.focus()

    wndw_menu.mainloop()

def our_command():
    print("Hola Mundo")

def datau():
    mensaje=messagebox.showinfo("Datos"," Curso: Lenguajes Formales y de Programación\n Nombre: Eduardo Josué González Cifuentes\n Carnet: 201900647 \n Sección: A-")


def openfile():
    global file
    global scroll1
    global bandera
    global filpathh
    filpathh = filedialog.askopenfilename(title='Abrir Archivo',filetypes = (("LFP files", "*.lfp*"), ("Text Files","*.txt"),("all files", "*.*")))
    try: 
        if filpathh != "":
            if(bandera==False):
                file = open(filpathh,'r',encoding="utf-8")
                contenido=file.read()
                scroll1.insert(tk.INSERT,contenido)
                print(contenido)
                file.close()
                bandera = True                
                tkinter.messagebox.showinfo("ALERTA", "Se cargo el araachivo exitosamente")
            else:
                tkinter.messagebox.showinfo("ERROR", "Ya se cargó  este archivo")
                
        else:
            tkinter.messagebox.showinfo("ERROR", "No se cargó ningún archivo")
        
    except:
        pass

def report():
    global ScannerGG
    generararchivoE(ScannerGG.listaErrores,ScannerGG.listaTokens)



def savefile():
    global filpathh
    global scroll1
    contenido1 = scroll1.get(1.0,tkinter.END)
    try: 
        file = open(filpathh,'w',encoding="utf-8")
        file.write(contenido1)
        file.close()
        tkinter.messagebox.showinfo("GUARDAR", "Se sobrescribió el archivo :D")
    except Exception as e:
        pass

def saveas():
    global scroll1
    contenido2= scroll1.get(1.0,tkinter.END)
    filegg = filedialog.asksaveasfilename(title='Guardar Archivo',filetypes = (("LFP files", "*.lfp*"), ("Text Files","*.txt"),("all files", "*.*")))
    try: 
        file = open(filegg,'w',encoding="utf-8")
        file.write(contenido2)
        file.close()
        tkinter.messagebox.showinfo("GUARDAR", "Se guard un nuevo archivo :D")
    except Exception as e:
            print(e)


def scanner():
    global filepath
    global file
    global scroll1
    global ScannerGG
    contenido1 = scroll1.get(1.0,tkinter.END)
    if contenido1 != "":
        ScannerGG.analyze(contenido1)
        ScannerGG.printScannergg()
    else:
        tkinter.messagebox.showinfo("ERROR", "No se puede analizar")

window_mainMenu()
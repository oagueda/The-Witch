import subprocess
from tkinter import *
from tkinter import ttk
from TheWitchUsuarios import mainUsuarios
from TheWitchGrupos import mainGrupos
from TheWitchCarpetas import mainCarpetas
path = "Ayuda The Witch.pdf"
class Aplicacion:
    def __init__(self):
        root = Tk()
        root.configure()
        root.title('The Witch')
        root.iconbitmap('./lol.ico')
        root.resizable(width=False,height=False)
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")
        root.pantalla = Text(root,font=("Sans Sheriff", 15),height = 11, width = 21)
        root.pantalla.grid(rowspan=5,column=1,sticky=EW,padx=15,pady=15,)
        root.pantalla.insert("1.0","Bienvenido a The Witch! \n\nThe Witch es un \nprograma diseñado para ayudarte con la creación de Usuarios para tu \nWindows Server.\n\nSe recomienda pulsar el \nbotón de ayuda para \naprender a usar el \nprograma.")
        root.pantalla.configure(state='disabled')
        root.button = ttk.Button(root, text='Salir', command=root.destroy)
        root.button.grid(column=2,row=4,sticky=EW,padx=15,pady=15)
        root.button1 = ttk.Button(root, text="Generar Usuarios", command=lambda:[mainUsuarios()])
        root.button1.grid(column=2,row=0,sticky=EW,padx=15,pady=15)
        root.button2 = ttk.Button(root, text="Configurar Generador", command=lambda:[])
        root.button2.grid(column=2,row=1,sticky=EW,padx=15,pady=15)
        root.button4 = ttk.Button(root, text="Ayuda", command=lambda:[subprocess.Popen([path], shell=True)])
        root.button4.grid(column=2,row=3,sticky=EW,padx=15,pady=15)
        root.mainloop()
def main():
    mi_app = Aplicacion()
    return 0
if __name__ == '__main__':
    main()
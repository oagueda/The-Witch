import csv
from tkinter import *
from tkinter import ttk
comillas = "\""
def GruposAutomaticos(ruta,servidor,UO,nombre):
    try:
        gruposparte1 = "Dsadd group \"CN="
        DC = "DC="
        Unidad = ",OU="
        puntobat = ".bat"
        if ruta == "":
            texto = "No has introducido nada en el campo de ruta del \narchivo .csv origen."
            return texto
        if servidor == "":
            texto = "No has introducido nada en el campo del DNS del \nservidor."
            return texto
        if UO == "":
            texto = "No has introducido nada en el campo de la unidad \norganizativa."
            return texto
        if nombre == "":
            texto = "No has introducido nada en el campo de nombre del archivo de salida"
            return texto
        datosseparados = servidor.split(".")
        nombre = (nombre,puntobat)
        nombre = "".join(nombre)
        datosjuntos = ",DC=".join(datosseparados)
        datosjuntos = (DC,datosjuntos)
        datosjuntos = "".join(datosjuntos)
        datosjuntos = (UO,datosjuntos)
        datosjuntos = ",".join(datosjuntos)
        datosjuntos = (Unidad,datosjuntos,comillas)
        datos = "".join(datosjuntos)
        f = open(nombre, "w")
        u = 0
        with open(ruta, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                grupos = row[0]
                tupla2 = (gruposparte1,grupos,datos)
                z = "".join(tupla2)
                f.write(z + "\n")
                u = u + 1
    except Exception as e:
        e = str(e)
        return e
    texto = "Grupos Generados con éxito, " + str(u) + " entradas correctas"
    return texto
class AplicacionGrupos:
    def __init__(self):
        root = Tk()
        root.configure()
        root.title('The Witch Grupos')
        root.resizable(width=False,height=False)
        root.iconbitmap('./lol.ico')
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")
        root.text1 = ttk.Label(root, text="Ruta del archivo .csv con los nombres de los grupos")
        root.text1.grid(column=0,row=0,sticky=EW,padx=15,pady=15)
        root.text2 = ttk.Label(root, text="Introducir el dominio DNS del Servidor: 1ASIR02.GSD.local")
        root.text2.grid(column=0,row=1,sticky=EW,padx=15,pady=15)
        root.text3 = ttk.Label(root, text="Introducir la Unidad Organizativa: Alumnos")
        root.text3.grid(column=0,row=2,sticky=EW,padx=15,pady=15)
        root.text4 = ttk.Label(root, text="Introducir el nombre de archivo de salida deseado")
        root.text4.grid(column=0,row=3,sticky=EW,padx=15,pady=15)
        root.entry1 = ttk.Entry(root)
        root.entry1.grid(column=3,row=0,sticky=EW,padx=15,pady=15)
        root.entry2 = ttk.Entry(root)
        root.entry2.grid(column=3,row=1,sticky=EW,padx=15,pady=15)
        root.entry3 = ttk.Entry(root)
        root.entry3.grid(column=3,row=2,sticky=EW,padx=15,pady=15)
        root.entry4 = ttk.Entry(root)
        root.entry4.grid(column=3,row=3,sticky=EW,padx=15,pady=15)
        root.pantalla = Text(root,font=("Sans Sheriff", 15) ,height = 2, width = 25)
        root.pantalla.grid(row=4,columnspan=4,sticky=EW,padx=15,pady=15)
        root.pantalla.insert("1.0","Bienvenido Usuario! Escribe tus datos y haz click en \"Generar Grupos\"")
        root.pantalla.configure(state='disabled')
        root.button = ttk.Button(root, text="Generar Grupos", command=lambda:[root.pantalla.configure(state='normal'),root.pantalla.delete("1.0", END),GruposAutomaticos(root.entry1.get(),root.entry2.get(),root.entry3.get(),root.entry4.get()), root.pantalla.insert("1.0",str(GruposAutomaticos(root.entry1.get(),root.entry2.get(),root.entry3.get(),root.entry4.get()))),root.pantalla.configure(state='disabled')])
        root.button.grid(column=3,row=5,sticky=EW,padx=15,pady=15)
        root.button2 = ttk.Button(root, text='Salir', command=root.destroy)
        root.button2.grid(column=0,row=5,sticky=EW,padx=15,pady=15)
        root.mainloop()
def mainGrupos():
    mi_app = AplicacionGrupos()
    return 0
import csv
from tkinter import *
from tkinter import ttk
comillas = "\"" #No cambiar
def normalizeraiz(s):
    replacements = (
        ("\\", ""),
        (".", ""),
        ("\"", "")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
def ComandosCarpetas(raiz,ArSalida,ArEntrada,internadas):
    try:
        if ArEntrada == "":
            texto = "No has introducido nada en el campo de ruta del \narchivo .csv origen."
            return texto
        if raiz == "":
            texto = "No has introducido nada en el campo de la raiz."
            return texto
        if ArSalida == "":
            texto = "No has introducido nada en el campo de nombre \ndel archivo de salida."
            return texto
        u = 0
        puntobat = ".bat"
        ArSalida = (ArSalida,puntobat)
        ArSalida = "".join(ArSalida)
        f = open(ArSalida, "w")
        internadas = internadas.split(",")
        subruta = ""
        mcarpeta = "mkdir \".\\"
        contrabarra = "\\"
        raizcarpetas = (mcarpeta,raiz)
        raizcarpetas = "".join(raizcarpetas)
        with open(ArEntrada, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                nombres = row[0]
                nombres = (nombres,contrabarra)
                nombres = "".join(nombres)
                subruta = ""
                nombressub_1 = []
                for y in row[1:]:
                    nombressub_1.append(str(y) + "\\")
                for x in nombressub_1:
                    subruta = str(subruta) + str(x)
                for z in internadas:
                    creacioncomando1 = (raizcarpetas,contrabarra,subruta,nombres,str(z))
                    X = "".join(creacioncomando1)
                    comandofinal = (X,comillas)
                    z = "".join(comandofinal)
                    f.write(z + "\n")
                    u = u + 1
    except Exception as e:
        print(e)
    texto = "Grupos Generados con éxito, " + str(u) + " entradas correctas"
    return texto
class AplicacionCarpetas:
    def __init__(self):
        root = Tk()
        root.configure()
        root.title('The Witch Carpetas')
        root.resizable(width=False,height=False)
        root.iconbitmap('./lol.ico')
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")
        root.text1 = ttk.Label(root, text="Ruta del archivo .csv con los nombres de las carpetas")
        root.text1.grid(column=0,row=0,sticky=EW,padx=15,pady=15)
        root.text2 = ttk.Label(root, text="Introducir el nombre deseado de la raiz de las carpetas")
        root.text2.grid(column=0,row=1,sticky=EW,padx=15,pady=15)
        root.text3 = ttk.Label(root, text="Introducir los nombres de las carpetas integradas")
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
        root.pantalla.insert("1.0","Bienvenido Usuario! Escribe tus datos y haz click en \"Generar Carpetas\"")
        root.pantalla.configure(state='disabled')
        root.button = ttk.Button(root, text="Generar Carpetas", command=lambda:[root.pantalla.configure(state='normal'),root.pantalla.delete("1.0", END),ComandosCarpetas(root.entry2.get(),root.entry4.get(),root.entry1.get(),root.entry3.get()), root.pantalla.insert("1.0",str(ComandosCarpetas(root.entry2.get(),root.entry4.get(),root.entry1.get(),root.entry3.get()))),root.pantalla.configure(state='disabled')])
        root.button.grid(column=3,row=5,sticky=EW,padx=15,pady=15)
        root.button2 = ttk.Button(root, text='Salir', command=root.destroy)
        root.button2.grid(column=0,row=5,sticky=EW,padx=15,pady=15)
        root.mainloop()
def mainCarpetas():
    mi_app = AplicacionCarpetas()
    return 0
    #ComandosCarpetas("Grupos","Grupos","Grupos.csv","SI,NO,A VECES")
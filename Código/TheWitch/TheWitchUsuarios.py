import csv
from tkinter import *
from tkinter import ttk
comillas = "\""
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ü", "u"),
        ("ñ", "n"),
        ("-", ""),
        (" ", ""),
    )   
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
def normalizeapellidos(s):
    replacements = (
        ("[", ""),
        ("]", " "),
        ("'", ""),
        (",", ""),
    )   
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
def CSVAutomaticos(ruta,servidor,UO,nombre):
    try:
        fila1 = "DN,objectClass,sn,givenName,sAMAccountName,userPrincipalName,displayName,Description"
        #datos = "OU=Alumnos,DC=1ASIR02,DC=local\"" #Cambiar esta linea y la siguienete por sus respectivos datos del servidor
        DC = "DC="
        Unidad = "OU="
        Arroba = "@"
        user = "user"
        puntocsv = ".csv"
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
        nombre = (nombre,puntocsv)
        nombre = "".join(nombre)
        datosjuntos = ",DC=".join(datosseparados)
        datosjuntos = (DC,datosjuntos)
        datosjuntos = "".join(datosjuntos)
        datosjuntos = (UO,datosjuntos)
        datosjuntos = ",".join(datosjuntos)
        datosjuntos = (Unidad,datosjuntos,comillas)
        datos = "".join(datosjuntos)
        correo = (Arroba,servidor)
        correo = "".join(correo)
        f = open(nombre, "w")#Cambiar Linea con el nombre del archivo de salida deseado
        f.write(fila1)
        cuentassave = ""
        errnum = 1
        u = 0
        with open(ruta, newline='') as csvfile: #Cambiar csv de entrada con formato adecuado
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                nombre = row[0]
                apellidos = row[1]
                tupla = (nombre, apellidos)
                x = " ".join(tupla)
                DN =("CN=" + x)
                descripcion = row[2]
                iniciales = nombre[0].lower()
                nombrefinal = nombre.split()[0]
                apellidoslow = apellidos.split()[0].lower()
                nombredelapellido = ""
                if nombre.split()[1:]:
                    nombredelapellido = normalizeapellidos(str(nombre.split()[1:]))
                apellidosreal = (nombredelapellido,apellidos)
                apellidoreal = "".join(apellidosreal)
                inicialapellido = (iniciales,apellidoslow)
                acountname = ".".join(inicialapellido)
                cuenta = normalize(acountname)
                i = int(1)
                error = 0
                while cuenta in cuentassave:
                    apellidoslow2 = apellidoslow + apellidos.split()[1].lower()[:i]
                    cuenta = inicialapellido = (iniciales,apellidoslow2)
                    acountname = ".".join(inicialapellido)
                    cuenta = normalize(acountname)
                    i = i + 1
                    error = error + 1
                    if error > 100:
                        texto = ("Ha ocurrido un error en la duplicidad de SamAcountName, demasiados nombres iguales Nº Linea: " + str(u))
                        errnum = errnum + 1
                        return texto
                cuentassave = cuentassave + "\n" + cuenta
                tupla3 = (cuenta,correo)
                correosi = "".join(tupla3)
                tupla2 = ( "\""+ DN,datos,user,apellidoreal,nombrefinal,cuenta,correosi,x,descripcion)
                z = ",".join(tupla2)
                f.write("\n" + z)
                u = u + 1
    except Exception as e:
        e = str(e)
        texto = (e)
        return texto
    texto = "Csv Generado con éxito, " + str(u) + " entradas correctas"
    return texto
class AplicacionUsuarios:
    def __init__(self):
        root = Tk()
        root.configure()
        root.title('The Witch Usuarios')
        root.resizable(width=False,height=False)
        root.iconbitmap('./lol.ico')
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")
        root.text1 = ttk.Label(root, text="Ruta del archivo .csv con los usuarios")
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
        root.pantalla.insert("1.0","Bienvenido Usuario! Escribe tus datos y haz click en \"Generar Usuarios\"")
        root.pantalla.configure(state='disabled')
        root.button = ttk.Button(root, text="Generar Usuarios", command=lambda:[root.pantalla.configure(state='normal'),root.pantalla.delete("1.0", END),CSVAutomaticos(root.entry1.get(),root.entry2.get(),root.entry3.get(),root.entry4.get()), root.pantalla.insert("1.0",str(CSVAutomaticos(root.entry1.get(),root.entry2.get(),root.entry3.get(),root.entry4.get()))),root.pantalla.configure(state='disabled')])
        root.button.grid(column=3,row=5,sticky=EW,padx=15,pady=15)
        root.button2 = ttk.Button(root, text='Salir', command=root.destroy)
        root.button2.grid(column=0,row=5,sticky=EW,padx=15,pady=15)
        root.mainloop()
def mainUsuarios():
    mi_app = AplicacionUsuarios()
    return 0
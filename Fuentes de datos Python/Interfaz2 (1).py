from tkinter import *
from tkinter import ttk
import random
import os

#pestanas
root= Tk()

personas =[]

notebook = ttk.Notebook(root)
notebook.configure(width=550, height=400)

#crearlas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
class datos:
  def __init__(self, nombre: str, aPat: str, aMat: str, correo: str, movil: str, ocupacion: str, leer: bool, musica: bool, videojuegos: bool, estado: str):
        self.nombre= nombre
        self.aPat= aPat
        self.aMat= aMat
        self.correo= correo
        self.movil= movil
        self.ocupacion = ocupacion
        self.leer = leer
        self.musica= musica
        self.videojuegos= videojuegos
        self.estado = estado
        
personas =[]    

if not os.path.isfile("Datos.csv"):
    with open("Datos.csv", 'w') as file:
        file.write("Nombre, ApellidoPaterno, Apellidomaterno, Correo, Movil, Ocupacion, Aficiones, Leer, Musica, Videojuegos, Estado\n")
        table = ttk.Treeview(tab2, columns=("nombre", "aPat", "aMat", "correo", "movil", "ocupacion", "leer", "musica", "videojuegos", "estado"))

        table.heading("#0", text="ID")
        table.heading("nombre", text="Nombre")
        table.heading("aPat", text="Apellido paterno")
        table.heading("aMat", text="Apellido materno")
        table.heading("correo", text="Correo")
        table.heading("movil", text="Móvil")
        table.heading("ocupacion", text="Ocupación")
        table.heading("leer", text="Lee")
        table.heading("musica", text="Escucha música")
        table.heading("videojuegos", text="Juega videojuegos")
        table.heading("estado", text="Estado")

        table.column("#0", width=50)
        table.column("nombre", width=100)
        table.column("aPat", width=120)
        table.column("aMat", width=120)
        table.column("correo", width=200)
        table.column("movil", width=100)
        table.column("ocupacion", width=120)
        table.column("leer", width=100)
        table.column("musica", width=120)
        table.column("videojuegos", width=120)
        table.column("estado", width=120)
        table.grid()
            
        
    

else:
    file= open("Datos.csv", "r")
    line = file.readline()

    line = file.readline()
    
    while line:

        
        DatosLeidos = line.strip().split(",") #split es para separar con el caracter indicado
        persona = datos(DatosLeidos[0], DatosLeidos[1], DatosLeidos[2], DatosLeidos[3], DatosLeidos[4], DatosLeidos[5], DatosLeidos[6], DatosLeidos[7], DatosLeidos[8], DatosLeidos[9])
        personas.append(persona)
        line = file.readline()

        for i, persona in enumerate(personas):
            table = ttk.Treeview(tab2, columns=("nombre", "aPat", "aMat", "correo", "movil", "ocupacion", "leer", "musica", "videojuegos", "estado"))

            table.heading("#0", text="ID")
            table.heading("nombre", text="Nombre")
            table.heading("aPat", text="Apellido paterno")
            table.heading("aMat", text="Apellido materno")
            table.heading("correo", text="Correo")
            table.heading("movil", text="Móvil")
            table.heading("ocupacion", text="Ocupación")
            table.heading("leer", text="Lee")
            table.heading("musica", text="Escucha música")
            table.heading("videojuegos", text="Juega videojuegos")
            table.heading("estado", text="Estado")

            table.column("#0", width=50)
            table.column("nombre", width=100)
            table.column("aPat", width=120)
            table.column("aMat", width=120)
            table.column("correo", width=200)
            table.column("movil", width=100)
            table.column("ocupacion", width=120)
            table.column("leer", width=100)
            table.column("musica", width=120)
            table.column("videojuegos", width=120)
            table.column("estado", width=120)
                
                
            table.insert(parent="", index=i, iid=i, text=i+1, values=(DatosLeidos[0], DatosLeidos[1], DatosLeidos[2], DatosLeidos[3], DatosLeidos[4], DatosLeidos[5], DatosLeidos[6], DatosLeidos[7], DatosLeidos[8], DatosLeidos[9]))
            
        
    table.grid()
    file.close()








     
     

     

def guardar():
    persona = datos(nombre.get(), aPat.get(), aMat.get(), correo.get(), movil.get(), ocupacion.get(), AficionesLe.get(), AficionesMu.get(), AficionesVi.get(), estado.get())
    personas.append(persona)
    with open("Datos.csv", "a") as file:

        if AficionesLe.get() == True:
            leer="Si lee"
        else:
            leer="No lee"

        if AficionesMu.get() == True:
            musica="Si escucha"
        else:
            musica="No escucha"

        if AficionesVi.get() == True:
            videojuegos="Si juega "
        else:
            videojuegos="No indicado"
            
        file.write(f"{persona.nombre}, {persona.aPat}, {persona.aMat}, {persona.correo}, {persona.movil}, {persona.ocupacion}, {leer}, {musica}, {videojuegos}, {persona.estado}\n")
        table.insert(parent="", index="end", iid=f"{len(personas)}_{random.randint(1, 1000)}", text=len(personas), values=(persona.nombre, persona.aPat, persona.aMat, persona.correo, persona.movil, persona.ocupacion, leer, musica, videojuegos, persona.estado))




     

     

   

     




style = ttk.Style()
style.configure('TLabel', font=('Arial', 14))

# Agregar las pestañas al notebook
notebook.add(tab1, text="     Datos    ")
notebook.add(tab2, text="     Guardados    ")


style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "red", "foreground": "black", "font": ("Arial", 14)},
        "map": {"background": [("selected", "Green")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

# Mostrar el notebook
notebook.pack(expand=True, fill=BOTH)



     
main_Frame= ttk.Frame(tab1, padding="10 10 30 30", width=400, height=400, relief="raised") #widget transparete hasta especificar
main_Frame.grid(column=0, row=0)
     
     
sub_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=200, height=200, relief="raised") #widget transparete hasta especificar
sub_Frame.grid(column=0, row=0)

sub2_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=200, height=200) #widget transparete hasta especificar
sub2_Frame.grid(column=1, row=0)

sub3_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=10, height=10, relief="raised") #widget transparete hasta especificar
sub3_Frame.grid(column=0, row=1, pady=10)

sub4_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=10, height=10) #widget transparete hasta especificar
sub4_Frame.grid(column=1, row=1)

sub5_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=10, height=10) #widget transparete hasta especificar
sub5_Frame.grid(column=0, row=3)
     
    
#nombre
nombre= ttk.Entry(sub_Frame,width=22)
nombre.grid(column=1,row=0)
   
ttk.Label(sub_Frame, text=" ").grid(column=0,row=1)
     
#paterno
aPat= ttk.Entry(sub_Frame,width=22)
aPat.grid(column=1,row=2)

ttk.Label(sub_Frame, text=" ").grid(column=0,row=3)
     
#materno
aMat= ttk.Entry(sub_Frame,width=22)
aMat.grid(column=1,row=4)

ttk.Label(sub_Frame, text=" ").grid(column=0,row=5)
     
#correo
correo= ttk.Entry(sub_Frame,width=22)
correo.grid(column=1,row=6)

ttk.Label(sub_Frame, text=" ").grid(column=0,row=7)
     
#movil
movil= ttk.Entry(sub_Frame, width=22)
movil.grid(column=1,row=8)

     
   
ttk.Label(sub_Frame, text="Nombre: ").grid(column=0,row=0)
ttk.Label(sub_Frame, text=" ").grid(column=0,row=1)    
ttk.Label(sub_Frame, text="A.Paterno: ").grid(column=0,row=2)
ttk.Label(sub_Frame, text=" ").grid(column=0,row=3)
ttk.Label(sub_Frame, text="A.Materno: ").grid(column=0,row=4)
ttk.Label(sub_Frame, text=" ").grid(column=0,row=5)
ttk.Label(sub_Frame, text="Correo: ").grid(column=0,row=6)
ttk.Label(sub_Frame, text=" ").grid(column=0,row=7)
ttk.Label(sub_Frame, text="Movil: ").grid(column=0,row=8)


ocupacion=StringVar()
estudiante= ttk.Radiobutton(sub2_Frame,text="Estudiante").grid(column=0,row=0,sticky=(W,E,N,S))
empleado= ttk.Radiobutton(sub2_Frame,text="Empleado").grid(column=0,row=1,sticky=(W,E,N,S))
desempleado= ttk.Radiobutton(sub2_Frame,text="Desempleado").grid(column=0,row=2,sticky=(W,E,N,S))

AficionesLe=BooleanVar()
AficionesMu=BooleanVar()
AficionesVi=BooleanVar()


ttk.Label(sub3_Frame, text="Aficiones ").grid(column=0,row=0)
AficionesL=ttk.Checkbutton(sub3_Frame,text="Leer", variable=AficionesLe).grid(column=0,row=1)
AficionesM=ttk.Checkbutton(sub3_Frame,text="Musica",variable=AficionesMu).grid(column=1,row=1)
AficionesV=ttk.Checkbutton(sub3_Frame,text="Videojuegos",variable=AficionesVi).grid(column=2,row=1)


estado=StringVar()
comboEstados= ttk.Combobox(sub4_Frame,textvariable=estado)
comboEstados.grid()
comboEstados['values']=("Jalisco", "Nayarit", "Colima", "Michoacan")


ttk.Button(sub5_Frame, text="Guardar", command=guardar).grid(column=0, row=0,padx=20,)
ttk.Button(sub5_Frame, text="Base de datos", command=guardar).grid(column=2, row=0,padx=20,)

ttk.Button(sub5_Frame, text="Cancelar").grid(column=1, row=0,padx=20)

root.mainloop()

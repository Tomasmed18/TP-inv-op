#! /usr/bin/env python
# -*- coding: latin-1 -*-
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Feb 22, 2018 12:32:21 AM
import sys
import tooltip
import os #para arreglar los problemas de path
import Notebook
import mainWindow_support

import TablaInterfaz as TI

from tkinter.filedialog import askopenfilename

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1



def vp_start_gui(adminInterfaz):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Ventana_principal (root,adminInterfaz)
    mainWindow_support.init(root, top)
    root.mainloop()

w = None
def create_Ventana_principal(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Ventana_principal (w)
    mainWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Ventana_principal():
    global w
    w.destroy()
    w = None


class Ventana_principal:
    adminInterfaz=None

    tabActiva=None #es el absolute path de la tab seleccionada
    tabs=None
    tablaActual = None
    tablas=None #nombre y la tabla
    note=None
    mapaRutas=None #va a servir para mostrar una version resumida en la tab pero pudiendo comunicarse con el adminModelo

    def DibujarTabla(self,dataset):
          self.tablaActual = TI.TablaInterfaz(None, dataset.nombresColumnas(), cantidadFilasVisibles= 20)
          self.tablaActual.place(x=10, y=150, anchoPix= 960)
          self.tablaActual.cargarDataset(dataset)
          return self.tablaActual

    def botonArchivos(self):
        ruta=askopenfilename()
        if(ruta is not None and ruta is not ''):
            dataset, ruta = self.adminInterfaz.cargarDatos(ruta)
            #se agrega la tabla del dataset cargado
            tablaDibujada = self.DibujarTabla(dataset)
            self.tabs.append(ruta)
            auxRuta=ruta.split("/")
            auxRuta=auxRuta[len(auxRuta)-1] #obtengo lo ultimo del archivo
            self.tablas.append([auxRuta,tablaDibujada]) #se guarda la tabla, para luego no tener que redibujar si se cambia la tab
            self.mapaRutas[auxRuta]=ruta
            self.note.addTab(auxRuta)
            self.note.seleccionarTab(auxRuta)
            self.tabActiva=ruta
            self.actualizarCombobox()

    def agregarDataset(self, datasetNuevo, nombre):
        nuevaTabla = self.DibujarTabla(datasetNuevo)
        self.tabs.append(nombre)
        self.tablas.append([nombre, nuevaTabla])
        self.mapaRutas[nombre] = nombre
        self.note.addTab(nombre)
        self.note.seleccionarTab(nombre)
        self.tabActiva = nombre
        self.actualizarCombobox()

    def actualizarCombobox(self):
        c = []
        for t in self.tablas:
            c.append(t[0])
        self.ComboArchivoAMergear["values"] = c

    def botonCategorias(self):
        ruta=askopenfilename()
        if(ruta is not None and ruta is not ''):
            aux=self.adminInterfaz.cargarCategorias(ruta, self.tabActiva)
            tablaDibujada=self.DibujarTabla(aux)

            #a continuacion lo que se hace es eliminar la tabla dibujada anterior para reemplazarla con una nueva
            #esta nueva tabla tiene los cambios presentados al cargar las nuevas categorias
            #podria hacerse que tablas fuera un diccionario para hacerlo mas eficiente
            #el costo se espera O(n), se considera que es insignificante
            auxRuta=self.tabActiva.split('/')[-1]
            for i in self.tablas:
                #self tablas es una lista de listas, si auxRuta (la version acotada del archivo)
                #se encuentra en una de esas listas entonces hay que actualizar el dibujo
                if auxRuta in i:
                    self.tablas.remove(i)
                    self.tablas.append([auxRuta,tablaDibujada])
                    break

    def botonFiltros(self):
        ruta=askopenfilename()
        if(ruta is not None and ruta is not ''):
            aux =self.adminInterfaz.cargarFiltros(ruta, self.tabActiva)
            tablaDibujada=self.DibujarTabla(aux)

            #idem botonCategorias
            auxRuta=self.tabActiva.split('/')[-1]
            for i in self.tablas:
                if auxRuta in i:
                    self.tablas.remove(i)
                    self.tablas.append([auxRuta,tablaDibujada])
                    break


    def botonCluster(self):
        self.adminInterfaz.abrirVentanaCluster(self.tabActiva)

       #le mando la tab activa para hacer clustering, se espera que se elija la del merge de datasets
       #de caso contrario el usuario vera un arhivo que no espera y lo puede solucionar tranquilamente

    def botonArbol(self):
        self.DibujarTabla(self.adminInterfaz.__test__())

    def mostrarTablaPorTab(self,nombreTabla):
        if(len(self.mapaRutas)>1):
            self.tabActiva=self.mapaRutas[nombreTabla]
            for tabla in self.tablas:
                if tabla[0] != nombreTabla:
                    tabla[1].place(x=10000, y=150, anchoPix= 960)
                else:
                    tabla[1].place(x=10, y=150, anchoPix= 960)
                    self.tablaActual = tabla[1]



    def hacerMergeTablas(self):
        tablasAMergear = []
        for t in self.tablas:
            if (t[1] == self.tablaActual or t[0] ==self.ComboArchivoAMergear.get()): # si es la tabla actual o la seleccionada en el combobox
                tablasAMergear.append(t[0]) #se agrega a la lista a mergear
        if len(tablasAMergear) < 2: #si se selecciono la misma, se va a hacer merge con la misma tabla
            raise ValueError('Se deben seleccionar 2 tablas diferentes para realizar un merge')
        self.adminInterfaz.abrirVentanaMerge(tablasAMergear)

    def configurarVistaNotebook(self):
        self.style.configure('TNotebook.Tab', background='#d9d9d9')
        self.style.configure('TNotebook.Tab', foreground='#000000')
        self.style.map('TNotebook.Tab', background=
            [('selected', 'white'), ('active','#d5ffd8')])

        #esto le saca la linea punteada a la tab
        self.style.layout("Tab",
            [('Notebook.tab', {'sticky': 'nswe', 'children':
                [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                    #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                        [('Notebook.label', {'side': 'top', 'sticky': ''})],
                    #})],
                })],
            })]
            )

    def insertarToolTips(self):

        stringCategorias="Este boton sirve para cargar las categorias que ligan un campo de los dataset a unas palabras claves.\n Por ejemplo Economia se define a partir del campo 'titulo_secundario' con la palabra clave 'Administracion'\n"
        stringFiltros="Este boton sirve para cargar filtros definidos en un archivo, por ejemplo que la fecha de ingreso sea en el 2017"
        stringArchivos="Este boton permite cargar los archivos de notas y alumnos en formato excel"
        tooltip.createToolTip(self.CargarCategorias,stringCategorias)
        tooltip.createToolTip(self.CargarArchivo,stringArchivos)
        tooltip.createToolTip(self.cargarFiltros,stringFiltros)

    def insertarAccionesBotones(self):
        #self.CargarArchivo.configure(command=self.establecerFiltro)
        self.CargarArchivo.configure(command=self.botonArchivos)
        self.CargarCategorias.configure(command=self.botonCategorias)
        self.cargarFiltros.configure(command=self.botonFiltros)
        self.generarArbol.configure(command=self.botonArbol)
        self.generarCluster.configure(command=self.botonCluster)
        self.botonMerge.configure(command=self.hacerMergeTablas)

    def insertarCambios(self):
        #ESTE METODO GENERA CAMBIOS A LA INTERFAZ, POR EJEMPLO, LE DA A LOS BOTONES TOOLTIP Y LOS LIGA A OTRAS FUNCIONES
        self.__inicializarPrivados__()
        self.insertarToolTips()
        self.insertarAccionesBotones()
        self.configurarVistaNotebook()


    def __inicializarPrivados__(self):
        self.tabs=[]
        self.mapaRutas={}

    def __init__(self, top=None,adminInterfaz=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("999x712+520+140")
        top.title("Ventana principal")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        #evitar problemas de paths, usa os
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        self.adminInterfaz=adminInterfaz #referencia al administrador de interfaz que se comunica con el admin de modelo para manejar la parte logica
        self.adminInterfaz.setMainWindow(self)

        self.CargarCategorias = Button(top)
        self.CargarCategorias.place(relx=0.12, rely=0.01, height=103, width=104)
        self.CargarCategorias.configure(activebackground="#d9d9d9")
        self.CargarCategorias.configure(activeforeground="#000000")
        self.CargarCategorias.configure(background="#d9d9d9")
        self.CargarCategorias.configure(disabledforeground="#a3a3a3")
        self.CargarCategorias.configure(foreground="#000000")
        self.CargarCategorias.configure(highlightbackground="#d9d9d9")
        self.CargarCategorias.configure(highlightcolor="black")
        self._img1 = PhotoImage(file=os.path.join(THIS_FOLDER, 'resources/categorias2.png'))
        self.CargarCategorias.configure(image=self._img1)
        self.CargarCategorias.configure(pady="0")
        self.CargarCategorias.configure(text='''categorias''')



        self.CargarArchivo = Button(top)
        self.CargarArchivo.place(relx=0.23, rely=0.01, height=104, width=105)
        self.CargarArchivo.configure(activebackground="#d9d9d9")
        self.CargarArchivo.configure(activeforeground="#000000")
        self.CargarArchivo.configure(background="#d9d9d9")
        self.CargarArchivo.configure(disabledforeground="#a3a3a3")
        self.CargarArchivo.configure(foreground="#000000")
        self.CargarArchivo.configure(highlightbackground="#d9d9d9")
        self.CargarArchivo.configure(highlightcolor="black")
        self._img2 = PhotoImage(file=os.path.join(THIS_FOLDER,"./resources/excel2.png"))
        self.CargarArchivo.configure(image=self._img2)
        self.CargarArchivo.configure(pady="0")
        self.CargarArchivo.configure(text='''archivo''')


        self.cargarFiltros = Button(top)
        self.cargarFiltros.place(relx=0.01, rely=0.01, height=103, width=104)
        self.cargarFiltros.configure(activebackground="#d9d9d9")
        self.cargarFiltros.configure(activeforeground="#000000")
        self.cargarFiltros.configure(background="#d9d9d9")
        self.cargarFiltros.configure(disabledforeground="#a3a3a3")
        self.cargarFiltros.configure(foreground="#000000")
        self.cargarFiltros.configure(highlightbackground="#d9d9d9")
        self.cargarFiltros.configure(highlightcolor="black")
        self._img3 = PhotoImage(file=os.path.join(THIS_FOLDER,"./resources/filtros3.png"))
        self.cargarFiltros.configure(image=self._img3)
        self.cargarFiltros.configure(pady="0")
        self.cargarFiltros.configure(text='''filtro''')


        self.generarCluster = Button(top)
        self.generarCluster.place(relx=0.834, rely=0.84, height=104, width=137)
        self.generarCluster.configure(activebackground="#d9d9d9")
        self.generarCluster.configure(activeforeground="#000000")
        self.generarCluster.configure(background="#d9d9d9")
        self.generarCluster.configure(disabledforeground="#a3a3a3")
        self.generarCluster.configure(foreground="#000000")
        self.generarCluster.configure(highlightbackground="#d9d9d9")
        self.generarCluster.configure(highlightcolor="black")
        self._img4 = PhotoImage(file=os.path.join(THIS_FOLDER,"./resources/cluster.png"))
        self.generarCluster.configure(image=self._img4)
        self.generarCluster.configure(pady="0")
        self.generarCluster.configure(text='''Ver Cluster''')
        self.generarCluster.configure(width=137)

        self.generarArbol = Button(top)
        self.generarArbol.place(relx=0.65, rely=0.84, height=104, width=137)
        self.generarArbol.configure(activebackground="#d9d9d9")
        self.generarArbol.configure(activeforeground="#000000")
        self.generarArbol.configure(background="#d9d9d9")
        self.generarArbol.configure(disabledforeground="#a3a3a3")
        self.generarArbol.configure(foreground="#000000")
        self.generarArbol.configure(highlightbackground="#d9d9d9")
        self.generarArbol.configure(highlightcolor="black")
        self.generarArbol.configure(pady="0")
        self.generarArbol.configure(text='''Ver Arbol''')

        self.botonMerge = Button(top)
        self.botonMerge.place(x=10, rely=0.84, height=30, width=100)
        self.botonMerge.configure(activebackground="#d9d9d9")
        self.botonMerge.configure(activeforeground="#000000")
        self.botonMerge.configure(background="#d9d9d9")
        self.botonMerge.configure(disabledforeground="#a3a3a3")
        self.botonMerge.configure(foreground="#000000")
        self.botonMerge.configure(highlightbackground="#d9d9d9")
        self.botonMerge.configure(highlightcolor="black")
        self.botonMerge.configure(pady="0")
        self.botonMerge.configure(text='''Hacer merge''')

        self.ComboArchivoAMergear = ttk.Combobox(top, state="readonly", width=15)
        self.ComboArchivoAMergear.place(x= 115, rely=0.84)


        self.insertarCambios()

        self.note=Notebook.Notebook(top,self)

        self.tablas = []


if __name__ == '__main__':
    vp_start_gui()

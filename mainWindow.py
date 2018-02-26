#! /usr/bin/env python
# -*- coding: latin-1 -*- 
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Feb 22, 2018 12:32:21 AM
import sys
import tooltip


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

import mainWindow_support

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
    
    def insertarToolTips(self):
        
        stringCategorias="Este boton sirve para cargar las categorias que ligan un campo de los dataset a unas palabras claves.\n Por ejemplo Economia se define a partir del campo 'titulo_secundario' con la palabra clave 'Administracion'\n"
        stringFiltros="Este boton sirve para cargar filtros definidos en un archivo, por ejemplo que la fecha de ingreso sea en el 2017"
        stringArchivos="Este boton permite cargar los archivos de notas y alumnos en formato excel"
        tooltip.createToolTip(self.CargarCategorias,stringCategorias)
        tooltip.createToolTip(self.CargarArchivo,stringArchivos)
        tooltip.createToolTip(self.cargarFiltros,stringFiltros)
        

    def insertarAccionesBotones(self):
        #self.CargarArchivo.configure(command=self.establecerFiltro)
        self.CargarArchivo.configure(command=self.adminInterfaz.cargarDatos)
        self.CargarCategorias.configure(command=self.adminInterfaz.cargarCategorias)
        self.cargarFiltros.configure(command=self.adminInterfaz.cargarFiltros)
    
    def insertarCambios(self):
        #ESTE METODO GENERA CAMBIOS A LA INTERFAZ, POR EJEMPLO, LE DA A LOS BOTONES TOOLTIP Y LOS LIGA A OTRAS FUNCIONES
        self.insertarToolTips()
        self.insertarAccionesBotones()
        
    
        
    def __init__(self, top=None,adminInterfaz=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("999x712+520+140")
        top.title("Ventana principal")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.adminInterfaz=adminInterfaz #referencia al administrador de interfaz que se comunica con el admin de modelo para manejar la parte logica

        self.CargarCategorias = Button(top)
        self.CargarCategorias.place(relx=0.12, rely=0.01, height=103, width=104)
        self.CargarCategorias.configure(activebackground="#d9d9d9")
        self.CargarCategorias.configure(activeforeground="#000000")
        self.CargarCategorias.configure(background="#d9d9d9")
        self.CargarCategorias.configure(disabledforeground="#a3a3a3")
        self.CargarCategorias.configure(foreground="#000000")
        self.CargarCategorias.configure(highlightbackground="#d9d9d9")
        self.CargarCategorias.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="./resources/categorías2.png")
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
        self._img2 = PhotoImage(file="./resources/excel2.png")
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
        self._img3 = PhotoImage(file="./resources/filtros3.png")
        self.cargarFiltros.configure(image=self._img3)
        self.cargarFiltros.configure(pady="0")
        self.cargarFiltros.configure(text='''filtro''')



        self.insertarCambios()

        self.insertarCambios()

    
if __name__ == '__main__':
    vp_start_gui()



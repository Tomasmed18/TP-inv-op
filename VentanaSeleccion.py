#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Mar 04, 2018 04:52:05 AM
import sys

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

import VentanaSeleccion_support


def vp_start_gui(Admin, mapaLxC=None,mapaResult=None):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    VentanaSeleccion_support.set_Tk_var()
    top = VentanaSeleccion (root, Admin, mapaLxC, mapaResult)
    VentanaSeleccion_support.init(root, top)
    root.mainloop()

w = None
def create_VentanaSeleccion(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    VentanaSeleccion_support.set_Tk_var()
    top = VentanaSeleccion(w)
    VentanaSeleccion_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_VentanaSeleccion():
    global w
    w.destroy()
    w = None


class VentanaSeleccion:
    #genera una interfaz con indicadores y opciones y devuelve las opciones elegidas en mapaElecciones, se debe proporcionar el mapa de labels y las opciones
    #El maximo que soporta son 5 labels, further work is requiered.

    adminInter = None
    mapElecciones=None
    resultados=None
    top=None
    def cerrar(self):
        self.top.destroy()

    def aceptarOpciones(self):
        for K in self.mapElecciones:
                self.resultados[K]=self.mapElecciones[K].get() #mapElecciones en la misma clave que es un texto debiera ser un combobox con una opcion seleccionada
        self.adminInter.configurarCluster(self, cantClusters = int(self.comboCantClusters.get()))

    def insertarAccionesBotones(self):
        self.aceptar.configure(command=self.aceptarOpciones)
        self.cancelar.configure(command=self.cerrar)

    def __init__(self, top=None,AdminInterfaz = None, mapaLabelsXContenido=None, resultados=None):
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

        top.geometry("851x232+608+384")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        Xlabel=0.02
        Ylabel=0.28

        Xbox=0.02
        Ybox=0.5

        self.aceptar = Button(top)
        self.aceptar.place(relx=Xbox, rely=0.78, height=44, width=117)
        self.aceptar.configure(activebackground="#d9d9d9")
        self.aceptar.configure(activeforeground="#000000")
        self.aceptar.configure(background="#d9d9d9")
        self.aceptar.configure(disabledforeground="#a3a3a3")
        self.aceptar.configure(foreground="#000000")
        self.aceptar.configure(highlightbackground="#d9d9d9")
        self.aceptar.configure(highlightcolor="black")
        self.aceptar.configure(pady="0")
        self.aceptar.configure(text='''Aceptar''')
        self.aceptar.configure(width=117)

        self.cancelar = Button(top)
        self.cancelar.place(relx=Xbox+0.2, rely=0.78, height=44, width=117)
        self.cancelar.configure(activebackground="#d9d9d9")
        self.cancelar.configure(activeforeground="#000000")
        self.cancelar.configure(background="#d9d9d9")
        self.cancelar.configure(disabledforeground="#a3a3a3")
        self.cancelar.configure(foreground="#000000")
        self.cancelar.configure(highlightbackground="#d9d9d9")
        self.cancelar.configure(highlightcolor="black")
        self.cancelar.configure(pady="0")
        self.cancelar.configure(text='''Cancelar''')

        self.labCantClusters = ttk.Label(top, text="Cantidad de clusters")
        self.labCantClusters.place(relx= Xbox+0.4, rely=0.78)
        self.labCantClusters.configure(background="#d9d9d9")

        self.comboCantClusters = ttk.Combobox(top, state="readonly", width=15 )
        self.comboCantClusters.place(relx= Xbox+0.4, rely=0.88)
        self.comboCantClusters["values"] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.comboCantClusters.set(2)

        self.mapElecciones={} #label x combobox
        self.resultados=resultados
        self.top=top
        self.adminInter = AdminInterfaz

        if(mapaLabelsXContenido is not None):
            for K in mapaLabelsXContenido:
                    Label1 = Label(top)
                    Label1.place(relx=Xlabel, rely=Ylabel, height=21, width=140)
                    Label1.configure(background="#d9d9d9")
                    Label1.configure(disabledforeground="#a3a3a3")
                    Label1.configure(foreground="#000000")
                    Label1.configure(text=K)

                    TCombobox1 = ttk.Combobox(top,state='readonly')
                    TCombobox1.place(relx=Xbox, rely=Ybox, relheight=0.12, relwidth=0.17)

                    TCombobox1.configure(textvariable=StringVar()) #Si uso el combobox de ventanaSeleccion_support se comparte el mismo combobox para todos los valores
                    TCombobox1.configure(takefocus="")

                    TCombobox1["values"]=mapaLabelsXContenido[K]
                    #TCombobox1.bind("<<ComboboxSelected>>", self.selection_changed)  EVENTO

                    self.mapElecciones[K]=TCombobox1
                    Xlabel=Xlabel+0.2
                    Xbox=Xbox+0.2



        self.insertarAccionesBotones()



if __name__ == '__main__':
    vp_start_gui()

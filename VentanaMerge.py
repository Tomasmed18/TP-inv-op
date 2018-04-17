#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Mar 29, 2018 10:43:15 PM
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

import VentanaMerge_support

def vp_start_gui(adminInterfaz, tablas):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = VentanaMerge (root, adminInterfaz = adminInterfaz, tablas = tablas)
    VentanaMerge_support.init(root, top)
    root.mainloop()

w = None
def create_VentanaMerge(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = VentanaMerge (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_VentanaMerge():
    global w
    w.destroy()
    w = None


class VentanaMerge:
    listboxes = [] #lista de listboxes donde van a estar las columnas de cada archivo
    adminInter = None
    top=None

    def botonAceptar(self):
        selecciones = {}
        for l in self.listboxes:
            columnas = []
            seleccion = l[1].curselection()
            for i in seleccion:
                entrada = l[1].get(i)
                columnas.append(entrada)
            if (len(columnas) > 0):
                selecciones[l[0]]= columnas
            else:
                selecciones[l[0]]= None
        self.top.destroy()
        self.adminInter.realizarMerge(selecciones)



    def __init__(self, top=None, adminInterfaz = None,  tablas=[]):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("343x299+427+253")
        top.title("Seleccionar columnas")
        top.configure(background="#d9d9d9")
        self.top = top
        self.adminInter = adminInterfaz
        self.listboxes = []


        offset = 0.0 #sirve para ir corriendo los elementos de la ventana

        for k in tablas:

            label = Label(top)
            label.place(relx=0.02 + offset, rely=0.17, height=21, width=104)
            label.configure(background="#d9d9d9")
            label.configure(disabledforeground="#a3a3a3")
            label.configure(foreground="#000000")
            label.configure(text = k)


            listbox = Listbox(top)
            listbox.configure(selectmode = MULTIPLE) #para seleccionar multiples valores
            listbox.configure(exportselection = 0) #para seleccionar de multiples listboxes
            listbox.place(relx=0.02 + offset, rely=0.27, relheight=0.51, relwidth=0.45)
            listbox.configure(background="white")
            listbox.configure(disabledforeground="#a3a3a3")
            listbox.configure(font="TkFixedFont")
            listbox.configure(foreground="#000000")
            listbox.configure(width=144)
            for columna in tablas[k]:
                listbox.insert(END, columna) #se inserta cada columnas en la listbox
            self.listboxes.append([k, listbox]) #se agrega a la lista de listboxes
                                                    #junto con el nombre del archivo
            offset += 0.5


        self.cancelar = Button(top)
        self.cancelar.place(relx=0.52, rely=0.87, height=24, width=67)
        self.cancelar.configure(activebackground="#d9d9d9")
        self.cancelar.configure(activeforeground="#000000")
        self.cancelar.configure(background="#d9d9d9")
        self.cancelar.configure(disabledforeground="#a3a3a3")
        self.cancelar.configure(foreground="#000000")
        self.cancelar.configure(highlightbackground="#d9d9d9")
        self.cancelar.configure(highlightcolor="black")
        self.cancelar.configure(pady="0")
        self.cancelar.configure(text='''Cancelar''')

        self.aceptar = Button(top)
        self.aceptar.place(relx=0.78, rely=0.87, height=24, width=67)
        self.aceptar.configure(activebackground="#d9d9d9")
        self.aceptar.configure(activeforeground="#000000")
        self.aceptar.configure(background="#d9d9d9")
        self.aceptar.configure(disabledforeground="#a3a3a3")
        self.aceptar.configure(foreground="#000000")
        self.aceptar.configure(highlightbackground="#d9d9d9")
        self.aceptar.configure(highlightcolor="black")
        self.aceptar.configure(pady="0")
        self.aceptar.configure(text='''Aceptar''')
        self.aceptar.configure(command=self.botonAceptar)

        self.Label6 = Label(top)
        self.Label6.place(relx=0.02, rely=0.03, height=21, width=286)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Seleccione las columnas por las cuales unir las tablas:''')






if __name__ == '__main__':
    vp_start_gui()

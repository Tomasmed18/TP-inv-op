#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Apr 17, 2018 01:12:15 AM
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

import ventanaPloteo_support
import matplotlib 
#matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import Cluster as Cluster
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as color

def vp_start_gui(cluster=None):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = VentanaPloteo (root,cluster)
    ventanaPloteo_support.init(root, top)
    root.mainloop()

w = None
def create_VentanaPloteo(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = VentanaPloteo (w)
    ventanaPloteo_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_VentanaPloteo():
    global w
    w.destroy()
    w = None


class VentanaPloteo:
    canv=None
    mostrarPuntos=None
    def close(self):
        
        self.top.destroy()  #Este se encarga de limpiar los widgets pero no necesariamente termina la ejecucion del mainloop
        #especialmente si top es una instancia de topLevel
        self.top.quit() #salgo del mainloop, sin embargo puede existir codigo todavia ejecutando por detras
        #este es el caso del ploteo y el metodo draw(). Son metodos que pueden seguir interactuando con los widgets
        
        #aunque parezca contradictorio la union de estos dos metodos permite que termine la ventana correctamente
    
    
    
    def setPuntos(self,cluster, diccClustersXColores):
        
        labelsCont=cluster.getClustersYPuntos()
        labelsColor=diccClustersXColores
        posX=15
        posY=150
        
        for k in labelsCont.keys():
            texto='cluster '+ str(k) + ' : ' + str(labelsCont[k])
            self.mostrarPuntos.create_oval(posX-15,posY-5,posX-5,posY+5,width=1,fill=labelsColor[k],outline=labelsColor[k]) #tienen la misma clave
            self.mostrarPuntos.create_text(posX,posY,text=texto,anchor='w',font=('Arial',10))
            
            
            posY+=20
    def __init__(self, top=None, cluster=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.top=top
        self.top.geometry("888x500+268+250")
        self.top.title("VentanaPloteo")
        self.top.configure(background="white")
        self.top.minsize(width=888, height=500)

        
        self.canv = Canvas(top)
        self.canv.place(relx=0.01, rely=0.02, relheight=0.96, relwidth=0.81)
        self.canv.configure(background="white")
        self.canv.configure(borderwidth="2")
        self.canv.configure(insertbackground="black")
        self.canv.configure(relief=RIDGE)
        self.canv.configure(selectbackground="#c4c4c4")
        self.canv.configure(selectforeground="black")
        self.canv.configure(width=586)

        self.mostrarPuntos = Canvas(top)
        self.mostrarPuntos.place(relx=0.81, rely=0.02, relheight=0.96
                , relwidth=0.18)
        self.mostrarPuntos.configure(background="white")
        self.mostrarPuntos.configure(borderwidth="0")
        self.mostrarPuntos.configure(insertbackground="black")
        
     
        self.mostrarPuntos.configure(relief=RIDGE)
        self.mostrarPuntos.configure(selectbackground="#c4c4c4")
        self.mostrarPuntos.configure(selectforeground="black")
        self.mostrarPuntos.configure(width=256)
        
        self.mostrarPuntos.configure(highlightthickness=0)
        self.mostrarPuntos.create_text(15,115,text="Cantidad de Puntos\n por cluster",anchor='w',justify='center', font=('Arial',12))
        self.mostrarPuntos.create_text(15,80,text='Correlacion: ' + str(cluster.getCorrelacion()),anchor='w',justify='center', font=('Arial',12))
       
        
        self.top.protocol("WM_DELETE_WINDOW",self.close)
        #protocol es una parte de la libreria tkinter, permite aplicar funcionalidad junto con el WINDOWS MANAGER
        #Aca, cuando apreto la X que cierra la ventana se ejecuta el metodo self.close
        
        colormap = cm.rainbow(np.linspace(0, 1, cluster.getCantClusters()))
        diccClustersXColores={}
         
        auxColor=0
        for i in cluster.getNombresClusters():
             diccClustersXColores[i]=color.to_hex(colormap[auxColor]) #transformo el color a hexadecimal para ser mas portable
             auxColor+=1
            
        data=cluster.getData() #matrix
        fig=Figure(figsize=(6,6))
        
        plot=fig.add_subplot(111)
        centers=cluster.getCenters()
        plot.scatter(data[:, 0], data[:, 1],c=colormap[cluster.getDistribucion()])
        plot.scatter(centers[:, 0], centers[:, 1], marker="x", color='black')
        plot.set(xlabel=cluster.getEtiquetaX(), ylabel=cluster.getEtiquetaY())
        plot.axis('tight')
        self.plot = FigureCanvasTkAgg(fig, master=top)
        
        self.setPuntos(cluster, diccClustersXColores)
        #print(cluster.getCantPuntos(0))
      
        
        toolbar = NavigationToolbar2TkAgg(self.plot, top) #es la barra de abajo de navegacion
        toolbar.update()
        self.plot.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1) 
        self.mostrarPuntos.pack(side=RIGHT,fill=BOTH,expand=0)
        #en realidad es Tkinter.TOP pero importe como from tkinter import * (esto podria ser una mala practica pero no afecta mucho en este modulo)
        self.plot.draw()
       
        
if __name__ == '__main__':
    
    f=Figure(figsize=(6,6))
    ax=f.add_subplot(111)
    ax.scatter([1,2,3,2,7],[2,3,42,1,3])
    ax.axis(tight=True)
    dicc={1:43,2:542}
    
    #diccColores={1:'blue',2:'green'}

    colormap = cm.rainbow(np.linspace(0, 1, 2))
    X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])
    print(color.to_hex(colormap[0]))
    diccColores={1:color.to_hex(colormap[0]),2:color.to_hex(colormap[1])}
    
    #diccColores={1:'blue',2:'green'}
    vp_start_gui(Cluster.Cluster(X,'x','y',[0,0,0,1,1,1],2,np.array([[1,2],[1,2]]))) #lo de distribucion es bardero hacerlo aca en main
   



import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter.messagebox import showerror
import math
from numpy import true_divide
import utm
import simplekml
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import webbrowser
import time
import tkintermapview
from tkinter import filedialog

#CONSTANTES UTM A MINA
constante_1 = 1.31415E-05
constante_2	= 1.00087683
constante_3	= -476994.037
constante_4	= -7214453.535
#CONSTANTES MINA UTM
constante_5 = -1.31415E-05
constante_6 = 0.999123937
constante_7 = 476481.435
constante_8 = 7208139.49


# root window
root = tk.Tk()
root.title('Convertir Coordenadas')
# root.geometry('390x760')
root.resizable(False, False)
window_width = 390
window_height = 760
  # get the screen size of your computer [width and height using the root object as foolows]
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
    # Get the window position from the top dynamically as well as position from left or right as follows
position_top = int(screen_height/111 -window_height/111)
position_right = int(screen_width /2 - window_width/2)
    # this is the line that will center your window
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    # initialise the window

longitud = None
latitud = None

resultado = None
map_widget = None


# # field options
options = {'padx': 10, 'pady': 10}

# # convert button
def convertir_mina():
    """  Handle convert button click event 
    """
    try:
        Este = float(este.get())
        Norte = float(norte.get())
        result1 = round(constante_2*Este*math.cos(constante_1)+constante_2*Norte*math.sin(constante_1)+constante_3,3)
        result_1.config(text=result1)
        result2 = round(constante_2*Norte*math.cos(constante_1)-constante_2*Este*math.sin(constante_1)+constante_4,3)
        result_label2.config(text=result2)
        result_3.config(text="")
        result_4.config(text="")
        
    except ValueError as error:
        showerror(title='Error', message=error)

 
def convertir_utm():
    global latitud, longitud
    try:
        Este = float(este.get())
        Norte = float(norte.get())
        result1 = round(constante_6*Este*math.cos(constante_5)+constante_6*Norte*math.sin(constante_5)+constante_7,3)
        result_1.config(text=result1)
        result2 = round(constante_6*Norte*math.cos(constante_5)-constante_6*Este*math.sin(constante_5)+constante_8,3)
        result_label2.config(text=result2)
        
        convert = utm.to_latlon(result1, result2, 19, 'k')
    
        longitud = round(convert[1],6)
        latitud = round(convert[0],6)
    
        result_3.config(text=latitud)
        result_4.config(text=longitud)
        #crear marcador
        map_widget.set_position(latitud,longitud) 
        marker_2 = map_widget.set_marker(latitud, longitud, text="Punto de interés")
        
        
    except ValueError as error:
        showerror(title='Error', message=error)
        
def generar():
    global resultado    
    kml = simplekml.Kml()
    kml.newpoint(name="Punto Generado", coords=[(longitud,latitud)])
    resultado = asksaveasfilename(filetypes =[('KML', '*.KML')])
    
    if(resultado):
        if latitud and longitud != "":
            kml.save(resultado)

            messagebox.showinfo("showinfo", "Archivo KML Generado correctamente")
            webbrowser.open_new_tab(resultado)
        else:
            messagebox.showinfo("showinfo", "El archivo no se genero.")


       
def copy():
    copiado1 = str(result_1.cget("text"))
    copiado2 = str(result_label2.cget("text"))
    
    
    if copiado1 and copiado2 != "":
        total = f'Este: {copiado1} Norte: {copiado2}'
        root.clipboard_clear()
        root.clipboard_append(total)
        root.update()
        messagebox.showinfo("showinfo", "Valores copiados")
    else:
        messagebox.showwarning("showinfo", "no hay datos que copiar")
        
    
        

def copy2():
    copiado1 = str(result_3.cget("text"))
    copiado2 = str(result_4.cget("text"))
    
    if copiado1 and copiado2 != "":
        total = f'Latitud: {copiado1} Longitud: {copiado2}'
        root.clipboard_clear()
        root.clipboard_append(total)
        root.update() # the text will stay there after the window is closed
        messagebox.showinfo("showinfo", "Valores copiados")
    else:
        messagebox.showwarning("showinfo", "no hay datos que copiar")

def borrar():
    result_1.config(text="")
    result_label2.config(text="")
    result_3.config(text="")
    result_4.config(text="")
    
def changeText():
    cabecera2.config(text="COORDENADAS UTM")
        
def changeText2():
    cabecera2.config(text="COORDENADAS MINA")

def changeText3():
    cabecera3.config(text="COORDENADAS GEOGRAFICAS")

def ambos1():
    convertir_mina()
    changeText2()
    
def ambos2():
    convertir_utm()
    changeText()
    changeText3()
    
######################## Primera parte ########################
# Titulo 1
cabecera = ttk.Label(root, text='CONVERTIR COORDENADAS', font='Helvetica 15 italic bold') 
cabecera.grid(column=0, row = 0,columnspan=3,**options)

# este
este_label = ttk.Label(root, text='Coordenada Este', font='arial 10')
este_label.grid(column=0, row=1, **options)

# norte
norte_label = ttk.Label(root, text='Coordenada Norte', font='arial 10')
norte_label.grid(column=0, row=2,**options)

# este entrada
este = tk.StringVar()
este_entry = ttk.Entry(root, textvariable=este)
este_entry.grid(column=1, row=1,sticky=tk.W, **options)
este_entry.focus()


# oeste entrada
norte = tk.StringVar()
norte_entry = ttk.Entry(root, textvariable=norte)
norte_entry.grid(column=1, row=2,sticky=tk.W, **options)
norte_entry.focus()

################################################################################################################

######################## Segunda parte ########################

# titulo 2

cabecera2 = ttk.Label(root, text="", font='Helvetica 15 bold italic')
cabecera2.grid(column=0, row = 3,columnspan=3,**options)

# Etiqueta Este
etiqueta_1 = ttk.Label(root, text="ESTE",font='arial 10')
etiqueta_1.grid(row=4, column=0)

# Etiqueta norte
etiqueta_2 = ttk.Label(root, text="NORTE",font='arial 10')
etiqueta_2.grid(row=5, column=0)

# result label1
result_1 = ttk.Label(root, font='Helvetica 11 bold',borderwidth=1, relief="sunken")
result_1.grid(row=4, column=1,sticky=tk.EW)

# result label2
result_label2 = ttk.Label(root, font='Helvetica 11 bold',borderwidth=1, relief="sunken")
result_label2.grid(row=5, column=1, sticky=tk.EW)

################################################################################################################

######################## Tercera parte ########################

# titulo3
cabecera3 = ttk.Label(root, text="", font='Helvetica 15 bold italic')
cabecera3.grid(column=0, row = 6,columnspan=3,**options)

# este
este2_label = ttk.Label(root, text='LATITUD', font='arial 10')
este2_label.grid(column=0, row=7, **options)

# norte
norte2_label = ttk.Label(root, text='LONGITUD', font='arial 10')
norte2_label.grid(column=0, row=8,**options)

# result label3
result_3 = ttk.Label(root, font='Helvetica 11 bold',borderwidth=1, relief="sunken")
result_3.grid(row=7, column=1,sticky=tk.EW)

# result label4
result_4 = ttk.Label(root, font='Helvetica 11 bold',borderwidth=1, relief="sunken")
result_4.grid(row=8, column=1,sticky=tk.EW)

################################################################################################################

######################## Botones ########################

#boton 1
convert_button1 = ttk.Button(root, text='Convertir UTM')
convert_button1.grid(column=2, row=1)
convert_button1.configure(command=ambos2)

#boton 2
convert_button1 = ttk.Button(root, text='Convertir MINA')
convert_button1.grid(column=2, row=2)
convert_button1.configure(command=ambos1)

#boton borrar
convert_button1 = ttk.Button(root, text='Borrar')
convert_button1.grid(column=2, row=5)
convert_button1.configure(command=borrar)

#boton generar kml
convert_button1 = ttk.Button(root, text='Generar KML')
convert_button1.grid(column=2, row=8)
convert_button1.configure(command=generar)

# #boton copiar

# #boton copiar1
convert_button1 = ttk.Button(root, text='Copiar datos')
convert_button1.grid(column=2, row=4)
convert_button1.configure(command=copy)

# #boton copiar2                      
convert_button1 = ttk.Button(root, text='Copiar datos')
convert_button1.grid(column=2, row=7)
convert_button1.configure(command=copy2)

################################################################################################################





# creditos
creador = ttk.Label(root, text='© Desarollado por Bruno Oviedo y Rodrigo Araya, Diciembre 2021', font='arial 9')
creador.grid(column=0, row=9, columnspan=3,sticky=tk.S, padx=10, pady=25)

######################################### Widget mapa #####################################################


map_widget = tkintermapview.TkinterMapView(root, width=370, height=340, corner_radius=0)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite

# zoom mapa
map_widget.set_zoom(16)
    
map_widget.place(x=10, y=410)


# comenzar aplicacion
root.mainloop()

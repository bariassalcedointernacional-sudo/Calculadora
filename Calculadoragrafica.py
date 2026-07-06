from tkinter import *

ventana= Tk()
#funciones 


# interfaz grafica


# pantalla
pantalla=Entry(ventana)
pantalla.grid(row=0,column=0)
#botones
siete = Button(ventana,text="7")
siete.grid(row=1,column=0)
ocho = Button(ventana,text="8")
ocho.grid(row=1,column=0)
nueve = Button(ventana,text="9")
nueve.grid(row=1,column=0)
division = Button(ventana,text="/")
division.grid(row=1,column=0)
#segunda fila
siete = Button(ventana,text="4")
siete.grid(row=1,column=0)
ocho = Button(ventana,text="5")
ocho.grid(row=1,column=0)
nueve = Button(ventana,text="6")
nueve.grid(row=1,column=0)
division = Button(ventana,text="*")
division.grid(row=1,column=0)
#tercera fila
siete = Button(ventana,text="1")
siete.grid(row=1,column=0)
ocho = Button(ventana,text="2")
ocho.grid(row=1,column=0)
nueve = Button(ventana,text="3")
nueve.grid(row=1,column=0)
division = Button(ventana,text="-")
division.grid(row=1,column=0)
#cuarta fila
siete = Button(ventana,text="7")
siete.grid(row=1,column=0)
ocho = Button(ventana,text="8")
ocho.grid(row=1,column=0)
nueve = Button(ventana,text="9")
nueve.grid(row=1,column=0)
division = Button(ventana,text="/")
division.grid(row=1,column=0)
#quinta fila
siete = Button(ventana,text="7")
siete.grid(row=1,column=0)
ocho = Button(ventana,text="8")
ocho.grid(row=1,column=0)
nueve = Button(ventana,text="9")
nueve.grid(row=1,column=0)
division = Button(ventana,text="/")
division.grid(row=1,column=0)
ventana.mainloop()
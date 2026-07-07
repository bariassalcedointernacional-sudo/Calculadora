from tkinter import *

ventana= Tk()
#funciones 


# interfaz grafica


# pantalla
pantalla=Entry(ventana)
pantalla.grid(row=0,column=0,columnspan=20)

#botones
siete = Button(ventana,text="7")
siete.grid(row=1,column=0)
ocho = Button(ventana,text="8")
ocho.grid(row=1,column=1)
nueve = Button(ventana,text="9")
nueve.grid(row=1,column=2)
division = Button(ventana,text="/")
division.grid(row=1,column=3)

#segunda fila
cuatro = Button(ventana,text="4")
cuatro.grid(row=2,column=0)
cinco = Button(ventana,text="5")
cinco.grid(row=2,column=1)
seis = Button(ventana,text="6")
seis.grid(row=2,column=2)
multiplicacion = Button(ventana,text="*")
multiplicacion.grid(row=2,column=3)

#tercera fila
uno = Button(ventana,text="1")
uno.grid(row=3,column=0)
dos = Button(ventana,text="2")
dos.grid(row=3,column=1)
tres = Button(ventana,text="3")
tres.grid(row=3,column=2)
menos = Button(ventana,text="-")
menos.grid(row=3,column=3)

#cuarta fila
punto = Button(ventana,text=".")
punto.grid(row=4,column=0)
cero = Button(ventana,text="0")
cero.grid(row=4,column=1)
igual = Button(ventana,text="=")
igual.grid(row=4,column=2)
suma = Button(ventana,text="+")
suma.grid(row=4,column=3)

#Barra de borrar
borrar = Button(ventana,text="BORRAR")
borrar.grid(row=5,column=0,columnspan=24)

ventana.mainloop()
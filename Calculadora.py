from tkinter import *

ventanas=Tk()
valor_a=0
valor_b=0
operacion= "sumar"
resultado=0
# funciones
def sumar():
    global valor_a
    global valor_b
    return valor_a+valor_b
def restar():
    global valor_a
    global valor_b
    return valor_a-valor_b
def dividir():
    global valor_a
    global valor_b
    return valor_a/valor_b
def multiplicar():
    global valor_a
    global valor_b
    return valor_a*valor_b
def Borrar():
    global pantalla
    pantalla.delete(0,END)
def agregar_en_pantalla(valor):
    global pantalla
    pantalla.insert(END,valor)
    
def operar(simbolo):
    global pantalla
    global valor_a
    global operacion
    valor_a=float(pantalla.get())
    print(valor_a)
    pantalla.delete(0,END)
    if simbolo == "/":
        operacion="dividir"
    elif simbolo == "*":
        operacion="multiplicar"
    elif simbolo == "-":    
        operacion="resta"
    elif simbolo == "+":    
        operacion="sumar"
    print(operacion)
    
    
def resultado_gual():
    global pantalla
    global valor_a
    global valor_b
    global resultado
    global operacion   
    valor_b=float(pantalla.get())
    print(valor_b)
    pantalla.delete(0,END)
    evaluacion=eval(operacion)
    resultado = evaluacion()
    pantalla.insert(END,resultado)
    print(resultado)
#interfaz grafica


#pantalla
pantalla = Entry(ventanas,width=24,bd=6,justify="right")
pantalla.grid(row=0,column=0,columnspan=4)

# botones
siete = Button(ventanas,text=7,width=4,command=lambda:agregar_en_pantalla(7))
siete.grid(row=1,column=0)
ocho = Button(ventanas,text=8,width=4,command=lambda:agregar_en_pantalla(8))
ocho.grid(row=1,column=1)
nueve = Button(ventanas,text=9,width=4,command=lambda:agregar_en_pantalla(9))
nueve.grid(row=1,column=2)
division = Button(ventanas,text="/",width=4,command=lambda:operar("/"))
division.grid(row=1,column=3)
# 2 fila de botones
cuatro = Button(ventanas,text=4,width=4,command=lambda:agregar_en_pantalla(4))
cuatro.grid(row=2,column=0)
cinco = Button(ventanas,text=5,width=4,command=lambda:agregar_en_pantalla(5))
cinco.grid(row=2,column=1)
seis = Button(ventanas,text=6,width=4,command=lambda:agregar_en_pantalla(6))
seis.grid(row=2,column=2)
multiplicacion = Button(ventanas,text="*",width=4,command=lambda:operar("*"))
multiplicacion.grid(row=2,column=3)
# 3 fila de botones
uno = Button(ventanas,text=1,width=4,command=lambda:agregar_en_pantalla(1))
uno.grid(row=3,column=0)
dos = Button(ventanas,text=2,width=4,command=lambda:agregar_en_pantalla(2))
dos.grid(row=3,column=1)
tres = Button(ventanas,text=3,width=4,command=lambda:agregar_en_pantalla(3))
tres.grid(row=3,column=2)
menos = Button(ventanas,text="-",width=4,command=lambda:operar("-"))
menos.grid(row=3,column=3)
# 4 fila de botones
punto = Button(ventanas,text=".",width=4,command=lambda:agregar_en_pantalla("."))
punto.grid(row=4,column=0)
cero = Button(ventanas,text=0,width=4,command=lambda:agregar_en_pantalla(0))
cero.grid(row=4,column=1)
igual = Button(ventanas,text="=",width=4,command=resultado_gual)
igual.grid(row=4,column=2)
mas = Button(ventanas,text="+",width=4,command=lambda:operar("+"))
mas.grid(row=4,column=3)
# 5 barra de borrar
borrar = Button(ventanas,text="Borrar",width=20,command=Borrar)
borrar.grid(row=5,column=0,columnspan=4)



ventanas.mainloop()